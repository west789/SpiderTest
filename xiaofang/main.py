#导入相关包
import requests
from lxml import etree

import json

#基本分为三个步骤
#获取数据 处理数据 存储数据


headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Mobile Safari/537.36"} 
url = "http://1804280907.pool2-msite.make.yun300.cn/product/6.html"  #还是以网址为请求对象，如果是其他可以加对应网址，写for循环
                                                                     #如果网址有规律，可以找出规律去请求网址

result = {}
response = requests.get(url, headers=headers) #发送request请求
html = etree.HTML(response.text)   #获取网页内容
canshu = html.xpath("//div[@class='e_box e_box-000 d_proDecSwiBox p_proDecSwiBox']/div[2]//text()") #三个字段均是用xpath去获取内容
canshu = ''.join(canshu).strip().replace('\n', '').replace('\t', '')                                #获取字段后有数据清洗的过程
shuoming = html.xpath("//div[@class='e_box e_box-000 d_proDecSwiBox p_proDecSwiBox']/div[3]//text()")
shuoming = ''.join(shuoming).strip().replace('\n', '').replace('\t', '')
baoyang = html.xpath("//div[@class='e_box e_box-000 d_proDecSwiBox p_proDecSwiBox']/div[3]//text()")
baoyang = ''.join(baoyang).strip().replace('\n', '').replace('\t', '')
result["canshu"] = canshu
result["shuoming"] = shuoming
result["baoyang"] = baoyang
res = json.dumps(result, ensure_ascii=False)
with open('xiaofang/xiaofang.txt', 'w', encoding="utf-8") as f:   #存库，根据实际情况存储数据
    f.write(res)
    print(res)
                                                                                                                                                            