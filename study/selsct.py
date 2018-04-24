""" 
@author: lileilei
@file: selsct.py 
@time: 2018/4/23 9:14 
"""
import  time,gevent
from gevent import select
start=time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)
def gr1():
    print('Started Polling: %s' % tic())
    select.select([], [], [], 1)#阻塞
    print('Ended Polling: %s' % tic())
def gr2():
    print('Started Polling: %s' % tic())
    select.select([], [], [], 1)#阻塞
    print('Ended Polling: %s' % tic())
def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)#阻塞
gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])