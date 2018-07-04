import threading
import asyncio
import aiohttp
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
async def showResult():
    print("showResult执行")
    await asyncio.sleep(1)
    print("showResult完毕")
    return "hello 结果"
async def hello():
    print("Hello world!")
    # async with aiohttp.get('https://github.com') as r:
    #     await r.text()
    #  asyncio.sleep(1)
    showResult1 = await showResult()
    
    print("Hello again!")
    return showResult1
async def getGitHub():
    print("Hello GitHub")
    # async with aiohttp.request("GET", "https://video.twimg.com/tweet_video/Dg74JWkWAAALNE1.mp4")as r:
    response = requests.get("https://video.twimg.com/tweet_video/Dg74JWkWAAALNE1.mp4", headers=headers)
    text = response.content
    print("getGitHub执行完毕", text)
    return "github 结果"
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(getGitHub()), asyncio.ensure_future(getGitHub())]

loop.run_until_complete(asyncio.wait(tasks))
for task1 in tasks:
    print(task1.result())
loop.close()

#tasks = [getPage(url, ret_list) for url in articles_url]