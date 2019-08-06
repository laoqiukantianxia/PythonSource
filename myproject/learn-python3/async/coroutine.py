# -*- coding:utf-8 -*-

# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息。通过锁机制控制队列和等待
# 改用协程后，生产者生产消息后，直接通过yield跳转到消费者开始执行，带消费者执行完毕后，切换
# 回生产者继续生产，效率极高

'''
yield:
	1. 通常出现在表达式右边，例如 n = yield
	2. 可以产出值，也可以不产出，如果yield后面没有关键字，生成器则产出None
	3. 调用方通过send(n)方式向协程发送数据

协程的四个状态：
	1. GEN_CREATE:等待开始执行
	2. GEN_RUNNING:解释器正在执行，这个状态一般看不到
	3. GEN_SUSPENDED:在yield表达式处暂停
	4. GEN_CLOSED:执行结束

'''


def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print("[CONSUMER] Consuming %s" % n)
		r = '200 OK'


def produce(c):
	c.send(None)  # 启动生成器，使生成器停在yield位置
	n = 0
	while n < 5:
		n = n + 1
		print("[PRODUCER] Producing %s..." % n)
		r = c.send(n)
		print("[PRODUCER] Consumer return: %s" % r)
	c.close()


c = consumer()
produce(c)
