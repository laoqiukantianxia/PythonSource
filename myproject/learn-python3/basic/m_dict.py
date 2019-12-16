# -*- coding:utf-8 -*-

from collections  import defaultdict

a = defaultdict(list)

a['a'].append('1')
a['a'].append('1')
a['a'].append('1')
a['b'] = 1
print(a)
print(dict(a))


a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(b.keys() - a.keys())
print(b.items() & a.items())