import pymysql

class MysqlDB(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect('localhost', 'root', '123', 'twitter', charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('连接数据库失败：%s' % str(e))

    def close(self):
        self.cursor.close()
        self.conn.close()


class TwitterPip (MysqlDB):
    def process_item(self, item):
        sql = """
            INSERT INTO test (message) VALUES ("%s")
        """
        try:
            self.cursor.execute(sql, item)
            self.conn.commit()
            print("执行sql语句成功")
            return item
        except Exception as e:
            self.conn.rollback()
            print(e)
            print("执行sql语句失败")
            return "error"

        

