#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio

'''
一）asyncio:在3.4版本引入的标准库，内置了对异步io的支持

1> @asyncio.coroutine:把generator标记为coroutine类型，然后把coroutine放到eventloop中执行
2> 异步操作在coroutine中通过yield from 完成：yield from语法可以方便地调用另一个generator
3> 获取event_loop:loop = asyncio.get_event_loop()
4> 执行coroutine：loop.run_until_complete(hello())
5> 关闭loop：loop.close()
'''

"""
把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，
而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
"""
@asyncio.coroutine
def hello():
    print("Hello world!(%s)" % threading.currentThread())
    yield from asyncio.sleep(1)
    print("Hello again!(%s)" % threading.currentThread())


# 获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello()]
#tasks = [hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))

loop.close()
