import urllib

import tornado.httpclient
import tornado.ioloop
import tornado.web
import tornado.options


from tornado.options import define, options
define('port', default=8000, help='run on the given port', type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.HTTPClient()
        response = client.fetch('https://www.baidu.com/')
        self.write(response.code)
        # self.write('response.code')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r'/', IndexHandler)])
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
