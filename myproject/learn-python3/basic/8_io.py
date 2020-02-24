# -*- coding:utf-8 -*-

# 1. 文件读写：
# 在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
# 读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），
# 或者把数据写入这个文件对象（写文件）。
#


# test1
f = open('test.txt', 'w')
if f:
    print(f.write('Hello,world'))  # 一次性读取全部文件


# test2
# read(size)  # size个字节
# readline()  # 每次读取一行内容
# readlines() # 一次读取所有内容并按行返回list
with open('test.txt', 'r') as f:
    print(f.read())

# test3
# file-like object
# file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO，在内存中读写str
# BytesIO， 在内存中读写字节
from io import StringIO, BytesIO
s = StringIO()
s.write('Hello')
s.write(',')
s.write('StringIO!')
print(s.getvalue())

b = BytesIO()
b.write('你好'.encode('utf8'))
print(b.getvalue())

