#自写的一个小查询
from bs4 import BeautifulSoup
import urllib.request
import gzip
import json
import re
import random
import zlib
def Get_weather(city):
    url = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + urllib.parse.quote(city)
    weather = urllib.request.urlopen(url).read()
    weather_data = gzip.decompress(weather).decode('utf-8')
    soup = BeautifulSoup(weather_data)
    return soup
def Show_weather(city):
    soup = Get_weather(city)
    print('查询的城市：', soup.city.text)
    print('更新时间：', soup.updatetime.text)
    print('湿度：', soup.shidu.text)
    print('风力：', soup.fengli.text)
    print('日出时间：', soup.sunrise_1.text)
    print('日落时间', soup.sunset_1.text)
    wheater = soup.findAll('weather')
    print('日期：', wheater[0].date.text)
    print('风向：', wheater[0].fengxiang.text)
    print('风级：', wheater[0].fengli.text)
    print('高温：', wheater[0].high.text)
    print('低温：', wheater[0].low.text)
    print('天气：', wheater[0].type.text)
def show_zhishu(city):
    soup = Get_weather(city)
    try:
        zhishus = soup.findAll('zhishu')
        print('晨练指数：', zhishus[0].value.text)
        print('晨练建议：', zhishus[0].detail.text)
        print('舒适度：', zhishus[1].value.text)
        print('舒适建议：', zhishus[1].detail.text)
        print('穿衣指数：', zhishus[2].value.text)
        print('穿衣建议：', zhishus[2].detail.text)
        print('感冒指数：', zhishus[3].value.text)
        print('感冒建议：', zhishus[3].detail.text)
        print('晾晒指数：', zhishus[4].value.text)
        print('晾晒建议：', zhishus[4].detail.text)
        print('旅游指数：', zhishus[5].value.text)
        print('旅游建议：', zhishus[5].detail.text)
        print('紫外线指数：', zhishus[6].value.text)
        print('紫外线建议：', zhishus[6].detail.text)
        print('洗车指数：', zhishus[7].value.text)
        print('洗车建议：', zhishus[7].detail.text)
        print('运动指数：', zhishus[8].value.text)
        print('运动建议：', zhishus[8].detail.text)
        print('约会指数：', zhishus[9].value.text)
        print('约会建议：', zhishus[9].detail.text)
        print('雨伞指数：', zhishus[10].value.text)
        print('雨伞建议：', zhishus[10].detail.text)
    except:
        print('没有查询到你要的指数')
def get_will(city):
    soup = Get_weather(city)
    try:
        wheater = soup.findAll('weather')
        print('-----------未来四天天气---------')
        for i in range(1, 5):
            print('日期：', wheater[i].date.text)
            print('风向：', wheater[i].fengxiang.text)
            print('风级：', wheater[i].fengli.text)
            print('高温：', wheater[i].high.text)
            print('低温：', wheater[i].low.text)
            print('天气：', wheater[i].type.text)
    except:
        print('没有查询到未来几天的天气')
