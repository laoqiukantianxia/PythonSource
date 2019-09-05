# -*- coding:utf-8 -*-
"""
生成器：
    带有 yield 的函数在 Python 中被称之为 generator（生成器），
    之所以引入生成器，是为了实现一个在计算下一个值时不需要浪费空间的结构。

    在do_iter.py中，代码3远没有代码1整洁。但生成器（yield）既可以保持代码1的简洁性，又可以保持代码3的效果。
"""


# 代码4
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


# 执行
for n in fab(5):
    print
    n
