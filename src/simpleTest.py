#!/bin/python
# coding:utf8
'''
Created on 2011-4-5

@author: hooxin
'''

# for(j=i; j<b;j--)
#
#
#
#
#

def binInsertSort(list=[],n=0):
	key,left,right,middle = 0,0,0,0
	
	for i in range(n):
		key=list[i]
		left=0
		right=i-1
		while left<=right:
			middle=(left+right)//2
			if list[middle] > key:
				right=middle-1
			else:
				left=middle+1
		
		for j in reversed(range(left,i)):
			list[j+1]=list[j]
			
		list[left]=key
		
	return list	
	
def selectSort(list=[],_from=0, len=0):
	for i in range(len):
		smallest=i
		for j in range(i+_from,_from+len):
			if list[j] < list[smallest]:
				smallest=j
		tmp=list[i]
		list[i]=list[smallest]
		list[smallest]=tmp
	return list

def shellSort(list,_form=0,len=0):
	def shellModifyInsertSort(__list,__form,__len,__delta):
		if __len<=1 :
			return
		
		for i in range(__form+__delta,__form+__len,__delta):
			tmp=__list[i]
			j=i
			for j in reversed(range(i,__form,__delta)):
				if tmp < __list[j-delta]:
					__list[j]=__list[j-delta]
				else:
					break
			__list[j]=tmp
	
	value=1
	while (value+1)*2 < len:
		value=(value+1)*2-1
	delta=value
	while delta >= 1:
		for i in range(delta):
			shellModifyInsertSort(list,_form+i,len-i,delta)
		delta=(delta+1)//2-1
	return list
	
def quicksort(list,form,len):
	def partion(__list,__form,__to,__pivot):
		tmp=__list[__pivot]
		__list[__pivot]=__list[__to]
		
		while __form != __to:
			while __form < __to and __list[__form] <= tmp :
				__form+=1
			if __form < __to:
				__list[__to]=__list[__form]
				__to-=1
				
			while __form<__to and __list[__to] >= tmp :
				__to-=1
			if __form < __to:
				__list[__form]=__list[__to]
				__form+=1
		__list[__form]=tmp
		return __form
	
	def selectPivot(__list,__form,__to):
		return (__form + __to) // 2
	
	def q_sort(__list,__form,__to):
		if __to - __form < 1 :
			return
		pivot = selectPivot(__list, __form, __to)
		
		pivot=partion(__list, __form, __to, pivot)
		
		q_sort(__list, __form, pivot-1)
		q_sort(__list,pivot+1,__to)
		
	
	q_sort(list, form, form+len-1)
	return list

if __name__ == "__main__":
	a=[1,2,4,5,9,3,2,1]
#	a = binInsertSort(a,len(a))
	a=quicksort(a,0, len(a))
	print(a)
	

