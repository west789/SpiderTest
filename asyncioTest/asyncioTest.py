import threading
import asyncio

async def hello():
    print("Hello world!")
    async with aiohttp.get('https://github.com') as r:
        await r.text()
    print("Hello again!")

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#tasks = [getPage(url, ret_list) for url in articles_url]