# -*- coning:utf-8 -*-

# 迭代器
class Fib():

    def __init__(self):
        self.a, self.b = 0, 1

    # 实现了__iter__方法的对象是可迭代的
    def __iter__(self):
        return self

    # 实现了__next__()方法的对象是迭代器
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a  # 返回下一个值


class Student(object):
    """
    learn class objects
    """
    # 类变量
    describe = 'say hello...'
    # 属性限制。表示类只能绑定__slots__中含有的属性。对继承的子类不起作用
    __slots__ = ['name', '_age', '_city']

    def __init__(self, name, age, city):   # self 参数代表示例，使用时自动传入
        # 实例变量
        self.name = name    # greet在__slots__中
        self._age = age
        self._city = city

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError('must be an integer!')

    @property
    def city(self): # 只读属性
        return self._city


s1 = Student('Bill', 17, 'shanghai')
# s1.age = '16' # ValueError: must be an integer!
# s1.city = 'beijing'  # AttributeError: can't set attribute
print(s1.name, s1.age, s1.city)


class A(object):
    def __init__(self, name):
        self.name = name

print(A('Bill'))


class A(object):
    def __init__(self, name):
        self.name = name

    # 调试使用
    # def __repr__(self):
    #     return 'College'

    # print打印显示
    def __str__(self):
        return 'College'

print(A('Bill'))



