import requests
import time
import multiprocessing
from multiprocessing import Pool

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"} 
def request(num):
    url = "http://img2.3lian.com/2014cf/f2/126/d/74.jpg"
    print("waiting for:", url)
    response = requests.get(url, headers=headers)
    result = response.text
    print("获取完成")

if __name__ == "__main__":
    start = time.time()
    # request(1)
    cpu_count = multiprocessing.cpu_count()
    pool = Pool(8)
    # pool.map(request, range(1))
    for i in range(4):
        pool.apply_async(request, (1,))
    pool.close()
    pool.join()
    end = time.time()
    print("cost time:", end-start)