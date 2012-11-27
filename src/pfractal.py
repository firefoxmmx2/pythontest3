#!/usr/bin/env python

from turtle import *

def f(length,depth):
    if depth == 0:
        forward(length)
    else:
        f(length/3,depth-1)
        right(60)
        f(length/3,depth-1)
        left(120)
        f(length/3,depth-1)
        right(60)
        f(length/3,depth-1)

def snowflake(length):
    def f(length):
        yield length/3
        right(60)
        yield length/3
        left(120)
        yield length/3
        right(60)
        yield length/3
    for a in f(length):
        for b in f(a):
            forward(b)
if __name__ == '__main__':
    #f(1000,5)
    snowflake(500)

