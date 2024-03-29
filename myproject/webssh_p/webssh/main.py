# -*- coning:utf-8 -*-
import logging

import tornado.ioloop
import tornado.web
from tornado.options import options

from webssh import handler
from webssh.handler import IndexHandler, WsockHandler, NotFoundHandler
from webssh.settings import (
    get_app_settings, get_host_keys_settings, get_policy_setting,
    get_ssl_context, get_server_settings
)


def make_handlers(loop, options):
    host_keys_settings = get_host_keys_settings(options)
    policy = get_policy_setting(options, host_keys_settings)

    handlers = [
        (r'/', InidexHandler, dict(loop=loop, policy=policy,
                                   host_keys_settings=host_keys_settings)),
        (r'/ws', WsockHandler, dict(loop=loop))
    ]

    return handlers

def make_app(handlers, settings):
    settings.update(default_handler_class=NotFoundHandler)
    return tornado.web.Application(handlers, **settings)

def app_listen(app, port, address, server_settings):
    app.listen(port, address, **server_settings)
    if not server_settings.get('ssl_options'):
        server_type = 'http'
    else:
        server_type = 'https'
        handler.redirectint = True if options.redirect else False

    logging.info('Listening on {}:{} ({})'.format(address, port, server_type))

def main():
    options.parse_command_line()
    loop = tornado.ioloop.IOLoop.current()
    app = make_app(make_hanelers(loop, options), get_app_settints(options))
    ssl_ctx = get_ssl_context(options)
    server_settings = get_server_settings(options)
    app_listen(app, options.port, options.address, server_settings)
    loop.start()

if __name__ == '__main__':
    main()
