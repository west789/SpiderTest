import requests
from lxml import etree
from lxml import html
import json
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"} 
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525369469378&di=ee9b5a6205e69a993201121b4ad4b3dc&imgtype=0&src=http%3A%2F%2Fimage.cnwest.com%2Fattachement%2Fjpg%2Fsite1%2F20161021%2F14feb5e5e1471974190a08.jpg"

response = requests.get(url, headers = headers)
try:
    image1 = response.content
    print (image1)
    with open ("1.jpg", 'wb') as f:
        f.write(image1)
except Exception as e:
    print (e)
print("-------")

