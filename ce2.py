""" 
@author: lileilei
@file: ce2.py 
@time: 2018/5/21 9:23 
"""
import  socket,threading
host='127.0.0.1'
port=999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
def sendmessage():
    while True:
        input_data = input('请输入:')
        s.sendall(input_data.encode(encoding='utf-8'))
def recvmessage():
    while 1:
        data=s.recv(1024)
        if data=='':
            data=s.recv(1024)
        else:
            print(data.decode('utf-8'))
if __name__=='__main__':
    thss=[]
    th1=threading.Thread(target=sendmessage,args=())
    th2=threading.Thread(target=recvmessage,args=())
    thss.append(th1)
    thss.append(th2)
    for i in range(len(thss)):
        thss[i].start()
    thss[0].join()