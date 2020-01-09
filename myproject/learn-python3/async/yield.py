#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio


def test(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [0,1,4,2,7,1,2,5,7,2,0,5,0,8,9,6,3]

f = test(a)

print(f)


print(f.send(None))
print(f.send(None))
print(f.send(None))
print(next(f))
print(list(f))

for i in f:
    print(i)

# print(list(f))

def test2():
    x = 1
    while True:
        y = yield x
        if y:
            x += y

fun = test2()
print(fun)
print(next(fun))
print(next(fun))
print(next(fun))
print(fun.send(None))
print(fun.send(2))
print(fun.send(2))