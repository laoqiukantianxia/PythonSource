# -*- coding:utf-8 -*-

# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息。通过锁机制控制队列和等待
# 改用协程后，生产者生产消息后，直接通过yield跳转到消费者开始执行，带消费者执行完毕后，切换
# 回生产者继续生产，效率极高

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print("[CONSUMER] Consuming %s" % n)
		r = '200 OK'

def produce(c):
	c.send(None) # 启动生成器，使生成器停在yield位置
	n = 0
	while n < 5:
		n = n + 1
		print("[PRODUCER] Producing %s..." % n)
		r = c.send(n)
		print("[PRODUCER] Consumer return: %s" % r)
	c.close()

c = consumer()
produce(c)
