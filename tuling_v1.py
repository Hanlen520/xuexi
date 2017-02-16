# coding=utf-8
import json,urllib

def zidonghuifu(content):
    url='http://www.tuling123.com/openapi/api'
    data={"key": "your key", "info": content}

    data=urllib.urlencode(data)
    html=urllib.urlopen(url,data).read()
    j=json.loads(html)
    code=j['code']
    if code == 100000:
        recontent = j['text']
    elif code == 200000:
        recontent = j['text']+j['url']
    elif code == 302000:
        recontent = j['text']+j['list'][0]['article']+j['list'][0]['detailurl']
    elif code == 308000:
        recontent = j['text']+j['list'][0]['info']+j['list'][0]['detailurl']
    else:
        recontent = '这货还没学会怎么回复这句话'
    return recontent

if __name__=='__main__':
    while True:
        content=raw_input('问：')
        me=zidonghuifu(content)
        print(me)
