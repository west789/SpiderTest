import time
import datetime

def runTask():
    print(f"执行内容{datetime.datetime.now()}")

def timeFun(sched_timedo):
    flag = 0
    while True:
        now = datetime.datetime.now()
        if sched_timedo < now < sched_timedo+datetime.timedelta(seconds=1):
            flag = 1
            time.sleep(1)
            runTask()
        else:
            if flag == 1:
                sched_timedo = sched_timedo+datetime.timedelta(seconds=10)
                print(f"sched_timedo change:{sched_timedo}")
                flag = 0

if __name__ == "__main__":
    sched_timedo = datetime.datetime(2018, 7, 17, 14, 39, 10)
    print(f"执行Timer{sched_timedo}")
    timeFun(sched_timedo)