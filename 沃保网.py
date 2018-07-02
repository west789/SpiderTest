import requests,json
from lxml import etree
#from pymongo import MongoClient
from  pymysql import  *
# from save_to_mysql.demo import save_mysql
import os
#import redis
import hashlib
#from retrying import retry


class WoBao(object):
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                     "'Chrome/55.0.2883.87 Safari/537.36"}

        self.data = {"Area1List1":"1","Area2List2":"39","Search.KeyWord":"","Search.AreaID1":"-100","Search.AreaID2":"0",
                "Search.AreaID3":"0","Search.PyCode":"0","Search.CompanySymbol":"pinganbaoxian","Search.Year":"0","Search.OrderTp":"1",
                "Search.SearchTp":"1","Search.UserLevel":"8","Search.SortRule":"","Search.PageIndex":"1","Search.PageSize":"10",
                "Search.LastHash":"0","Search.TotalPages":"1","Search.TotalCount":"0","sex":"1",
                "X-Requested-With":"XMLHttpRequest"}

        with open("沃保网1.csv","a",encoding="GBK") as f:
            f.write("姓名,公司,城市,照片,等级,数量,微信二维码,网站地址" + "\n")

        self.r = redis.Redis("127.0.0.1", 6379)
        self.item_key = "item_dumpkey"
        client = MongoClient("127.0.0.1", 27017)
        self.collection = client["book"]["wobao"]

    @retry(stop_max_attempt_number=3)
    def parse_url_get(self,url):
        try:
            response = requests.get(url, headers=self.headers,timeout=5).content.decode('utf8')
        except:
            return None
        return response

    @retry(stop_max_attempt_number=3)
    def parse_url(self,url,data):

        response = requests.post(url,headers=self.headers,data=data).content.decode('utf8')
        # print(response)
        return response

    # def save_mysql(self,con_list):
    #     # print(111,con_list)
    #     conn = connect(host="localhost",
    #                    user="root",
    #                    password="mysql",
    #                    database="wobao",
    #                    port=3306,
    #                    charset='utf8')
    #     for dict in con_list:
    #         cur = conn.cursor()  # 数据库链接对象
    #         sql = "insert IGNORE into wobao SET"
    #         for key, value in dict.items():
    #             res = "`{}` = '{}'".format(key, value)
    #             sql = sql + ' ' + res + ','
    #         sql = sql[:-1]
    #         sql = sql + ';'
    #         print(sql)
    #         cur.execute(sql)
    #         conn.commit()
    #         cur.close()
    #     conn.close()

    def get_content_list(self,str_con,data):
        html = etree.HTML(str_con)
        # print(html)
        li_list = html.xpath("//ul[@class='safe_con div1']/li")
        # print(li_list)
        con_list = []
        for li in li_list:

            # print(i,li)
            dict = {}
            # 获取名字
            dict["name"] = li.xpath("./div[@class='middle']//span[@class='name']/a/text()")[0]


            # 获取公司地址和公司名称，span不能写span[3],要在前面加限定的p标签
            #  ['廊坊廊坊\xa0 平安保险'] 拆分，先join转换成字符串，在split转换成列表，在取值
            dict["ltd"] = li.xpath ( "./div[@class='middle']//p/span/text()")
            dict["ltd"]=" ".join(dict["ltd"])
            dict["ltd"]=dict["ltd"].split("\xa0 ")
            dict["city"] = dict["ltd"][0]
            dict["ltd"]=dict["ltd"][1]

            dict["photo"] = li.xpath("./div[@class='photo']/a/img/@src")[0]

            # 微信二维码
            dict["wechat"] = li.xpath("./div[@class='site']/div[@class='site-btn']/span[text()='微信']/../div/img/@src")
            dict["wechat"] = dict["wechat"][0] if len(dict["wechat"])>0 else None

            # 获取个人站
            # dict["website"] = li.xpath ( "./div[@class='site']/div[@class='site-btn']/span[text()='手机站']/following-sibling::div[1]/img/@src" )[0]
            dict["website"] = li.xpath ("./div[@class='site']/div[@class='site-btn']/span[text()='手机站']/../div/img/@src" )[0]
            dict["website"] = "http://member.vobao.com" + dict["website"]

            # 获取等级
            if data["Search.UserLevel"] == "8":
                dict["level"] = "皇冠"
            else:
                dict["level"] = "钻石"

            # 获取皇冠钻石个数
            ol_li_list = li.xpath ( "./div[@class='middle']//div[@class='gold-rank']/ol/li" )
            num = len(ol_li_list)
            dict["num"] = num


            # 获取详情页url,提取展业证号
            dict["detail_url"] = li.xpath ( "./div[@class='middle']/div[@class='infor']/span[@class='name']/a/@href")[0]
            # print(dict["detail_url"])
            dict["id_num"] = self.get_id_num(dict["detail_url"])
            print(dict)

            con_list.append(dict)



        # <input type="hidden" id="Search_PageIndex" name="Search.PageIndex" value="2" />
        # <input type="hidden" name="Search.TotalPages" value="3" />
        page_count = html.xpath("//input[@name='Search.TotalPages']/@value")[0]
        current_page = html.xpath("//input[@name='Search.PageIndex'][1]/@value")[0]
        total_count = html.xpath("//input[@name='Search.TotalCount']/@value")[0]
        print(page_count,current_page,total_count)
        if int(current_page)<int(page_count):
            print(33333)
            next_url = "http://member.vobao.com/Member/SellerList?Length=6"
            self.data["Search.PageIndex"] = int(current_page)+1
            self.data["Search.TotalPages"] = page_count
            self.data["Search.TotalCount"] = total_count
        else:
            next_url=None
            self.data["Search.PageIndex"] = "1"
            self.data["Search.TotalPages"] = "1"
            self.data["Search.TotalCount"] = "0"


        print(con_list)
        print(self.data)
        return con_list,next_url,self.data

    def get_id_num(self,detail_url):
        # print(333)
        if detail_url is not None:
            # print(detail_url)
            detail_html_str = self.parse_url_get(detail_url)
            if detail_html_str is not None:
                # print(detail_html_str)
                detail_html = etree.HTML(detail_html_str)

                id_text_hg = detail_html.xpath("//p[contains(text(),'资格证号')]/span/text()")
                id_text_zs = detail_html.xpath("//div[@class='num']/span[2]/text()")

                if len(id_text_hg) > 0:
                    id_num = id_text_hg[0]
                elif len(id_text_zs) >0:
                    id_text = id_text_zs[0]
                    id_num = id_text.split("：")[1]
                else:
                    id_num=None

                return id_num
        else:
            return None

    def item_dupfilter(self,dict):
        f = hashlib.sha1()
        f.update(dict["name"].encode())

        # f.update(dict["author"].encode())
        fingerprint = f.hexdigest()
        print(fingerprint)
        res = self.r.sadd (self.item_key,fingerprint)
        return res

    def save_mysql(self,con_list):
        conn = connect(host="localhost",
                       user="root",
                       password="mysql",
                       database="wobao",
                       port=3306,
                       charset='utf8')
        for dict in con_list:

            cur = conn.cursor()  # 数据库链接对象
            res = self.item_dupfilter(dict)
            print(res)
            if res==1:
                if dict["ltd"]=="中国人寿":
                    print("存入人寿")
                    sql = "insert IGNORE into zgrs SET"
                else:
                    print('存入平安')
                    sql = "insert IGNORE into pabx SET"

                for key, value in dict.items():
                    res = "`{}` = '{}'".format(key, value)
                    sql = sql + ' ' + res + ','
                sql = sql[:-1]
                sql = sql + ';'

            else:
                if dict["ltd"] == "中国人寿":
                    print('更新人寿')
                    sql = "update zgrs SET"
                else:
                    print('更新平安')
                    sql = "update pabx SET"

                for key, value in dict.items():
                    res = "`{}` = '{}'".format(key, value)
                    sql = sql + ' ' + res + ','
                sql = sql[:-1]
                sql = sql + " where name='{}'".format(dict["name"])
                sql = sql + ';'
            print(sql)
            cur.execute(sql)
            conn.commit()
            cur.close()
        conn.close()

    def save_mongodb(self,con_list):

        for dict in con_list:
            # 保存mongodb
            client = MongoClient(host="127.0.0.1", port=27017)
            self.collection = client["book"]["wobao"]
            res = self.item_dupfilter(dict)
            print(res)
            if res==1:
                self.collection.insert_one(dict)
            else:
                self.collection.update({"name":dict["name"],"city":dict["city"]},{"$set":dict})


            # 保存csv
            with open("沃保网1.csv","a",encoding="GBK") as f:
                temp_list = [dict["name"],dict["ltd"],dict["city"],dict["photo"],dict["level"],dict["num"],dict["wechat"],dict["website"]]
                tmp_str = ",".join([str(i) for i in temp_list]) + "\n"
                f.write(tmp_str)

            # 保存二维码
            if dict["wechat"] is not None:
                path = "{}_{}_{}_{}".format(dict["ltd"],dict["level"],dict["name"],dict["city"])
                path = os.path.join("./二维码/",path)
                # print(path)
                with open(path,"wb") as f:
                    content = requests.get(dict["wechat"]).content
                    f.write(content)

    def run(self):
        ltdList = ['pinganbaoxian','zhongguorenshou']
        levelList = ["8","4"]

        for ltd in ltdList:
            self.data["Search.CompanySymbol"] = ltd
            for level in levelList:
                self.data["Search.UserLevel"] = level
                data = self.data
                next_url = "http://member.vobao.com/Member/SellerList?Length=6"
                while next_url is not None:
                    # print(3444)
                    str_con = self.parse_url(next_url,data)
                    con_list,next_url,data = self.get_content_list(str_con,data)
                    self.save_mysql(con_list)  # 导入包save_to_mysql
                    # self.save_mongodb(con_list)



if __name__ == '__main__':
    wobao = WoBao()
    print(333)
    wobao.run()

