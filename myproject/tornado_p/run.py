# -*- coning:utf-8 -*-
import logging

import tornado.ioloop
import tornado.web

"""
tornado 四大组件：
1. ioloop实例：tornado.ioloop.IOLoop.current()，默认的ioloop实例，全局的tornado时间循环，服务器的引擎核心。
    一个ioloop包含多个app(管理多个服务端口)
2. app实例：   挂接一个服务端套接字对外提供服务，一个iloop实例可以有多个app实例
    一个app包含一个路由表            
3. 路由表：    将指定的url规则和handler挂接起来
    一个路由表包含多个handler
4. handler类： 业务逻辑，处理客户端请求


"""


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")

def make_app():
    return tornado.web.Application([(r'/', MainHandler),])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    print('Listen Port [8888]...')
    tornado.ioloop.IOLoop.current().start()