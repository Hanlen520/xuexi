import urllib.request
import json
kuaidi_id={
'百世汇通':'huitongkuaidi',
'德邦':'debangwuliu',
'国通':'guotongkuaidi',
'汇通':'huitongkuaidi',
'佳怡物流':'jiayiwuliu',
'全峰':'quanfengkuaidi',
'如风达':'rufengda',
'圆通':'yuantong',
'韵达':'yunda',
'顺丰':'shunfeng',
'中通':'zhongtong',
'宅急送':'zhaijisong',
'中铁':'ztky',
'中铁快运':'zhongtiewuliu',
'申通':'shentong',
'京东':'jingdong',
'天天':'tiantian'}
gongsi=input('请输入你要查询的公司：')
baoguo=int(input('请输入您要查询的公司的快递单号：'))
url='http://www.kuaidi100.com/query?type=%s&postid=%s'%(kuaidi_id[gongsi],baoguo)
html=urllib.request.urlopen(url).read().decode('utf-8')
html=json.loads(html)

sou=html['data']
for item in sou:
          print('时间：%s'%item['time'])
          print('状态：%s'%item['context'])
         

