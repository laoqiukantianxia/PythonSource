# -*- coding:utf-8 -*-
import requests
from io import BytesIO
from urllib.parse import urlencode


url = 'http://localhost:8880'
headers = {'X-Fake-IP': '101.231.57.146'}

# 1. 快速上手
## get请求
r = requests.get(url, headers=headers)
print('No1. ', r.status_code, r.url, r.text)

## get + 传递url参数(params)
payload = {'firstname': 'qiu', 'lastname': 'shichao'}
r = requests.get(url, params=payload)
print('No2. ', r.status_code, r.url, r.text)

## get + 传递url参数(urlencode)
payload = {'firstname': 'qiu', 'lastname': 'shichao'}
url = url + '?' + urlencode(payload)
r = requests.get(url)
print('No3. ', r.status_code, r.url, r.text)


## post + 传递url参数 + data
payload = {'firstname': 'qiu', 'lastname': 'shichao'}
f = BytesIO()
f.write(b'who are you?')
r = requests.post(url, data=f)
print('No4. ', r.status_code, r.url, r.text)

## post
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r.status_code)



## 定制请求头
url = 'https://monitor.wiwide.com/v1/upload'
headers = {'X-Fake-IP': '101.231.57.146'}
r = requests.get(url, headers=headers)
print(r.status_code)

# 2. 会话对象
"""
会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie
"""

## cookie
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

#print(r.text)

