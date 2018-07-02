import execjs
import requests
import json
#初始化环境
node=execjs.get()

#参数
method='GETDETAIL'
# method='GETCITYWEATHER'
city='北京'
typeName='DAY' #'HOUR'
startTime='2018-05-01 00:00'
endTime='2018-06-01 00:00'

#执行js
filePath='qixiang/encryption.js'
ctx=node.compile(open(filePath, encoding='utf-8').read())

#得到参数
#js='getEncryptedData("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, typeName, startTime, endTime)
js="getEncryptedData({},{},{},{},{})".format(method, city, typeName, startTime, endTime)
params=ctx.eval(js)


#获取response的txt
api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
formData={'d':params}
response=requests.post(api,  data=formData)
print(response.text)

# Decode data
decodejs = 'decodeData("{0}")'.format(response.text)
decrypted_data = ctx.eval(decodejs)
data = json.loads(decrypted_data)
print(data)