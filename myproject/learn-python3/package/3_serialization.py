# -*- coding:utf-8 -*-

# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 局限：只能用于python，并且可能不同版本的Python彼此都不兼容
# dumps()：把任意对象序列化成一个bytes    //dump()，直接把对象序列化后写入一个file-like Object：
# loads(): 把序列化的对象反序列化写入内存  //load()，从一个file-like Object中直接反序列化出对象


import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)

print(d)

# JSON：
# 要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML/JSON等
# JSON表示出来就是一个字符串，可以被所有语言读取
#    JSON 类型              Python 类型
#      {}                       dict
#      []                       list
#    "string"                   str
#    123.45                   int/float
#    true/false               True/False
#     null                      NULL

import json
d = dict(name='Bill', age=20, score=88)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
