#coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import json
import random
import zlib
#ip_list=['118.212.80.133:8118','222.170.17.74:2226','110.73.43.101:8183']
url='http://train.qunar.com/dict/open/s2s.do?callback=jQuery172031565032433718443_1472536168006&dptStation=%E5%8C%97%E4%BA%AC&arrStation=%E4%B8%8A%E6%B5%B7&date=2016-08-31&type=normal&user=neibu&source=site&start=1&num=500&sort=3&_=1472536168232'
headers={'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Cookie':'QN99=3733; QN1=eIQiP1dEAASbOq51LyeNAg==; QunarGlobal=192.168.31.105_-4c70ffc_154e15d8dc8_2de|1464074245311; ag_fid=AsWRT9vZYYLJ23qF; __ag_cm_=1464074247005; QN269=906FD473217F11E6B393C4346BAC1530; PHPSESSID=epq85mhbfeg12b3t6q8rkic702; QN25=5cfd26dc-8670-44ec-aafc-94923235a6fc-9f992f90; QN42=zbua0851; _q=U.ryzxozi0081; _t=24542281; csrfToken=QxdjaQNPcDnkhaMMMwxbGbpwWeKXNtET; _s=s_2QHWQF6G6AI3QWPVO6UBTX2LZE; _v=-8JqPkXGW-Vsgcr1koBOn0mWlXDIk6gdgRyueLvJJO3C0Ru2ALnLJw7DFu6Y6FUrAWf8tU-PZtj1Dc2l_o50sSp6YyMnlDQ4dVpPmDi0QMz_XOGK0loLwpTeCoe0wvE0aHJKPGHtArx4jlrdtgWSX9O2IfI8qnNi3-wHXEY6rVEN; QN44=ryzxozi0081; _i=RBTjeomvkDExEx-xsOrmQxSvMXex; _vi=7AZYnlCS385W7Z8-IQdjp5sbVR1PFm8kL0-Qi39HR1-wvJEvexvDP9L5vcTyfiBM9AUeWbCi1osGa2UEs6aMSu-IrejFGqde7L7Y04s8z115RVvdF0h-VmYrWg5Ni-nNZVw8xz3rFA7Jcv-ASn9aff2fhGbtS_0JFDKWQkwggWMx; Hm_lvt_2e7c38479e4def08a8ea1c0ebdb3e0d6=1472535537; Hm_lpvt_2e7c38479e4def08a8ea1c0ebdb3e0d6=1472541016; QN268=|1472541016285_e1523dd1fcbd8c01',
'Host':'train.qunar.com',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}
#proxy_support = urllib.request.ProxyHandler({'http':random.choice(ip_list)}) 
#opener = urllib.request.build_opener(proxy_support) 
#urllib.request.install_opener(opener)
req=urllib.request.Request(url,headers=headers)
html=urllib.request.urlopen(req).read()
decompressed_data = zlib.decompress(html ,16+zlib.MAX_WBITS)
text = decompressed_data.decode("utf-8")
soup=BeautifulSoup(text)
m=str(soup)[46:-2]
htm=json.loads(m)
lines=htm['data']['s2sBeanList']
print('一共查询到：%s趟车'%len(lines))

for item in lines:
	#print('到达车站：%s'%item['arrStationName']),print('出发车站：%s'%item['dptStationName']),print('车次:%s'%item['trainNo']),print('出发时间:%s'%item['dptTime']),print('到达%s'%item['arrTime']),print('历时：%s'%item['extraBeanMap']['interval']),print('车票类型：%s'%item['extraBeanMap']['ticketType']),print('车次属于：%s'%item['extraBeanMap']['stationType'])

	print(item['seats'])
