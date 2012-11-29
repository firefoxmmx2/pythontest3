#!/usr/bin/env python

'''
Created on 2012-11-27

'''

from functools import reduce 
#new guys
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(6))

#lazy guys
def fact(x):
    return x>1 and x*fact(x-1) or 1
print(fact(6))

#more lazy guys
f = lambda x: x and x*f(x-1) or 1
print(f(6))

#pro
fact = lambda x: reduce(int.__mul__,range(2,x+1),1)
print(fact(6))

#hack
#import sys
#@tailcall
#def fact(x,acc=1):
#    if x: return fact(x.__sub__(1),acc.__mul__(x))
#    return acc
#sys.stdout.write(str(fact(6)+'\n'))
