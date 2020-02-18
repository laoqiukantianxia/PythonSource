
#================================1. 字符串编码========================
# 1. ascii编码：最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为`ASCII`编码，
#  比如大写字母`A`的编码是`65`，小写字母`z`的编码是`122`。
# 2. Unicode编码：Unicode把所有语言都统一到一套编码里，ASCII编码是1个字节，而Unicode编码通常是2个字节。
# （但是，如果文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。）
# 3. utf-8编码：可变长度编码，把一个Unicode字符根据不同的数字大小编码成1-6个字节

# 所以，
# *1.* 计算机内存中，统一使用Unicode编码：用空间换时间
# *2.* 当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码,减少延迟或节省带宽


# 1. encode，编码：
#  将Unicode字符按照编码规则（如UTF-8）编成字节序列
# 2. decode，解码：
#  将字节序列按照编码规则（如UTF-8）解释成unicode形式。

# python3中的字符串：
# 1. 区分为文本字符串类型-使用Unicode数据存储，str对象；字节字符串类型-有具体编码形式，bytes对象
# 2. 一般情况下，实例化一个字符串会得到一个str对象；
# （很多人都说，Python3默认是Unicode，也就是这个意思。）
# 3. str 对象有一个encode方法，bytes 对象有一个decode方法。

# python2中的字符串
# 在Python3中的 str 对象在Python2中叫做 unicode ，感觉很通俗对吧？
# 但 bytes 对象在Python2中叫做 str ，对。。就是你平时用的 str ， 默认的那个。。。
# 1. Python2中的 str （字节） 对象，有一个 encode 方法，它就是用来报错的，永远都别使用它！！！
# 2. 同样的，unicode （文本字符） 对象也有一个用来报错的 decode 方法。
# 3. 所以在用2.X时，请养成在字符串加上 u 前缀的习惯，统一编码UTF-8

# 参考链接：https://blog.csdn.net/yanghuan313/article/details/63262477

# -*- coning:utf-8 -*-
# 字符编码问题，字符串存在编码格式，赋值给变量时，str类型是以默认编码方式编码，在赋给变量。因此不能解码码
# 在python3, 默认的编码方式就是utf-8，因此上面一行加与不加都可
# 在python2中，默认编码方式是ASCII码，要想输出中文，必须制定编码格式
#

a = '谢谢你'.decode('utf8')
print(a, type(a), len(a))

a = '谢谢你'.encode('utf8')  # 一个汉字占三个字节
print(a, type(a), len(a))

a = 'ABC'.encode('ascii')
print(a, type(a), len(a))  # b'ABC'   bytes 类型，每个字符占一个字节

