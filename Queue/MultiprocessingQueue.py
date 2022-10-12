from multiprocessing import Queue

mq = Queue(maxsize=3)
mq.put(10)
mq.put(20)
print(mq.get())
