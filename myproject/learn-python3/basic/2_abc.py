# -*- coding:utf-8 -*-


#1.list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['zhao', 'qiao', 'sun', 'li']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])
print(classmates.append('Bill'), classmates)
print(classmates.insert(1, 'Tom'), classmates)
print(classmates.pop(), classmates)
for i, v in enumerate(classmates):
    print(i, v)

# 列表生成式
l = [x * x for x in list(range(1, 11))]
print(l)
l = [x * x for x in list(range(1,11)) if x % 2 == 0]
print(l)
import os
l = [d for d in os.listdir('.')]
print(l)
#2. tuple和list非常类似 ，也是有序列表。 但是tuple一旦初始化就不能修改
print('======================tuple=============================')
classmates = ('zhao',)
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])

#3. dict，字典，键-值（key-value）存储，具有极快的查找速度。
# a. dict是一种用空间换时间方法
# b. dict的key必须是不可变对象。
print('======================dict=============================')
classmates = {'zhao': 1, 'qiao': 2, 'sun': 3, 'li': 4}
print(classmates)
print('zhou' in classmates)
print(classmates.get('zhou', None))
print(classmates.pop('zhou', None))
for k in classmates:
    print('key: ', k)
for v in classmates.values():
    print('value: ', v)
for k, v in classmates.items():
    print(k, v)



#4. set, dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
classmates = ['zhao', 'qian', 'sun', 'li', 'zhao', 'qiao', 'sun', 'li']
s = set(classmates)
print(s)  # 不表示位置信息
print(s.add(10086), s)


## 交集和并集处理
a = set([1, 2, 3])
b = set([2, 3, 4])
print(a & b)   # 交集 {2,3}
print(a | b)   # 并集 {1,2,3,4}

# slice，切片
L = ['zhao', 'qian', 'sun', 'li']
print(L[:3])
