""" 
@author: lileilei
@file: sort.py 
@time: 2018/4/23 13:28 
"""
def inertsort(seq):#插入排序
    for j in range(1,len(seq)):
        key=seq[j]
        i=j-1
        while i>=0 and seq[i]>key:
            seq[i+1]=seq[i]
            i-=1
        seq[i+1]=key
def selectsort(seq):#选择排序
    le=len(seq)
    for i in range(le-1):
        mininde=i
        for j in range(i,le):
            if seq[mininde]>seq[j]:
                mininde=j
        if i !=mininde:
            seq[i],seq[mininde]=seq[mininde],seq[i]
def paobao(seq):#冒泡
    for i in range(len(seq)):
        for j in range(len(seq)-1,i,-1):
            if seq[j]<seq[j-1]:
                seq[j-1],seq[j]=seq[j],seq[j-1]
if __name__=='__main__':
    seq=[5,2,4,6,1,3]
    paobao(seq)
    print(seq)