# 一. 多进程
# 1. fork 函数
# 调用一次，返回两次，因为把当前进程复制了一份，然后，分别在父进程和子进程中返回

# import os
# print('process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just create a child process %s' % (os.getpid(), pid))

# multiprocessing 跨平台

# from multiprocessing import Process
# import os

# def run_proc(name):
#     print('run child process %s (%s)...' % (name, os.getpid()))

# if __name__ == '__main__':
#     print('parent process %s ' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('Child process end')
# Pool 大量子线程
# 采用线程池方法
'''  
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (name, (end - start)))

# if __name__ == '__main__':
#     print('Parent process %s' % os.getpid())
#     p = Pool(20)
#     for i in range(21):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done...')

# 子进程 subprocess 启动，控制输入输出
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
# 和命令行直接输入情况一样

# 子进程输入 communicate()
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# 进程之间的通信
# multiprocessing 中的Queue Pipes
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write: %s ' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
    
# if __name__ == '__main__':
#     # 父进程创建queue，传给子进程
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
'''
'''
 小结
在Unix/Linux下，可以使用fork()调用实现多进程。
要实现跨平台的多进程，可以使用multiprocessing模块。
进程间通信是通过Queue、Pipes等实现的。
'''
# 二. 多线程.
# 多任务可以多进程， 也可以一个进程内的多线程
# 两个模块 _thread低级模块 threading高级模块
# 绝大多数，使用高级 threading 
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
'''
import threading, time
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is end' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name = 'LoopThread')
t.start()
t.join()
print('thread %s is ended.' % threading.current_thread().name)
'''
# 线程锁，线程共享所有变量，如果多个线程同时修改同个变脸，会乱
# Lock
import threading, time

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n 
    balance = balance - n

def run_thread_lock(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

def run_thread(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target=run_thread_lock, args=(5,))
t2 = threading.Thread(target=run_thread_lock, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print('balance->>>>>>',balance) 
# banlance值会乱，所以要锁上
# 1. lock.acquire()
# 2. try 
# 3. release

# 多核cpu
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

'''
小结
多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
'''

# 三. ThreadLocal
# 痛点 每个线程下的局部变量传递问题，全局变量的加锁问题
# 如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？
# global_dict = {}

# class Student(object):
#     def __init__(self, name):
#         self.name = name

# def std_thread(name):
#     std = Student()
#     global_dict[threading.current_thread()] = std

# def do_task_1():
#     std = global_dict[threading.current_thread()]    

# def do_task_2():
#     std = global_dict[threading.current_thread()]

local_school = threading.local()
def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
def process_thread(name):
    local_school.student = name
    process_student()

t3 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t4 = threading.Thread(target=process_thread, args=('Peter',), name='Thread-B')
t3.start()
t4.start()
t3.join()
t4.join()
# 理论可行，就是太丑
# 使用ThreadLocal吧

# 四. 进程vs线程
'''
首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。

如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。

如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

计算密集型 vs. IO密集型


'''

# 五. 分布式进程
