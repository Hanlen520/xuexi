# -*- coding: utf-8 -*-
# @Date    : 2018-07-08 13:40:56
# @Author  : leizi
#print(complex(1,2))#复数
#print(bytearray([1,2,3]))#返回字节的新数组
#m=(bytearray('rooot','utf-8'))
#rint(m.count)
'''import datetime
print(datetime.datetime.today())#现在的时间
print(datetime.datetime.now())#当前时间
print(datetime.datetime(2017,6,1,hour=13,minute=17,second=30))#生成制定时间的
from datetime import datetime
now=datetime.now()
print(now.strftime('%a, %b %d %H:%M'))#星期几，几月，几日
print(now.strftime('%Y-%M-%d %H:%M:%S'))
from heapq import *
def heasort(initi):# 排序
	h=[]
	for value in initi:
		heappush(h,value)#将每一个item进入heap中
	return [heappop(h) for  i in range(len(h))]
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:              
        middle = int(len(seq)/2)
        left = merge_sort(seq[:middle])
        right = merge_sort(seq[middle:])
        return list(merge(left, right)) 
if __name__ == '__main__':
	seq=[1,3,6,2,4]
	print(merge_sort(seq))
	print(heasort([11,2,31,4]))

import linecache
with open('study.py',encoding='utf-8') as f:
	print(linecache.getline('beijing.txt',1))

import codecs
fw=codecs.open('beijing.txt','a+','utf-8')
fw.write('dddd')
	'''
from enum import Enum
Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name ,member in Month.__members__.items():
	if 'Mar'== name:
		print('在')
	else:
		print('不在')