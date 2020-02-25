import time

# 时间戳：1582608713
print(int(time.time()))
# 标准时区时间
print(time.gmtime())      # 标准时间
# struct_time (tm_year=2020, tm_mon=2, tm_mday=25, tm_hour=5, tm_min=31, tm_sec=53, tm_wday=1, tm_yday=56, tm_isdst=0)
print(time.localtime())   # 本地时间
# 获取指定时间属性
print(time.localtime().tm_year)
# Tue Feb 25 13:31:53 2020
print(time.asctime(time.localtime()))
# 格式化时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
# 时间的运算

# 2020-02-25 13:48:35.681490
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today()+datetime.timedelta(days=2))

