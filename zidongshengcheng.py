import random
from shouji import suiji
xingshi=[]
mingzhi=[]
mingzi=[]
def zidong():
    with open('xingshi.txt','r',encoding='utf-8') as f1:
        for lines in f1.readlines():
            temp=lines.strip('\n').split(' ')
            xingshi.extend(temp)
    with open ('xingming.txt','r') as f2:
        for lines in f2.readlines():
            temp2=lines.split('、')
            mingzhi.extend(temp2)
    xingsh=random.choice(xingshi)
    ming=''
    for i in range(1):
        mingzi.append(random.choice(mingzhi,))
        ming=''.join(mingzi)
    print(xingsh+ming)

if __name__ == '__main__':
    xuqiu=input("请输入你要生成的个数:")
    j=0
    while j < int(xuqiu):
        print("自动生成姓名：" ),zidong()
        print("自动生成手机号："),suiji()
        j +=1
    


