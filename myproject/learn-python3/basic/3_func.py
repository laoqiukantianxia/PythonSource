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

