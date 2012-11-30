#!/usr/bin/env python

'''
Created on 2012-11-27
一般来说计算模块运行时间的通用办法
'''

from time import time

def timeTest():
    start = time()
    print("start: "+str(start))
    for i in range(1,100000000):
        pass
    stop = time()
    print("stop: "+str(stop))
    print("runtime is {0} second".format((stop - start)))
    
if __name__ == '__main__':
    timeTest()