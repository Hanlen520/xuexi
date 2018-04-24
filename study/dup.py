""" 
@author: lileilei
@file: dup.py 
@time: 2018/4/23 9:39 
"""
from multiprocessing import  Pool
import time
def task(n):
    print('task is start' ,n)
    time.sleep(2)
    print('this is task',n)
if __name__=='__main__':
    p=Pool(5)
    for i in range(10):
        p.apply_async(task,args=(str(i)))
    p.close()
    p.join()