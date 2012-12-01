#!/usr/bin/env python

def calc(str):
	import re

	num=re.compile(r'\d+')
	opr=re.compile(r'[+\-*/()]')
	rgt={'(':0,'+':1,'*':2,'/':2,')':3}
	fac={'+':lambda x,y:x+y, '-':lambda x,y:x-y,'*':lambda x,y:x*y,
        '/':lambda x,y:x/y}
	ans=[]
	stk=['()',]

	while str:
		i=num.match(str)
		j=opr.match(str)
		if i:
			ans.append(int(i.group(),10))
			str=str[i.end():]
		elif j:
			if str[0] == '(':
				stk.append(str[0])
			elif str[0] == ')':
				while stk[-1]!='(':
					ans[-2] = fac[stk.pop()](ans[-2],ans[-1])
					ans.pop()
				stk.pop()
			else:
				while rgt[stk[-1]] >= rgt[str[0]]:
					ans[-2] = fac[stk.pop()](ans[-2],ans[-1])
					ans.pop()
				stk.append(str[0])
			str=str[1:]
		else:
			return 0
	while stk[-1] != '(':
		ans[-2] = fac[stk.pop()](ans[-2],ans[-1])
		ans.pop()

	return ans[0]

if __name__ == '__main__':
	print(calc("1+2"))
