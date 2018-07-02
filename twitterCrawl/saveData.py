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
    def insert_userInfo(self, itemDict):
        sql = """
            INSERT INTO account (accountName, twitterId, screenName, location, description,
                                url, statusesCount, friendsCount, followersCount, favoritesCount,
                                accountTime, profileImage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(sql, (itemDict["accountName"], itemDict["twitterId"],
                                itemDict["screenName"], itemDict["location"],
                                itemDict["description"], itemDict["url"],
                                itemDict["statusesCount"], itemDict["friendsCount"],
                                itemDict["followersCount"], itemDict["favoritesCount"],
                                itemDict["accountTime"], itemDict["profileImage"]))
            self.conn.commit()
            print("执行sql语句成功")
        except Exception as e:
            self.conn.rollback()
            print(e)
            print("执行sql语句失败")
            return "error"
    def insert_tweetInfo(self, itemDict):
        sql = """
            INSERT INTO tweets (accountId, tweetsText, tweetsUrl, videoUrl, imageUrl, retweetCount,
                                tweetFavCount, tweetTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(sql, (itemDict["accountId"], itemDict["tweetsText"],
                                    itemDict["tweetsUrl"], itemDict["videoUrl"],
                                    itemDict["imageUrl"], itemDict["retweetCount"],
                                    itemDict["favoriteCount"], itemDict["tweetTime"],))
            self.conn.commit()
            print("执行sql语句成功")
        except Exception as e:
            self.conn.rollback()
            print(e)
            print("执行sql语句失败")
            return "error"
    def update_userInfo(self, itemDict, twitterId):
        sql = """
            update account set accountName=%s, screenName=%s,
                               twitterId=%s, location=%s,
                               description=%s, url=%s,
                               statusesCount=%s, friendsCount=%s,
                               followersCount=%s, favoritesCount=%s,
                               accountTime=%s, profileImage=%s where twitterId=%s
        """
        try:
            self.cursor.execute(sql, (itemDict["accountName"], itemDict["screenName"],
                                itemDict["twitterId"], itemDict["location"],
                                itemDict["description"], itemDict["url"],
                                itemDict["statusesCount"], itemDict["friendsCount"],
                                itemDict["followersCount"], itemDict["favoritesCount"],
                                itemDict["accountTime"], itemDict["profileImage"],twitterId))
            self.conn.commit()
            print("执行sql语句成功")
        except Exception as e:
            self.conn.rollback()
            print(e)
            print("执行sql语句失败")
            return "error"
    #处理idList数据
    def do(self, idList):
        twitterIdlist = []
        for item in idList:
            twitterIdlist.append(item["twitterId"])
        return twitterIdlist
    #获取twitterId的列表
    def get_twitterIdList(self):
        sql = "select twitterId from account"
        # cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            self.cursor.execute(sql)
            idTuple = self.cursor.fetchall()
            idList = [item[0] for item in idTuple]
            return idList
        except Exception as e:
            self.conn.rollback()
            print(e)
            print("执行sql语句失败")
            return "error"
    
    #获取accountId
    def get_accountId(self, twitterId):
        sql = "select accountId from account where twitterId =%s"%twitterId
        try:
            self.cursor.execute(sql)
            accountId = self.cursor.fetchone()
            return accountId
        except Exception as e:
            self.conn.rollback()
            print(e)
            print("执行sql语句失败")
            return "error"


        

