from aip import AipOcr
import os
import requests

APP_ID = '11210992'
API_KEY = 'BAIsF9A3rKciMRuc7QnpaBy0'
SECRET_KEY = 'rjOpUYc9aYFPVeqD83lnuDkziXg2aT5r '
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#本地图片代码

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def getFileName(image):
    for _,_,file in  os.walk(image):
        return file

imageList = getFileName("./image")
for fileName in imageList:
    image = get_file_content(os.path.join('./image', fileName))
    data = client.basicGeneral(image)
    for item in data['words_result']:
        itemWord = item['words']
        print (itemWord)

#网络url测试
# urlList = [
#         'http://www.1juzi.com/article/pic/2015-10/201510210224815363.jpg'
# ]
# for url in urlList:
#     data = client.basicGeneralUrl(url)
#     itemList = []
#     for item in data['words_result']:
#         itemList.append(item["words"])
#     print (''.join(itemList))

print("----------")

#验证码识别
# itemList = []
# response = requests.get('https://www.douban.com/misc/captcha?id=WkuB2dTueCsUyTd5RjlAGZQ8:en&size=s')
# with open('yanzhengma.jpg', 'wb') as f:
#     f.write(response.content)
# data = client.basicGeneral(yanzhengma.jpg)
# for item in data['words_result']:
#     itemList.append(item["words"])
#     print (''.join(itemList))