# -*- coding:utf-8 -*-

import time
import datetime

print(time.time())
print(time.localtime())
print(time.localtime(time.time()))

# 格式化时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
