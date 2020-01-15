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

class MyClass():
    """
    learn class objects
    """
    # 类变量
    describe = 'say hello...'
    def __init__(self):
        # 实例变量
        self.greet = 'hello'

    def __repr__(self):
        return 'myclass'

    def __str__(self):
        return 'myclass'

    @staticmethod
    def sta_greeting():
        return 'hello, static method'

    @classmethod
    def cls_greeting(cls):
        return 'hello, class method'

    def self_greeting(self):
        return self.greet

print(MyClass.cls_greeting())

print(MyClass.sta_greeting())
print(MyClass().self_greeting())

# print(MyClass.__name__)
# #print(MyClass().__name__) :error
# print(MyClass.__doc__)
# print(MyClass().__doc__)
# print(MyClass.__dict__)
# print(MyClass().__dict__)
# print(MyClass)
# print(MyClass())
# print(dir(MyClass()))
# print(dir(MyClass))
#
# print(MyClass)




