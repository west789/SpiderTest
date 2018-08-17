import imaplib
import email
from email import utils
from fetcher.email import ImapEmailFetcher, AttHandlers
import os
import re
connection = imaplib.IMAP4_SSL('10.209.152.54', 993)
# 使用imap，比如要访问163邮箱，地址是imap.163.com，而不是mail.163.com

username = 'bj/db'
password = 'XR%@**0ocIYrb1SG'

# 登陆
try:
    connection.login(username, password)
    res, data = connection.select('INBOX')
    res1, msg_ids = connection.search(None, 'ALL')
    res2, msg_ids2 = connection.uid('search', None, 'ALL')
    # res2m, msgnums = connection.uid('search', None, "UnSeen")
    # msgid = msgnums[0].split(b' ')
    # ret, data = connection.uid('fetch', b'6809', '(RFC822)')
    (result, messages) = connection.uid('search', None, "UnSeen")
    ret3, msg_data = connection.fetch('6823', '(RFC822)') #6811
    ret4, data4 = connection.uid('fetch', b'6866', '(RFC822)')
    response, dataUn = connection.store(
                b'6852', '+FLAGS', '\\UnSeen')
    msg = email.message_from_bytes(data4[0][1])
    response6, data6 = connection.store(
        b'6830', '+FLAGS', '\\Seen')
    # for messageTest in messages[0].split(b' '):
    #     ret5, data5 = connection.uid('fetch', messageTest, '(RFC822)')
    #     response, data = connection.store(
    #         messageTest, '+FLAGS', '\\Seen')
    #     msg = email.message_from_bytes(data5[0][1])
    sender = utils.parseaddr(msg['FROM'])[1]
    # for item in msg.walk():
    #     if item.get_filename():
    #         print(item.get_filename())
    #         splitFileName = os.path.splitext(item.get_filename())
    #         if splitFileName[1].lower() in ['.xls', '.xlsx', '.csv']:
    #             print(splitFileName[1].lower())
    #             reFileName = re.sub(r'[\/:*?"<>|]', r'', item.get_filename())
                # print(item.get_payload(decode=True).decode('utf-8'))
        # if item.get_content_maintype():
        #     print(item.get_content_maintype())
            # if not item.is_multipart():
                # print(item.get_payload(decode=True).decode('utf-8'))


    for handler in AttHandlers:
        h = handler()
        if sender in h.related_vendor_emails():
            for record in h.handle(msg):
                print(record)
            break
    print(res, data)
    print(data[0])  # 邮件数
except Exception as err:
    print('登陆失败: :', err)  # 输出登陆失败的原因

# 输出日志
connection.print_log()

# 断开连接
# connection.close()
connection.logout()
