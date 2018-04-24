""" 
@author: lileilei
@file: shujujiegou.py 
@time: 2018/4/23 11:22 
"""
# 对有序列表进行二分查找
def bin_search(data_set,val):
    low = 0
    high = len(data_set)-1
    while low <= high:
        mid = (low+high) // 2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return None
