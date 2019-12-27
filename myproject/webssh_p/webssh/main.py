# -*- coning:utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.options import options

def main():
    options.parse_command_line()
    loop = tornado.ioloop.IOLoop.current()
    app = make_app(make_hanelers(loop, options), get_app_settints(options))
    ssl_ctx = get_ssl_context(options)
    server_settings = get_server_settings(options)
    app_listen(app, options.port, options.address, server_settings)

if __name__ == '__main__':
    main()
