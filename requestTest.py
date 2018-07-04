import requests
from lxml import etree
from lxml import html
import json

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"} 
url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token="

formData = {
    "params":"8xLRFsy+eDV15BIpEUvHxMFQo20CJPKZkAiX3NbVaereyX7ZR/Su3PE/cSk1rDDdXU52KunYI3MS/3t2EMhTrsbCLcNzJenQ+BfJEDzPVxFmDALo1BtTNb8SgJz72GSg7icQAFxPA/qosT+D5wdx1KJiD6yZtFrrfgmdLLlIPQY9Q4NZmv8fybNrMRZAI+oz",
    "encSecKey":"c08da5cce8c7dd739aab89f98b7a5efef33794b9468e0c9f1cfcaae9ce447f1bc01c0f6e63ecd15c99f9d48e4485c7a80b9d62c833052356b421fa02669b64e256da301a647198643d59cb9fc378b30e03dbfaaab77716d52fc408081a1f53164e34aa0892cbb9e31922e8c20db823cc779a8e8dc1966c89690482cc3403d50f"
}
response = requests.post(url, headers = headers, data=formData)
#response.encoding = "utf-8"
#tree = html.fromstring(response.text)
data = json.loads(response)
try:
    print (response.text)

    #link = tree.xpath("//div[@class='col-xs-6 col-sm-3 col-md-2'][1]/div[@class='rounded-tile program-tile-small']/p[@class='program']/a/@href")
except Exception as e:
    print (e)

#result = tree.xpath("//p[@class='program']/a/@href")
# with open("link.txt", 'w') as f:
#     f.writelines(' '.join(res))
