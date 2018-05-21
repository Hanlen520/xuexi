# -*- coding: utf-8 -*-
# @Date    : 2018-05-21 08:34:16
# @Author  : lileilei
import socket,threading
from time import sleep,ctime
host='127.0.0.1'
port=999
beijin=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
beijin.bind((host,port))
beijin.listen(2)
data=''
data2=''
def resvmess(coon,coon1,addetr,addetr2):
    while True:
        data=coon.recv(1024)
        data2=coon1.recv(1024)
        coon.sendall(('收到来自：%s,时间是：%s，消息内容：%s'%(addetr2,ctime(),data2)).encode(encoding='utf-8'))
        coon1.sendall(('收到来自：%s,时间是：%s，消息内容：%s'%(addetr,ctime(),data)).encode(encoding='utf-8'))
if __name__=='__main__':
    while True:
        coon, addetr = beijin.accept()
        coon1, addetr2 = beijin.accept()
        m1=threading.Thread(target=resvmess,args=(coon,coon1,addetr,addetr2))
        m1.start()