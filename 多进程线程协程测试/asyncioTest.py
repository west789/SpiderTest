import asyncio
import aiohttp
import time
# from aiomultiprocess import Pool
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"} 
#协程测试
start = time.time()
async def get(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url, headers=headers) as response:
            result = await response.read()
            return result
async def request():
    url = "http://img2.3lian.com/2014cf/f2/126/d/74.jpg"
    print("waiting for:", url)
    result = await get(url)
    print("Get response from:", url, "Result:")

tasks = [asyncio.ensure_future(request()) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("cost time:", end-start)
 
#报错 "cannot find context for 'fork'"错误
# start = time.time()
# async def get(url):
#     session = aiohttp.ClientSession()
#     # response = await session.get(url)
#     async with session.get(url) as r:
#         await r.text() 
#         print(r.status)
#         print(r.text())
#     return r.text()
# async def request():
#     url = "http://example.com/"
#     urls = [url for _ in range(3)]
#     async with Pool() as pool:
#         result = await pool.map(request, urls)
#         return result
# task = asyncio.ensure_future(request())
# loop = asyncio.get_event_loop()
# end = time.time()
# print("cost time:", end-start)

#测试最简单coroutine
# loop = asyncio.get_event_loop() 
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

#tasks = [getPage(url, ret_list) for url in articles_url]