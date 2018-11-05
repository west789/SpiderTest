from fetcher import records_from_email, records_from_web
from factory import RecordFileFactory
from time import sleep
import threading
#import sys
#sys.path.append('..')
#from wafer_STATS_tool.demo import demo
#from wafer_STATS_tool.avl_mail import sendmail2eng


DEFAULT_DOWNLOAD_FOLDER = './attachments'

def email_routine():
    while True:
        try:
            factory = RecordFileFactory(default_folder=DEFAULT_DOWNLOAD_FOLDER)
            for record in records_from_email('INBOX'):
                factory.feed(record)       
            print('We got {} records'.format(len(factory.records)))
            result = factory.to_upstream()
            print('{} record(s) have been successfully handled'.format(result))
        except Exception as e:
            print('*** EMAIL TASK ERROR ***  {}'.format(e))

        sleep(1200)

def spider_routine():
    while True:
        try:
            factory = RecordFileFactory(default_folder=DEFAULT_DOWNLOAD_FOLDER)
            for record in records_from_web():
                factory.feed(record)       
            print('We got {} records'.format(len(factory.records)))
            result = factory.to_upstream()
            print('{} record(s) have been successfully handled'.format(result))
        except Exception as e:
            print('*** EMAIL TASK ERROR ***  {}'.format(e))
        #try:
        #    demo()
        #except Exception as err:
        #    sendmail2eng('*** wafer demo error *** {}'.format(err))

        sleep(1200)

def main():
    task_email = threading.Thread(target=email_routine)
    task_spider = threading.Thread(target=spider_routine)

    threads = [task_email, task_spider]
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

    print("Vendor DB App-Main done.")

if __name__ == '__main__':
    main()
