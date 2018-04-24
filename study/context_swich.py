""" 
@author: lileilei
@file: context_swich.py 
@time: 2018/4/23 9:07 
"""
import  gevent
'''通过sleep来实现切换'''
def foo():
    print('Running in foo')#函数执行到这一步
    gevent.sleep(0)#函数休眠，卡主，切换上下文
    print('Explicit conent switch to foo')#再次切换到foo函数，执行完毕
def bar():
    print('切换到bar')#切换到这个函数，开始执行
    gevent.sleep(0)#函数遇到阻力，卡主，切换上线文
    print('再次切换到bar')#最后执行这个函数
if __name__=='__main__':
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
    ])#加入所有的函数，来模拟上下文切换