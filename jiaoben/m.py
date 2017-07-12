import tkinter as tk
import urllib.request
import gzip
from bs4 import BeautifulSoup
import json
root = tk.Tk()
root.geometry("322x322")
#root.iconbitmap('123.ico')
root.resizable(width=False, height=False)
root.title('雷子的小工具V0.1版本')
def show():

        city=e1.get()
        url='http://wthrcdn.etouch.cn/WeatherApi?city='+urllib.parse.quote(city)
        weather= urllib.request.urlopen(url).read()
        weather_data = gzip.decompress(weather).decode('utf-8')
        try:
                soup=BeautifulSoup(weather_data)
                wheater=soup.find_all('weather')
                Text = (('湿度:%s'%soup.shidu.text),('风力:%s'%soup.fengli.text),wheater[0].high.text,wheater[0].low.text,('天气:%s'%wheater[0].type.text))
                e2['state']= 'normal'
                e2.delete(1.0,tk.END)
                e2.insert(tk.END,Text)
                e2['state']= 'disabled'
        except:
                Text ='查询不到，请确认你输入的地名是否正确'
                e2['state']= 'normal'
                e2.delete(1.0,tk.END)
                e2.insert(tk.END,Text)
                e2['state']= 'disabled'
def translation():
        try:
                context=e3.get()
                url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
                data = {}
                data['type'] = 'AUTO'
                data['i'] = context
                data['doctype'] = 'json'
                data['xmlVersion'] = '1.6'
                data['keyfrom'] = 'fanyi.web'
                data['ue'] = 'UTF-8'
                data['typoResult'] = 'true'
                data = urllib.parse.urlencode(data).encode('utf-8')
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36'}
                response=urllib.request.Request(url,data)
                html=urllib.request.urlopen(response)
                html = html.read().decode('utf-8')
                target = json.loads(html)
        
                tgt = target['translateResult'][0][0]['tgt']
                e4['state']= 'normal'
                e4.delete(1.0,tk.END)
                e4.insert(tk.END,tgt)
                e4['state']= 'disabled'
        except:
                tgt = '请确认你的翻译内容是否正确'
                e4['state']= 'normal'
                e4.delete(1.0,tk.END)
                e4.insert(tk.END,tgt)
                e4['state']= 'disabled'
if __name__ == '__main__':
    tk.Label(root, text="城市：").grid(row=0, column=0)
    tk.Label(root, text="天气").grid(row=2, column=0)

    e1 = tk.Entry(root,width=30)
    e2 = tk.Text(root,width=30,height=5, state="disabled")

    e1.grid(row=0, column=1, padx=3, pady=2)
    e2.grid(row=2, column=1, padx=3, pady=2)
    tk.Button(root, text="查询", width=10,command=show).grid(row=1, column=1, padx=70, pady=10)
    tk.Label(root, text="翻译文字：").grid(row=4, column=0)
    tk.Label(root, text="翻译结果").grid(row=7, column=0)
    e3 = tk.Entry(root,width=30)
    e4 = tk.Text(root,width=30,height=5, state="disabled")

    e3.grid(row=4, column=1, padx=3, pady=2)
    e4.grid(row=7, column=1, padx=3, pady=2)
    tk.Button(root, text="翻译", width=10,command=translation).grid(row=5, column=1, padx=70, pady=10)
 
    tk.mainloop()
    
