# -*- coding:utf-8 -*-

import time
import datetime

strform = '%Y-%m-%d %H:%M:%S'

### 一、time ###

# 时间戳：
print(time.time())
print(int(time.time()))

# struct_time
print(time.localtime())

# 字符串
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# sttuct_time 转时间戳
print(time.mktime(time.localtime()))

### 二、 datetime ###

# 时间戳
# datetime模块常用的主要有下面这四个类：

# 1. datetime.date: 是指年月日构成的日期(相当于日历)
# 2. datetime.time: 是指时分秒微秒构成的一天24小时中的具体时间(相当于手表)
# 3. datetime.datetime: 上面两个合在一起，既包含时间又包含日期
# 4. datetime.timedelta: 时间间隔对象(timedelta)。一个时间点(datetime)加上一个时间间隔(timedelta)可以得到一个新的时间点(datetime)。
# 比如今天的上午3点加上5个小时得到今天的上午8点。同理，两个时间点相减会得到一个时间间隔。

print('===  datetime  ===')
print(datetime.date.today())
