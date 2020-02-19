# -*- coding:utf-8 -*-

# 1. 函数abc
## a. 函数定义：
###  使用def语句，依次写出函数名、括号、括号中的参数和冒号:
### 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
## b. 函数的参数
### 1）. 位置参数
### 2）. 默认参数（arg = None，必须指向不可变对象）
### 3）. 可变参数（*args, args接收的是一个tuple）
### 4）. 关键字参数（**kw，kw接收的是一个dict）
### 5）. 命名关键字参数
## c. 参数组合
### 参数定义的顺序必须是：必选参数（位置参数）、默认参数、可变参数、命名关键字参数和关键字参数。


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1,2)
f1(1,2, [1, 2, 3])
f1(1, 2, [1,2,3,], [1,2,3])
f1(1, 2, [1,2,3,], *[1,2,3])

# 2. lambda
f1 = lambda x, y: x + y
print(f1(2, 3))
f2 = lambda: 'test'
print(f2())

# 2. 高阶函数
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
## a. 变量可以指向函数
## b. 函数名也是变量
## c. 传入函数
f = abs
print(-10, f, f(-10))
abs = 10
print(abs)

def test(x, y, f):
    return f(x) + f(y)
print(test(-10, -10, f))

## 2.1 map
### map()函数接收两个参数，一个是函数，一个是Iterable，
### map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

l = [1, -9, 29, 10, -30, -29]
print(list(map(f, l)))

## 2.2 reduce
### 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
### reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x,y):
    return x+y
l = [1, 2, 3, 4, 5]
print(reduce(add, l))

#### example：将[1, 3, 5, 7, 9] 变换成13579
l = [1, 3, 5, 7, 9]
def fn(x, y):
    return x * 10 + y
print(reduce(fn, l))

#### example:str2int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x*10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('123456'))