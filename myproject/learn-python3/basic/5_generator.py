# -*- coding:utf-8 -*-
"""
生成器：
    带有 yield 的函数在 Python 中被称之为 generator（生成器），
    之所以引入生成器，是为了实现一个在计算下一个值时不需要浪费空间的结构。

    在do_iter.py中，代码3远没有代码1整洁。但生成器（yield）既可以保持代码1的简洁性，又可以保持代码3的效果。
"""

# 通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间，如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。
# 因此，没有必要创建完整的列表（节省大量内存空间）。在Python中，我们可以采用生成器：边循环，边计算的机制—>generator

# 代码4
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


# 执行
for n in fab(5):
    print(n)


# 将列表生成式中[]改成()之后数据结构是否改变？是，从列表变为生成器

l = [x*x for x in range(10)]
print(l)
l = (x*x for x in range(10))
print(l)
print(l.send(None))
print(l.send(None))
print(l.send(None))