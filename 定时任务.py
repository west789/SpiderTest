import datetime
import time
from demo import demo

def loopTask():
    '''
    loop module,define current time and sleep time
    '''
    while True:
        now = datetime.datetime.now()
        today = now.date()
        sleepSeconds = get_sleepSecods(now, today)
        time.sleep(sleepSeconds)
        time.sleep(0.5)


def get_sleepSecods(now, today):
    '''
    time task: compare with the time which are defined
    '''
    timeFirst = datetime.time(18, 56, 50)
    timeSecond = datetime.time(15, 40, 0)
    timeThird = datetime.time(19, 30, 0)
    dateTimeFirst = datetime.datetime.combine(today, timeFirst)
    dateTimeSecond = datetime.datetime.combine(today, timeSecond)
    dateTimeThird = datetime.datetime.combine(today, timeThird)
    tomorrow = dateTimeFirst + datetime.timedelta(days=1)
    print(dateTimeFirst+datetime.timedelta(seconds=1))
    if dateTimeFirst < now < dateTimeFirst+datetime.timedelta(seconds=1):
        doTask()
        from insert_report.autoReport import generateReport
        generateReport()
        print((dateTimeSecond - datetime.datetime.now()).total_seconds()-10)
        return (dateTimeSecond - datetime.datetime.now()).total_seconds()-10
    if dateTimeSecond < now < dateTimeSecond+datetime.timedelta(seconds=1):
        doTask()
        # print((dateTimeThird - datetime.datetime.now()).total_seconds()-10)
        return (dateTimeThird - datetime.datetime.now()).total_seconds()-10
    if dateTimeThird < now < dateTimeThird+datetime.timedelta(seconds=1):
        doTask()
        # print((tomorrow - datetime.datetime.now()).total_seconds()-10)
        return (tomorrow - datetime.datetime.now()).total_seconds()-10
    if now > dateTimeThird:
        # print((tomorrow - datetime.datetime.now()).total_seconds() - 10)
        return (tomorrow - datetime.datetime.now()).total_seconds() - 10
    return 0

def doTask():
    print("this is task")
    # demo()

def doLoop():
    loopTask()

# if __name__ == "__main__":
#     print("-----------")
#     loopTask()