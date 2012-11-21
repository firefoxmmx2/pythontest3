#!/usr/bin/env python
#coding:utf8

import pickle
import tempfile
import time
import datetime
import os
class Transaction(object):
	def __init__(self,amount=0,date=datetime.datetime.now(),currency="USD",
			usd_conversion_rate=1,description=None):
		self.__amounut=amount
		self.__date=date
		self.__currency=currency
		self.__usd_conversion_rate=usd_conversion_rate
		self.__description=description
	
	@property
	def usd(self):
		return self.__amounut * self.__usd_conversion_rate
	@property
	def currency(self):
		return self.__currency
	@property
	def amount(self):
		return self.__amounut
	@property
	def date(self):
		return self.__date
	@property
	def description(self):
		return self.__description
	@property
	def usd_conversion_rate(self):
		return self.__usd_conversion_rate

class Account(object):
	def __init__(self,accountName,transactions=[],balance=0):
		self.accountName=accountName
		self.__balance=balance
		self.transactions=[]
		for i in transactions: self.apply(i)
	@property
	def id(self):
		return self.__id
	@property
	def accountName(self):
		return self.__accountName
	@accountName.setter
	def accountName(self,accountName):
		assert len(accountName) >= 4,"账户名称必须大于4个字符"
		self.__accountName=accountName
	@property
	def balance(self):
		return self.__balance,' USD'
	@property
	def all_usd(self):
		return all([i.currency=='USD' for i in self.transactions])

	def save(self):
		'''保存当前的账户信息到磁盘'''
		#@TODO 保存的时候生成id并且使用pickle序列化模块保存到硬盘上面，保存路径为os.path.join(tempfile.gettempdir(),accountName)
		self.__id = time.time()
		savefile=open(os.path.join(tempfile.gettempdir(),self.__accountName),'wb')
		try:
			pickle.dump(self,savefile)
		finally:
			savefile.close()

	def apply(self,transaction):
		'''添加一个交易'''
		#@TODO 添加一个交易，把transaction里面的amount和账户的balance做计算，并且把添加的这个transaction加入到管理的transactions列表中。
		if transaction:
			self.__balance+=transaction.usd
			self.transactions.append(transaction)
	def load(self):
		'''载入一个已经保存的账户'''
		#@TODO 从保存路径载入一个已经序列化的对象到当前对象，替换当前的self变量，从而实现载入操作。
		savefile=open(os.path.join(tempfile.gettempdir(),self.__accountName),'rb')
		try:
			obj=pickle.load(savefile)
		finally:
			savefile.close()
		print(obj.id)
		self=obj

if __name__ == '__main__':
	acct = Account('xxxx银行')
	acct.apply(Transaction(amount=-10,description='买了拖鞋'))
	acct.apply(Transaction(amount=300,description='工资') )
	acct.apply(Transaction(amount=-200,description='买了电脑'))
	print(acct.balance)
	print(acct.all_usd)
	acct.save()
	print(acct.id)
	accts=Account('xxxx银行')
	accts.load()
	print(accts.balance)
	print(accts.id)