#-----------------------------------------------今日新闻
def Get_xinwen():
    url='http://toutiao.com/api/article/recent/?source=2&category=__all__&as=A1E5D7FB652C648&cp=57B5DC76D4080E1&_=1471529365354'
    headers={
            "Cookie":'uuid="w:47691d23c31440c4bd53a85ac5414c98"; tt_webid=25850524556; csrftoken=2fe9206db804195192595b66d4e5ce93; _ga=GA1.2.417946548.1471524630; CNZZDATA1258609184=126876833-1467773945-null%7C1467773945; utm_source=toutiao; __tasessionId=lh5v3uyl51471527331261',
            "Host":"toutiao.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        }
    response=urllib.request.Request(url,headers=headers)
    html=urllib.request.urlopen(response).read().decode('gbk')
    be=json.loads(html)
    me=be['data']
    for title in me:
        if len(title['abstract']) !=0:
            print('------------今日头条最新的新闻：-------')
            print("标题：%s"%title['title'])
            print('内容：%s'%title['abstract'])
            print('新闻连接：%s'%title['display_url'])
            print('更新时间:%s'%title['datetime'])
#——————————————————————来点段子
def Get_duanzi():
    url = 'http://toutiao.com/api/article/recent/?source=2&category=essay_joke&as=A1F5278B4978A6A&cp=57B9B8EA565A8E1&_=1471777386510'
    headers = {
        "Cookie": 'uuid="w:47691d23c31440c4bd53a85ac5414c98"; tt_webid=25850524556; csrftoken=2fe9206db804195192595b66d4e5ce93; CNZZDATA1258609184=126876833-1467773945-null%7C1467773945; utm_source=toutiao; _ga=GA1.2.417946548.1471524630; __tasessionId=r5qzmlkxx1471777347242; CNZZDATA1259612802=2124063489-1471767844-%7C1471772263',
        "Host": "toutiao.com",
        "Referer": "http://toutiao.com/essay_joke/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    response = urllib.request.Request(url, headers=headers)
    htm = urllib.request.urlopen(response).read().decode('utf-8')
    html = json.loads(htm)
    try:
        lo = html['data']
        for item in lo:
            print('------------段子新鲜出炉--------------------')
            print('上传者：%s' % item['group']['user']['name'])
            print('内容：%s' % item['group']['content'])
            print("点赞：%s" % item['group']['digg_count'])
            print('分享：%s次' % item['group']['share_count'])
    except:
        pass
#-----------------------------查询火车票
def get_huochepiao(url1):
    headers={'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Connection':'keep-alive',
	'Cookie':'QN99=3733; QN1=eIQiP1dEAASbOq51LyeNAg==; QunarGlobal=192.168.31.105_-4c70ffc_154e15d8dc8_2de|1464074245311; ag_fid=AsWRT9vZYYLJ23qF; __ag_cm_=1464074247005; QN269=906FD473217F11E6B393C4346BAC1530; PHPSESSID=epq85mhbfeg12b3t6q8rkic702; QN25=5cfd26dc-8670-44ec-aafc-94923235a6fc-9f992f90; QN42=zbua0851; _q=U.ryzxozi0081; _t=24542281; csrfToken=QxdjaQNPcDnkhaMMMwxbGbpwWeKXNtET; _s=s_2QHWQF6G6AI3QWPVO6UBTX2LZE; _v=-8JqPkXGW-Vsgcr1koBOn0mWlXDIk6gdgRyueLvJJO3C0Ru2ALnLJw7DFu6Y6FUrAWf8tU-PZtj1Dc2l_o50sSp6YyMnlDQ4dVpPmDi0QMz_XOGK0loLwpTeCoe0wvE0aHJKPGHtArx4jlrdtgWSX9O2IfI8qnNi3-wHXEY6rVEN; QN44=ryzxozi0081; _i=RBTjeomvkDExEx-xsOrmQxSvMXex; _vi=7AZYnlCS385W7Z8-IQdjp5sbVR1PFm8kL0-Qi39HR1-wvJEvexvDP9L5vcTyfiBM9AUeWbCi1osGa2UEs6aMSu-IrejFGqde7L7Y04s8z115RVvdF0h-VmYrWg5Ni-nNZVw8xz3rFA7Jcv-ASn9aff2fhGbtS_0JFDKWQkwggWMx; Hm_lvt_2e7c38479e4def08a8ea1c0ebdb3e0d6=1472535537; Hm_lpvt_2e7c38479e4def08a8ea1c0ebdb3e0d6=1472541016; QN268=|1472541016285_e1523dd1fcbd8c01',
	'Host':'train.qunar.com',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest'
	}
    req=urllib.request.Request(url1,headers=headers)
    html=urllib.request.urlopen(req).read()
    decompressed_data = zlib.decompress(html ,16+zlib.MAX_WBITS)
    text = decompressed_data.decode("utf-8")
    soup=BeautifulSoup(text)
    m=str(soup)[46:-2]
    htm=json.loads(m)
    try:
        lines=htm['data']['s2sBeanList']
        print('一共查询到：%s趟车'%len(lines))
        i =1
        for item in lines:
            print("-------------第%s趟列车详情-------------"%i)
            print('--------------列车余票票价--------------')
            print('出发车站：%s'%item['dptStationName']),\
            print('到达车站：%s'%item['arrStationName']),\
            print('车次:%s'%item['trainNo']),\
            print('出发时间:%s'%item['dptTime']),\
            print('到达%s'%item['arrTime']),\
            print('历时：%s'%item['extraBeanMap']['interval']),\
            print('车票类型：%s'%item['extraBeanMap']['ticketType']),print('车次属于：%s'%item['extraBeanMap']['stationType'])
            b=item['seats']
            for key ,value in b.items():
                    print('坐席类别：%s,票价：%s,余票:%s'%(key,value['price'],value['count']))
            i+=1
    except:
        print('抱歉，您查询的车站有误或者是没有直达的火车！！！')
#--------乘车路线查询
def chaxun_luxian():
    chufadi = input('请输入你出发的地址：')
    daodadi = input('请输入你去的地方：')
    city = input('城市拼音：')
    url = 'http://bus.aibang.com/%s/?start=%s&end=%s&area=abbd&cmd=traffic&type=bus&mode=text' % (
    city, urllib.parse.quote(chufadi), urllib.parse.quote(daodadi))
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.3',
        "Host": "bus.aibang.com",}
    response = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(response).read().decode('utf-8')
    soup = BeautifulSoup(html)
    try:
        xuqiu = soup.find_all('', {'class': "s1"})
        fangshi = soup.find_all('', {'class': 's2'})
        print("一共查询到:%s条路线，详情如下：" % len(xuqiu))
        c = []
        for i in range(len(xuqiu)):
            fangshi1 = ''.join(fangshi[i].text.split())
            c.append(xuqiu[i].strong.text + '，' + '具体方式：' + fangshi1)
        for item in c:
            print(item)
    except:
        print('网络异常或者是没有找到你要查询的路线')
def Get_gongjiao():
    didian = input('请输入地点：')
    city=input('请输入城市的拼音：')
    url = 'http://bus.aibang.com/%s/stations-%s' % (city,urllib.parse.quote(didian))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.3',
        "Host": "bus.aibang.com",
    }
    response = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(response).read()
    soup = BeautifulSoup(html)
    try :
        zhan1 = soup.find_all('td', {'class': 'lh180 f14'})
        for item in zhan1:
            text = ''.join(item.text.split())
            print(text, end="\n")
    except:
        print('没有你要查询的站点')

