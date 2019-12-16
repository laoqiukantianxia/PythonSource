# -*- coding:utf-8 -*-

"""
数据读写不一定是文件，也可以在内存中读写。
StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
"""

from io import StringIO, BytesIO
