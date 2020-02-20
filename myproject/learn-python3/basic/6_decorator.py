# -*- coding:utf-8 -*-


"""
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。
"""

import functools
import logging
import time

format = '%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

#
# def log(func):
#     @functools.wraps(func)  # 保持属性不变
#     def wrapper(*args, **kw):
#         print("call %s():" % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('start {}'.format(func.__name__))
        func(*args, **kwargs)
    return wrapper
@log
def now():
    logging.info("hello now")


def decorator(f):
    def wrapper(*args, **kw):
        # TODO
        return f(*args, **kw)
    return wrapper

# def log1(test):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print("%s:call %s():" % (test, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator
#
#
# @log1(time.strftime('%Y-%m-%d %H:%M:%S'))
# def now1():
#     print("hello now1")


if __name__ == "__main__":
    now()
    logging.info(now.__name__)  # now.__name__ = wrapper
    # now1()
    # print(now1.__name__)  # now.__name__ = now1
