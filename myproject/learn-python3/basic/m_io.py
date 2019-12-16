# -*- coding:utf-8 -*-

"""
数据读写不一定是文件，也可以在内存中读写。
StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
"""

from io import StringIO, BytesIO

f = StringIO()
f.write('hello world\n')
f.write('Python3.8!')
print(f.getvalue())

f = BytesIO()
f.write('你好'.encode('utf-8'))
print(f.getvalue())