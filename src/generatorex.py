#!/usr/bin/env python
# -*- Coding:utf-8 -*-

'''
Created on 2012-6-5

@author: hooxin
'''

def generatorex(list):
    for e in list:
        enew = yield e

it = generatorex(range(1,10,3))
print(next(it))
print(next(it))
print(next(it))
