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

for i in test(a):
    print(i)

print(list(test(a)))