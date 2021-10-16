import time
# import os
# from multiprocessing import Process
from threading import Thread


# import threading
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from queue import Queue


# pid = os.getpid()
#
# Make process to watch on oit in linux console
# while True:
#     print(pid, time.time())
#     time.sleep(2)


# Only in linux console
# Create new process by using fork()
#
# pid = os.fork()
# if pid == 0:
#     while True:
#         print('Child:', os.getpid())
#         time.sleep(5)
# else:
#     print('Parent:', os.getpid())
#     os.wait()


# Create process with multiprocessing
# Only in linux console
#
# def foo(name):
#     print("hello", name)
#
#
# p = Process(target=foo, args=("Oleg", ))
# p.start()
# p.join()

# Only in linux console
# Inheritance from Process to make new process(override method 'run')
#
# class PrintProcess(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print("Hello,", self.name)
#
#
# p = PrintProcess("Oleg")
# p.start()
# p.join()

# Creating new thread in the same process (thread is a part of a process)
#
# def foo(name):
#     print("hello", name)
#
#
# th = Thread(target=foo, args=("Oleg", ))
# th.start()
# th.join()

# Inheritance from Thread to make new thread(override method 'run')
#
# class PrintThread(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print("Hello,", self.name)
#
#
# p = PrintThread("Oleg")
# p.start()
# p.join()


# Using ThreadPool to make some threads
# def foo(a):
#     return a * a
#
#
# # .shutdown() in exit
# with ThreadPoolExecutor(max_workers=3) as pool:
#     results = [pool.submit(foo, i) for i in range(10)]
#
#     for future in as_completed(results):
#         print(future.result())

# Using Queue to pass data between threads
#
# def worker(q, n):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print("process data:", n, item)
#
#
# q = Queue(5)
# th1 = Thread(target=worker, args=(q, 1))
# th2 = Thread(target=worker, args=(q, 2))
# th1.start()
# th2.start()
#
# for i in range(50):
#     q.put(i)
#
# q.put(None)
# q.put(None)
# th1.join()
# th2.join()

# Synchronizing threads with context manager
#
# class Point(object):
#     def __init__(self):
#         self._mutex = threading.RLock()
#         self._x = self._y = 0
#
#     def get(self):
#         with self._mutex:
#             return (self._x, self._y)
#
#     def set(self, x, y):
#         with self._mutex:
#             self._x = x
#             self._y = y

# Synchronizing threads by hands (may have deadlock)
#
# a = threading.RLock()
# b = threading.RLock()
#
#
# def foo():
#     try:
#         a.acquire()
#         b.acquire()
#     finally:
#         a.release()
#         b.release()


# # Synchronizing threads witch conditional variables
#
# class Queue:
#     def __init__(self, size=5):
#         self._size = size
#         self._queue = []
#         self._mutex = threading.RLock()
#         self._empty = threading.Condition(self._mutex)
#         self._full = threading.Condition(self._mutex)
#
#     def put(self, val):
#         with self._mutex:
#             while len(self._queue) >= self._size:
#                 self._full.wait()
#
#             self._queue.append(val)
#             self._empty.notify()
#
#     def get(self):
#         with self._mutex:
#             while len(self._queue) == 0:
#                 self._empty.wait()
#
#             val = self._queue.pop(0)
#             self._full.notify()
#             return val

# Cpu bound program
#
def count(n):
    while n > 0:
        n -= 1


# Series rum
t0 = time.time()
count(100_000_000)
count(100_000_000)
print(time.time() - t0)

# Parallel run
t0 = time.time()
th1 = Thread(target=count, args=(100_000_000,))
th2 = Thread(target=count, args=(100_000_000,))

th1.start()
th2.start()

th1.join()
th2.join()
print(time.time() - t0)
