'''
#乘法口诀
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print("")

打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
for i in range(10,1000):
    sum=0 #各个位数的立方和
    temp=i
    while temp:
        sum=sum+(temp%10)**3   #累加
        temp//=10   #地板除
    if sum==i:
        print(i)
           '''
'''
有 1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？


cnt = 0
for i in range(1,5):
    for j in range(1,5):
       for k in range(1,5):
            if i!=j and i!=k and j!=k:
                print (i*100+j*10+k)
                cnt+=1
print (cnt)
'''
'''企业发放的奖金根据利润提成。利润(I)低于或等于 10万元时，奖金可提 10%；
利润高于 10万元，低于 20 万元时，低于10 万元的部分按 10%提成，高于 10万元的部分，可提成 7.5%；
20 万到40 万之间时，高于 20 万元的部分，可提成5%；40万到 60 万之间时高于40 万元的部分，可提成 3%；
60万到100万之间时，高于 60 万元的部分，可提成1.5%，高于100万元时，超过 100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

m=input('请输入月利润:')
n=int(m)
if 0<n <=100000:
    print('你的提成是:%d'%(n*0.1))
elif 100000<n<=200000:
    print('你的提成是:%d'%(100000*0.1+(n-100000)*0.075))
elif 200000<n<=400000:
    print('你的提成是:%d'%(100000*0.1+(100000)*0.075+(n-200000)*0.05))
elif 400000<n<=600000:
    print('你的提成是:%d'%(100000*0.1+(100000)*0.075+200000*0.05+(n-400000)*0.03))
elif 600000<n<=1000000:
    print('你的提成是:%d'%(100000*0.1+(100000)*0.075+200000*0.05+400000*0.03+(n-600000)*0.015))
elif n>1000000:
    print('你的提成是:%d'%(100000*0.1+(100000)*0.075+200000*0.05+400000*0.03+400000*0.015+(n-1000000)*0.01))
else:
    print('请确认利润是否正确')'''
'''一个整数，它加上 100 后是一个完全平方数，再加上 168又是一个完全平方数，请问该数是多少？
import math
num=1
while True:
    if math.sqrt(num+100)-(int(math.sqrt(num+100)))==0 and  math.sqrt(num+268)-(int(math.sqrt(num+268)))==0:
        print(num)
        break
    num+=1'''
'''输入某年某月某日，判断这一天是这一年的第几天？
import datetime
das=input('请输入年月日(如:20150103) :')
dta=datetime.datetime.strptime(das,'%Y%m%d')
m=(str(das))[:4]+'0101'
m=datetime.datetime.strptime(m,'%Y%m%d')
h=(int((dta-m).days)+1)
print(h)'''
'''输入三个整数 x,y,z，请把这三个数由小到大输出。
x=input()
y=input()
z=input()
n=0
if int(x)>int(y):
    if int(z)>int(y):
        if int(z)>int(x):
            print(z,x,y)
        else:
            print(x,z,y)
    else:
        print(x,y,z)

elif int(y)<int(z):
    print(z,x,y)
else:
    print(x,y,z)
'''
"""利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
score=int(input('请输入分数:'))
if score >=90:
    print('评级为:A')
elif 60<score<=89:
    print('评级为:B')
else:
    print('评级为:C')
"""
