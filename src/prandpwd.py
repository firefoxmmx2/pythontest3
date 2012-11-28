#!/usr/bin/env python

'''
Created on 2012-11-28
通过命令行,生成随机密码
'''

from optparse import OptionParser
import string
from random import randint

#可用的符号
sign = "~!@#$%^&*()_+="

def randpwd(length,has_sign):
    seed = string.ascii_letters + string.digits
    if has_sign:
        seed += sign
    return "".join([seed[randint(0,len(seed)-1)] for i in range(0,length)])

def main():
    parse = OptionParser("usege: prandpwd.py [option] ")
    parse.add_option("-L","--length",help="password length",dest="length",default=8)
    parse.add_option("-s","--hassign",help="contain sign",dest="has_sign",default=str(False))
    
    (options,args) = parse.parse_args()
     
    length = int(options.length)
    has_sign = bool(options.has_sign)
    
    print(randpwd(length, has_sign))

if __name__ == '__main__':
    main()