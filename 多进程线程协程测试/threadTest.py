import threading
import time
from time import ctime


# start = time.time()
# def action(num):
#     print("耗时开始:%d"%num)
#     time.sleep(1)
#     print("耗时完毕%d"%num)

# if __name__ == "__main__":
#     tsk = []
    #分开写thread
    # t1 = threading.Thread(target=action, args=(1,))
    # t1.start()
    # tsk.append(t1)
    # t2 = threading.Thread(target=action, args=(2,))
    # t2.start()
    # tsk.append(t2)
    
    #for循环里的thread
    # for i in range(5):
    #     t = threading.Thread(target=action, args=(i,))
    #     t.start()
    #     tsk.append(t)
    # for tt in tsk:
    #     tt.join()

    # end = time.time()
    # print("cost time:%s"%(end-start))

#类对象写多线程
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("sleep之前%s"%i)
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i)
            print(msg)
def test():
    tsk = []
    for i in range(2):
        t = MyThread()
        t.start()
        tsk.append(t)
    
    print("join开始")
    for tt in tsk:
        tt.join()
if __name__ == '__main__':
    start = time.time()
    test()
    end = time.time()
    print("cost time:", end-start)


