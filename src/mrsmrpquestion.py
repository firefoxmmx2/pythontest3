#!/usr/bin/env python

'''
美国斯坦福大学的麦卡锡提出的：
	设有两个自然数x,y 且 2<=x<=y<=99,S先生知道这两个数的和S,P先生知道这两个数的积
	P，他们二人进行了如下对话：
	S：我确信你不知道这两个数是什么，但我也不知道。
	P：一听你这样一说，我就知道这两个数是什么了。
	S：我也是，现在我也知道了
	问：现在你能通过他们的对话推断出这两个数是什么吗？
'''

def gatherBy(seq, f):
	d = {}
	for x in seq:
		d.setdefault(f(x), []).append(x)
	return d

pool = [(a,b) for a in range(2,98+1) for b in range(2, a+1)]
sums = gatherBy(pool, lambda x: x[0]+x[1])
prods = gatherBy(pool, lambda x:x[0]*x[1])

def mrp_dont_know(p):
	return len(prods[p]) != 1

def mrs_dont_know(s):
	return len(sums[s]) != 1

def mrs_know_mrp_doesnt_know(s):
	return all([mrp_dont_know(a*b) for a,b in sums[s]])

def mrp_now_knows(p):
	return len([(a,b) for a, b in prods[p]
			if mrs_know_mrp_doesnt_know(a+b)]) == 1

def mrs_knows_mrp_now_know(s):
	return len([(a,b) for a,b in sums[s] if
			mrs_know_mrp_doesnt_know(a+b)]) == 1

for a,b in pool:
	s = a+b
	p = a*b
	if mrp_dont_know(p) and mrs_dont_know(s) and\
		mrs_know_mrp_doesnt_know(s) and\
		mrp_now_knows(p) and mrs_know_mrp_doesnt_know(s):
			print(a,b)
