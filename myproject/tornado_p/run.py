# -*- coning:utf-8 -*-
import logging

import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.httpclient

"""
tornado特点：非阻塞式服务器，而且速度相当快。得力于非阻塞方式和对epoll的运用，
             Torando每秒可以处理数以千计的连接，因此Tornado是实时web服务的理想框架。



tornado 四大组件：
1. ioloop实例：tornado.ioloop.IOLoop.current()，默认的ioloop实例，全局的tornado时间循环，服务器的引擎核心。
    一个ioloop包含多个app(管理多个服务端口)
2. app实例：   挂接一个服务端套接字对外提供服务，一个iloop实例可以有多个app实例
    一个app包含一个路由表            
3. 路由表：    将指定的url规则和handler挂接起来
    一个路由表包含多个handler
4. handler类： 业务逻辑，处理客户端请求

"""


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, World")

# arguments-获取所有GET或POST的参数
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('<html><body><form action="/" method="post">'
#                    '<input type="text" name="message">'
#                    '<input type="submit" value="Submit">'
#                    '</form></body></html>')
#
#     def post(self):
#         self.set_header("Content-Type", "text/plain")
#         self.write("You wrote " + self.get_argument("message"))

# # cookie
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         if not self.get_cookie("mycookie"):
#             self.set_cookie("mycookie", "myvalue")
#             self.write("Your cookie was not set yet!")
#         else:
#             self.write("Your cookie was set!")

# 安全cookie-get_secure_cookie,get_secure_cookie
# cookie 很容易被客户端伪造。使用时可以对cookie进行签名以防止伪造。
# 使用时需要在创建app时，提供一个秘钥，参数为cookie_secret。
# application = tornado.web.Application([
#     (r"/", MainHandler),
# ], cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         if not self.get_secure_cookie("mycookie"):
#             self.set_secure_cookie("mycookie", "myvalue")
#             self.write("Your cookie was not set yet!")
#         else:
#             self.write("Your cookie was set!")

# class BaseHandler(tornado.web.RequestHandler):
#     def get_current_user(self):
#         return self.get_secure_cookie('user')
#
# class MainHandler(BaseHandler):
#     def get(self):
#         if not self.current_user:
#             self.redirect('/login')
#             return
#         name = tornado.escape.xhtml_escape(self.current_user)
#         self.write('Hello, ' + name)
#
#
# class LoginHandler(BaseHandler):
#     def get(self):
#         self.write('<html><body><form action="/login" method="post">'
#                    'Name: <input type="text" name="name">'
#                    '<input type="submit" value="Sign in">'
#                    '</form></body></html>')
#
#     def post(self):
#         self.set_secure_cookie("user", self.get_argument("name"))
#         self.redirect("/")


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://friendfeed-api.com/v2/feed/bret",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        json = tornado.escape.json_decode(response.body)
        self.write("Fetched " + str(len(json["entries"])) + " entries "
                   "from the FriendFeed API")
        self.finish()

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        #(r'/login', LoginHandler)
        ],
        cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    print('Listen Port [8888]...')
    tornado.ioloop.IOLoop.current().start()
