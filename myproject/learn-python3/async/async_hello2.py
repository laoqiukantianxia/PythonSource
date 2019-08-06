#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio


'''
（二）asyno/await:Python 3.5开始引入了新的语法,可以让coroutine的代码更简洁易读。
两步简单替换：
    1> 把@asyncio.coroutine替换为async；
    2> 把yield from替换为await
'''


async def hello():
    print("Hello world!(%s)" % threading.currentThread())
    await asyncio.sleep(1)
    print("Hello again!(%s)" % threading.currentThread())



# 获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))

loop.close()
