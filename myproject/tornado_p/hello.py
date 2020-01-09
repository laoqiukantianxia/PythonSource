# -*- coning:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define('port', default=8888, help='run on the given port', type=int)


class IndexHandler(tornado.web.RequestHandler):
    async def get(self):
        greetint = self.get_argument('greeting', 'Hello')
        self.write(greetint + ', friendly user!')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r'/', IndexHandler)])
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
