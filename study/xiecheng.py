
"""
@author: lileilei
@file: xiecheng.py 
@time: 2018/4/23 9:46 
"""
# import  asyncio,datetime
# async def display_date(num, loop):
#     end_time = loop.time() + 10.0
#     while True:
#         print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
#         if (loop.time() + 1.0) > end_time:
#             break
#         await asyncio.sleep(2)  # 等同于yield from
# if __name__=='__main__':
#     loop=asyncio.get_event_loop()
#     tasks = [display_date(1, loop), display_date(2, loop)]
#     loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
#     loop.close()
import asyncio
import requests


async def spider(loop):
    # run_in_exectuor会返回一个Future，而不是coroutine object
    future1 = loop.run_in_executor(None, requests.get, 'https://www.python.org/')
    future2 = loop.run_in_executor(None, requests.get, 'http://httpbin.org/')
    # 通过命令行可以发现上面两个网络IO在并发进行
    response1 = await future1  # 阻塞直到future1完成
    response2 = await future2  # 阻塞直到future2完成
    print(z(response1.text))
    print(len(response2.text))
    return 'done'


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(spider(loop))
    print(result)
    loop.close()