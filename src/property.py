#!/usr/bin/env python
#coding:utf8

_identity=lambda x:x
class SortedList:
	
	def __init__(self,sequence=None,key=None):
		self.__key=key or _identity
		assert hasattr(self.__key,"__call__")
		if sequence is None:
			self.__list=[]
		elif (isinstance(sequence,SortedList) and 
				sequence.key == self.__key):
			self.__list=sequence.__list[:]
		else:
			self.__list=sorted(list(sequence),key=self.__key)

	@property
	def key(self):
		return self.__key

	def add(self,value):
		index=self.__bisect_left(value)
		if index==len(self.__list):
			self.__list.append(value)
		else:
			self.__list.insert(index,value)

	def __bisect_left(self,value):
		key=self.__key(value)
		left,right=0,len(self.__list)
		while left<right:
			middle=(left+right)//2
			if self.__key(self.__list[middle]) < key:
				left=middle+1
			else:
				right=middle
		return left
	def remove(self,value):
		index=self.__bisect_left(value)
		if index<len(self.__list) and self.__list[index]==value:
			del self.__list[index]
		else:
			raise ValueError("{0}.remove(x):x not in list.".format(self.__calss__.__name__))
	def remove_every(self,value):
		count=0
		index=self.__bisect_left(value)
		while(index<len(self.__list) and self.__list[index]==value):
			del self.__list[index]
			count+=1
		return count
	def count(self,value):
		count=0
		index=self.__bisect_left(value)
		while(index<len(self.__list) and self.__list[index]==value):
			index+=1;count+=1
		return count

	def index(self,value):
		index=self.__bisect_left(value)
		if index<len(self.__list) and self.__list[index]==value:
			return index
		raise ValueError("{0}.index(x):x not in list".format(self.__class__.__name__))
	def __delitem__(self,index):
		del self.__list[index]
	def __getitem__(self,index):
		return self.__list[index]
	def __setitem__(self,index,value):
		raise TypeError(("use add() to insert a value and rely on"
				"the list to put it in the right place"))
	def __iter__(self):
		return iter(self.__list)
	def __reversed__(self):
		return reversed(self.__list)
	def __contains__(self,value):
		index=self.__bisect_left(value)
		return (index<len(self.__list) and self.__list[index]==value)
	def clear(self):
		self.__list=[]
	def pop(self,index=-1):
		return self.__list.pop(index)
	def __len__(self):
		return len(self.__list)
	def __str__(self):
		return str(self.__list)
	def __iadd__(self,value):
		self.add(value)
		return self
	def __isub__(self,value):
		self.remove(value)
		return self
	def __add__(self,value):
		if "list" in str(type(value)):
			for val in value:
				self.add(val)
		else:
			raise TypeError("must use list or SortedList")
		return self
	def __str__(self):
		return str(self.__list)

if __name__ == '__main__':
	test=SortedList(['b','ss'])
	try:
		test[0]='f'
	except Exception as e:
		print(e)
		test.add('f')
	test.add('a')
	test+='d'
	test=test+['s','x']
	print(test)
