# -*- coding:utf-8 -*-

def test(age, num, **user):
    print(age, num, user.pop('test', None), user.pop('name', None))


user = {
    'test': 15,
    'name': 'ming'
}
test(1, 2, **user)