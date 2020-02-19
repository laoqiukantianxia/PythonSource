# -*- coding:utf-8 -*-


"""
可迭代对象（Iterable）：只要定义了__iter__()方法，我们就说该对象是可迭代对象，并且可迭代对象能提供迭代器。
                      a. 集合数据类型，如list、tuple、dict、set、str等；
                      b. 是generator，包括生成器和带yield的generator function。

迭代器、迭代对象      ：实现了__next__()或者next()(python2)方法的称为迭代器，迭代器仅仅在迭代到某个元素时才计算该元素，
                        而在这之前或之后，元素可以不存在或者被销毁，因此只占用固定的内存。


'for' 语法糖：
    在for循环中，Python将自动调用工厂函数iter()获得迭代器，自动调用next()获取元素，还完成了检查StopIteration异常的工作。

"""


# from collections import Iterable, Iterator

# 可迭代的

class MyRange(object):
    def __init__(self, n):
        self.idx = 0
        self.n = n

    def __iter__(self):  # 这个可迭代对象的的迭代对象就是它自身。这会导致一个问题，无法重复迭代，
        return self

    def __next__(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration()


m = MyRange(3)
for i in m:
    print(i)

# 第二次执行时，无法迭代
for i in m:
    print(i)


## 为什么使用迭代器？
# 代码1
# 直接在函数fab(max)中用print打印会导致函数的可复用性变差，因为fab返回None。其他函数无法获得fab函数返回的数列。
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


# 代码2
# 代码2满足了可复用性的需求，但是占用了内存空间。
def fab(max):
    L = []
    n, a, b = 0, 0, 1
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


# 代码3，定义并使用迭代器
# Fabs 类通过 next() 不断返回数列的下一个数，内存占用始终为常数

class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


for key in Fab(5):
    print(key)

