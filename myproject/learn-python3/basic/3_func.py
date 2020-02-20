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
print(reduce(add, l))  # 15

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


## 2.3 filter
### filter()函数用于过滤序列，filter()接收一个函数和一个序列，
### filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

### 关键在于正确实现一个“删选”函数，
### ilter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
### 需要用list()函数获得所有结果并返回list。

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,l)))

#### example：打印1000以内的素数

#  从3开始的奇数序列（偶数中只有2是素数）
#  是一个生成器，无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#  定义删选函数:n的倍数返回false
def _not_divisible(n):
    return lambda x: x % n > 0

# 定义生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)  # 构造新的序列

for n in primes():
    if n < 100:
        print(n)
    else:
        break

#### example: 回数-从左向右读和从右向左读一样的数，12321

#### one way:
print(list(filter(lambda n: str(n) == str(n)[::-1], range(1000))))

#### two way:
def is_palindrome(n):
    nn = str(n)
    return nn == nn[::-1]
print(list(filter(is_palindrome, range(1000))))


## 2.4 sorted
## 排序函数，默认升序
## key-指定函数作用在目标对象上；reverse=True-反向排序
l = [-1, 0, -9, 10, 4, 3, 9]
abs=f  # 见前文
print(sorted(l))
print(sorted(l, reverse=True))
print(sorted(l, key=abs))  # 根据绝对值大小进行排序

#### example:
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key=lambda x: x[0]))   # 按名字进行排序
print(sorted(L, key=lambda x: x[1]))   # 按分数进行排序

# 3. 返回函数 （闭包）
## 将结果作为函数值返回;
## 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#  当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”
l = [1, 2, 3, 4, 5]
def _add(*args):
    ns = 0
    for i in args:
        ns = ns + i
    return ns
print(_add(*l))

# 不需要立即求和，后面代码中根据需要在计算
def _lazy_sum(*args):
    def _add():
        ns = 0
        for i in args:
            ns = ns + i
        return ns
    return _add

f = _lazy_sum(*l)
print(f)
print(f())



# 闭包，返回的函数并没有立刻执行，而是直到调用了f()才执行。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)

    return fs
f1, f2, f3 = count()
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
print(f1(), f2(), f3())   # 结果是9,9,9，而不是1,2,3

def count2():
    fs = []
    def f(i):
        def g():
            return i*i
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()
print(f1(), f2(), f3())

def count3():
    fs = []
    def f(i):
        return lambda: i*i
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()
print(f1(), f2(), f3())

# global: 如果局部变量要修改全局变量，应在局部声明全局变量，同事全部变量的值也会改变;
#         如果局部不声明全局变量，并且不修改全局变量，则可以正常使用。
# nonlocal: 声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
def createCounter():
    s = 0
    def counter():
        nonlocal s
        s = s+1
        return s
    return counter

c = createCounter()
print(c(), c(), c())


# 匿名函数
f = lambda x: x*x

# 偏函数,固定函数的某些参数，返回新的函数
from functools import partial
partial