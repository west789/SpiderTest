from threading import Thread,Lock
import time


g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()

    print("---test2---g_num=%d"%g_num)

mutex = Lock()



tsk = []
p1 = Thread(target=test1)
p1.start()
tsk.append(p1)

p2 = Thread(target=test2)
p2.start()
tsk.append(p2)
for tt in tsk:
    tt.join()
# time.sleep(7) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？
print("---g_num=%d---"%g_num)