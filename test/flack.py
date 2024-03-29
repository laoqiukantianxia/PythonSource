# -*- coding:utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_from():
	return '''<form action="/signin" method="post">
		  <p><input name="username"></p>
		  <p><input name="password" type="password"></p>
		  <p><button type="subimt">Sign In</button></p>
		  </form>'''

@app.route('/signin', methods=["POST"])
def signin():
	# 从request对象中读取表单数据
	if request.form['username'] == 'admin' and request.form['password']=='123456':
		return '<h3>Hello, admin</h3>'
	return '<h3>Bab username or password</h3>'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0' ,port=8082)

