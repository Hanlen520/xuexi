import urllib.request
from bs4 import BeautifulSoup 
import time
def head():
	headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
	}
	return headers
def parse_url(url):
	hea=head()
	resposne=urllib.request.Request(url,headers=hea)
	html=urllib.request.urlopen(resposne).read().decode('gb2312')
	return html
def url_s():
	url='http://www.w3school.com.cn/jquery/index.asp'
	html=parse_url(url)
	soup=BeautifulSoup(html)
	me=soup.find_all(id='course')
	m_url_text=[]
	m_url=[]
	for link in me:
		m_url_text.append(link.text)
		m=link.find_all('a')
		for i in m:
			m_url.append(i.get('href'))
	for i in m_url_text:
		h=i.encode('utf-8').decode('utf-8')
		m_url_text=h.split('\n')
	return m_url,m_url_text

def xml():
	url,url_text=url_s()
	url_jque=[]
	for link in url:
		url_jque.append('http://www.w3school.com.cn/'+link)
	return url_jque
def xiazai():
	urls=xml()
	i=0
	for url in urls:
		html=parse_url(url)
		soup=BeautifulSoup(html)
		me=soup.find_all(id='maincontent')
		with open(r'%s.txt'%i,'wb') as f:
			for h in me:
				f.write(h.text.encode('utf-8'))
				print(i)
		i+=1
if __name__ == '__main__':
	xiazai()



