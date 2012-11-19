#coding:utf8
'''
Created on 2011-2-28

@author: hooxin
'''

import chardet
import os



with open(os.path.expandvars('$HOME')+'/detectfile.txt',mode='rb') as detectfile:
	strg=detectfile.read()
	#侦测字节数组里面的编码信息
	detectresult=chardet.detect(strg)
	if detectresult != 'Unknown':
		strg=str(strg,encoding=detectresult['encoding']) 
	print(strg) 
