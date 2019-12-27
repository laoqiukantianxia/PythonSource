# -*- coding:utf-8 -*-
import logging

import tornado.websocket
from tornado.ioloop import IOLoop
from tornado.iostream import _ERRNO_CONNRESET
from tornado.util import errno_from_exception

BUF_SIZE = 32 * 1024
clients = {}  # {ip: {id: worker}}


def clear_worker(worker, clients):
    ip = worker.src_addr[0]
    workers = clients.get(ip)
    assert worker.id in workers
    workers.pop(worker.id)

    if not workers:
        clients.pop(ip)
        if not clients:
            clients.clear()


def recycle_worker(worker):
    if worker.handler:
        return
    logging.warning('Recycling worker {}'.format(worker.id))
    worker.close(reason='worker recycled')


class Worker(object):
    def __init__(self, loop, ssh, chan, dst_addr, user, filter_command=None):
        self.loop = loop
        self.ssh = ssh
        self.chan = chan
        self.dst_addr = dst_addr
        self.fd = chan.fileno()
        self.id = str(id(self))
        self.data_to_dst = []
        self.handler = None
        self.mode = IOLoop.READ
        self.closed = False
        self.filter_command = filter_command
        self.append_command = []
        self.user = user

    def __call__(self, fd, events):
        if events & IOLoop.READ:
            self.on_read()
        if events & IOLoop.WRITE:
            self.on_write()
        if events & IOLoop.ERROR:
            self.close(reason='error event occurred')

    def set_handler(self, handler):
        if not self.handler:
            self.handler = handler

    def update_handler(self, mode):
        if self.mode != mode:
            self.loop.update_handler(self.fd, mode)
            self.mode = mode
        if mode == IOLoop.WRITE:
            self.loop.call_later(0.1, self, self.fd, IOLoop.WRITE)

    def on_read(self):
        # 接收ssh服务器返回
        logging.debug('worker {} on read'.format(self.id))
        try:
            data = self.chan.recv(BUF_SIZE)
        except (OSError, IOError) as e:
            logging.error(e)
            if errno_from_exception(e) in _ERRNO_CONNRESET:
                self.close(reason='chan error on reading')
        else:
            logging.debug('{!r} from {}:{}'.format(data, *self.dst_addr))
            if not data:
                self.close(reason='chan closed')
                return
            logging.debug('{!r} to {}:{}'.format(data, *self.handler.src_addr))
            self.match_command_read(data)
            try:
                self.handler.write_message(data, binary=True)
            except tornado.websocket.WebSocketClosedError:
                self.close(reason='websocket closed')

    def on_write(self):
        logging.debug('worker {} on write'.format(self.id))
        if not self.data_to_dst:
            return

        data = ''.join(self.data_to_dst)
        logging.debug('{!r} to {}:{}'.format(data, *self.dst_addr))

        if self.match_command_write(data):
            try:
                sent = self.chan.send(data)
            except (OSError, IOError) as e:
                logging.error(e)
                if errno_from_exception(e) in _ERRNO_CONNRESET:
                    self.close(reason='chan error on writing')
                else:
                    self.update_handler(IOLoop.WRITE)
            else:
                self.data_to_dst = []
                data = data[sent:]
                if data:
                    self.data_to_dst.append(data)
                    self.update_handler(IOLoop.WRITE)
                else:
                    self.update_handler(IOLoop.READ)
        else:
            self.data_to_dst = []
            return


    def match_command_write(self, data):
        # 没有白名单, 全部开放
        if not self.filter_command:
            return True
        data_len = len(data)
        if data_len == 1:
            if data == '\x03':  # ctrl + c
                self.append_command = []
                logging.info('[write] clean append_command because [crtl + c].')
                return True
            if data == '\r\n' or data == '\r':
                try:
                    if self.append_command:
                        mem_command = ''.join(self.append_command).replace(' ', '')
                        logging.info('[write] mem_command:{}'.format(mem_command))

                        for command in self.filter_command:
                            command = command.replace(' ', '')
                            if mem_command.find(command) == 0:  # 前缀匹配
                                self.append_command = []  # 匹配到命令后清空内存
                                logging.info('[write] clean append_command because matched.')
                                return True
                        logging.info(
                            '[write] match command: [{}] is not allow!Press [Ctrl + c] return'.format(mem_command))
                        self.handler.write_message('\r\nThis command is not allowed!\r\nPress [Ctrl + c] return...',
                                                   binary=True)
                        return False
                    else:
                        return True
                except:
                    pass
            elif data == '\x7f':  # 删除键
                if self.append_command:
                    self.append_command.pop()
            elif data == '\t':
                pass
            else:
                self.append_command.append(data)
        else:
            self.append_command.append(data)
        logging.debug('[write] append_command:{}'.format(self.append_command))
        return True

    def match_command_read(self, data):
        if not self.filter_command or not self.append_command:
            return
        if len(data) > 1:
            data = data.decode('utf-8').replace(' ', '')
            # if data.find(self.user) != -1:
            #     self.append_command = []
            #     return
            for command in self.filter_command:
                command = command.replace(' ', '')
                try:
                    # 使用tab或者翻页键时，命令匹配
                    if command.find(data) != -1:
                        self.append_command.append(data)
                        logging.debug('[read] append_command:{}'.format(self.append_command))
                    elif data.find(command) != -1:
                        self.append_command = []
                        self.append_command.append(command)
                        logging.debug('[read] append_command:{}'.format(self.append_command))
                except:
                    pass

    def close(self, reason=None):
        if self.closed:
            return
        self.closed = True

        logging.info(
            'Closing worker {} with reason: {}'.format(self.id, reason)
        )
        if self.handler:
            self.loop.remove_handler(self.fd)
            self.handler.close(reason=reason)
        self.chan.close()
        self.ssh.close()
        logging.info('Connection to {}:{} lost'.format(*self.dst_addr))

        clear_worker(self, clients)
        logging.debug(clients)
