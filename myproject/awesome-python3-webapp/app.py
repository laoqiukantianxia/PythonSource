# -*- coding:utf-8 -*-

'''
（一）asyncio:在3.4版本引入的标准库，内置了对异步io的支持

1> @asyncio.coroutine:把generator标记为coroutine类型，然后把coroutine放到eventloop中执行
2> 异步操作在coroutine中通过yield from 完成：yield from语法可以方便地调用另一个generator
3> 获取event_loop:loop = asyncio.get_event_loop()
4> 执行coroutine：loop.run_until_complete(hello())
5> 关闭loop：loop.close()

        import asyncio

        @asyncio.coroutine
        def hello():
        print("Hello world!")
        # 异步调用asyncio.sleep(1):
        r = yield from asyncio.sleep(1)
        print("Hello again!")

        # 获取EventLoop:
        loop = asyncio.get_event_loop()
        # 执行coroutine
        loop.run_until_complete(hello())
        loop.close()

（二）asyno/await:Python 3.5开始引入了新的语法,可以让coroutine的代码更简洁易读。
两步简单替换：
    1> 把@asyncio.coroutine替换为async；
    2> 把yield from替换为await


    async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

'''

import logging
import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

logging.basicConfig(level=logging.INFO)

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

#协程不能直接运行，需要把协程加入到事件循环（loop）。asyncio.get_event_loop方法可以创建一个事件循环
loop = asyncio.get_event_loop()
#使用run_until_complete将协程注册到事件循环，并启动事件循环。
loop.run_until_complete(init(loop))
loop.run_forever()

