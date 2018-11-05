import pymysql

a = 'NA'
try:
    int(a)
except ValueError as e:
    print(e)
    print(int(1))

# conn = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='123',
#     db='psl',
#     charset='utf8'
# )

# cur = conn.cursor()
# sql = "INSERT INTO stu (id, age) VALUES (10, 'NA')"
# try:
#     cur.execute(sql)
# except Exception as e:
#     pass
