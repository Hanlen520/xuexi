""" 
@author: lileilei
@file: kuaishou.py 
@time: 2018/6/21 13:45 
"""
import requests,json
url='http://124.243.249.4/rest/n/feed/hot?appver=5.7.5.508&did=EB3C5966-C50E-432D-801E-D7EB42964654&c=a&ver=5.7&sys=ios9.3.5&mod=iPhone7%2C2&net=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8_5'
headers={
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': '124.243.205.129',
    'Accept-Language': 'zh-Hans-CN;q=1'
}
data={
    'client_key':'56c3713c',
    'coldStart':'true',
    'count':'20',
    'country_code':'cn',
    'id':'5',
    'language':'zh-Hans-CN;q=1',
    'pv':'false',
    'refreshTimes':'0',
    'sig': '4d0f20c2d2441031022b4dd2bfa4949b',
    'source':'1',
    'type':'7'
}
jso=requests.post(url,data=(data),headers=headers)
list=jso.json()['feeds']
for i in list:
    print('描述：%s'%i['caption'])
    print('视频连接：%s'%i['main_mv_urls'][0]['url'])
    print('作者：%s'%i['user_name'])
    print('用户id：%s'%i['user_id'])