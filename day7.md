### day7

- 学习内容
	#### 线程
- 引用
	`import threading`
- 基本方法
	- 声明线程，并调用相关函数代码
		`threading.Thread(target=[function])`
	- 运行线程
		`threading.start()`
	- 查看当前运行线程
		`threading.current_thread()`
	```
	def run():
		for i in range(4):
			print('%s正在运行线程' % threading.current_thread()) # 查看当前运行的线程
			time.sleep(1)
	t1 = threading.Thread(target=run) # target 调用方法
	t1.start()
	threading.enumerate() # 查看调用多少个线程
	```
 - 继承使用
 	```
 	class MyThread(threading.Thread):
 		def run(self):
 			pass
 	t1 = MyThread(name='mythread') # 可以命名线程名字
 	t1.start()
 	```
 - 全局变量&线程加锁/解锁
 	- 函数中调用全局变量的时候，使用global来声明变量是来自全局。
 	- 问题：
 		- 如果多个线程调用同一个变量或程序，会出现数据不正确或脏数据，不完整。
 	- 解决：
 		- 加锁和解锁，规定一些程序只有一个线程运行。
 		```
 		glock = threading.Lock() # 声明锁
 		glock.acquire() # 加锁
 		glock.release() # 释放锁
 		```
 	- 例子
 		- 生产者&消费者：如果大于生产和消费次数，就释放锁。
 		- condition版生产者与消费者，比较之前生产者和消费者不断加锁和解锁，十分耗CPU。当没有数据可以阻塞，等待数据。
 			- wait() 线程阻塞，并解锁
 			- notify() 唤醒线程，并加锁，执行下面的代码（不包括加锁和解锁）
 			- notify_all()
 			```
 			# 声明condition
 			gcondition = threading.Condition()
 			while x < y
 				gcondition.wait()
 			gcondition.notify_all()
 			```
 - Queue线程安全队列
 	- 引用
 		`from queue import Queue`
 	- 使用
 	```
 	q = Queue(4) # 队列大小
 	def q_put():
	 	for i in rang(4):
	 		q.put(i) # 放数据
	def q_get():
	 	while True:
	 		q.get() # 获取数据 默认参数block = False，True指的是如果没有数据，一直阻塞等待。
 	t1 = threading.Thread(target=q_put,args=[q]) # args指参数
 	t2 = threading.Thread(target=q_get,args=[q])
 	t1.start()
 	t2.start()
 	```
 - GIL全局解析锁器是cpython解析器的一个东西
 	- 背景：python用cpython解析器，其线程是假多线程，不可以运行多核。
	 	- GIL 管理同一时刻运行一个线程，保证线程安全。
	 	- 在IO操作上建议使用多线程提高效率。有些CPU不建议使用多线程，使用多进程。