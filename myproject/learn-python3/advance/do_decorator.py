import functools
import time


def log1(func):
	@functools.wraps(func) # 保持属性不变
	def wrapper(*args, **kw):
		print("call %s():" % func.__name__)
		return func(*args, **kw)
	return wrapper

@log1
def now():
	print("2019")


if __name__ == "__main__":
	now()
	print(now.__name__)