def Get_news():
    url='http://www.toutiao.com/hot_words/?_=1471584915061'
    headers={
    "Host":"toutiao.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}
    response = urllib.request.Request(url)
    html = urllib.request.urlopen(response).read().decode('utf-8')
    ht = json.loads(html)
    print('---------------今日头条热搜榜---------------')
    for text in ht:
        print(text)
if __name__ == '__main__':
    print("一个个小小的查询功能！")
    print('作者：雷子')
    city = input('请输入要天气查询的城市名称（国内）：')
    Show_weather(city)
    Get_weather(city)
    zhishu=input('你是否想要看今天的指数：（请输入y 或者n）')
    if zhishu =='y':
        show_zhishu(city)
    else:
        pass
    will=input('你是否想要查看未来几天的天气：（请输入y 或者n）')
    if will =="yes":
        get_will(city)
    else:
        pass
    xinwen=input('你是否想要查看下新闻：（请输入y 或者n）')
    if xinwen =='y':

        print('今日头条新闻------')
        Get_xinwen()
    else:
        pass
    print('这里给您提供几个方便！')
    print('你可以输入下面的序列号，进行查询相应的内容：')
    while True:
        shuru=input('1.火车票，2.公交线路，3.目的地公交站点查询，4.段子，5.今日热闻,6.退出：')

        if shuru =='4':
            print('给你点段子')
            Get_duanzi()
        elif shuru=='1':
            print('查询火车票')
            chufa = input('请输入你要查询的上车车站：')
            daoda = input('请输入到达的火车站：')
            riqi = input('请输入你要查询的日期(格式：09-18)：')
            url1 = 'http://train.qunar.com/dict/open/s2s.do?callback=jQuery172031565032433718443_1472536168006&dptStation=%s&arrStation=%s&date=2016-%s&type=normal&user=neibu&source=site&start=1&num=500&sort=3&_=1472536168232' % (urllib.parse.quote(chufa), urllib.parse.quote(daoda), riqi)
            get_huochepiao(url1)
        elif shuru =='2':
            print('查询路线')
            chaxun_luxian()
        elif shuru=='3':
            print('公交站点')
            Get_gongjiao()
        elif shuru =='5':
            print("正在给你查询今天的热闻")
            Get_news()
        if shuru == '6':
            print('你选择退出程序！')
            print("欢迎再次使用，感谢")
            break
