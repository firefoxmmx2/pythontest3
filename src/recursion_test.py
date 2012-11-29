#!/usr/bin/env python

'''
尝试尾递归优化
'''

import sys
class TailRecurseException(BaseException):
    def __init__(self,args,kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_call_optimized(g):
    def func(*args,**kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back \
            and f.f_back.f_back.f_code == f.f_code:
                raise TailRecurseException(args,kwargs)
        else:
            while True:
                try:
                    return g(*args,**kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func

@tail_call_optimized
def fib(n,b1=1,b2=1,c=3):
    if n < 3:
        return 1
    else:
        if n == c:
            return b1+b2
        else:
            return fib(n,b1=b2,b2=b1+b2,c=c+1)


if __name__ == '__main__':
    print(fib(10000000))
