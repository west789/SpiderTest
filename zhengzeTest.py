from threading import Timer
import time


# count = 0
# def loopfunc(msg,starttime):
#     global count
#     print ('启动时刻：', starttime, ' 当前时刻：', time.time(), '消息 --> %s' % (msg))
#     count += 1
#     if count < 3:
#         Timer(3, loopfunc, ('world %d' % (count), time.time())).start()

# Timer(3, loopfunc, ('world %d' % (count), time.time())).start()


def func(msg, starttime):
    print ('程序启动时刻：', starttime, '当前时刻：', time.time(), '消息内容 --> %s' % (msg))
    
# 下面的两个语句和上面的 scheduler 效果一样的
Timer(5, func, ('hello', time.time())).start()
Timer(3, func, ('world', time.time())).start()