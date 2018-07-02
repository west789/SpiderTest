import requests
from lxml import etree
from lxml import html
import json
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Mobile Safari/537.36",
            "referer":"https://www.douyin.com/share/user/57720812347"} 
url = "https://www.douyin.com/aweme/v1/aweme/post/?user_id=57720812347&count=21&max_cursor=0&aid=1128&_signature=DEnrbhATV02mZqvuX0F1gQxJ63"

response = requests.get(url, headers = headers)
content=response.content

try:
    with open('shipin/douyin1.mp4', 'wb')  as f:
        f.write(content)
except Exception as e:
    print (e)

print (content)

