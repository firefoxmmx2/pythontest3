#!/usr/bin/env python   
# -*- coding:utf-8   
  
class HttpBase:   
	def get(self):   
		pass 
class Http1(HttpBase):   
	def get(self):   
		print( 'http1'   )
class Http2(HttpBase):   
	def get(self):   
		print( 'http2'   )
  
  
class Base:   
	def __init__(self):   
		self.httpobj = None   
	def http(self):   
		self.httpobj.get()   
	def compute(self):   
		self.http()   
		self.show()   
	#虚函数   
	def show(self):   
		pass   
	def notify(self, k):   
		print( 'notify', k )  
		  
  
#桥接模式，通过A，B 关联不同的http1和http2   
class BaseA(Base):   
	def __init__(self):   
		self.httpobj = Http1()		  
	def notify(self, k):   
		print ('A notify', k)	   
	def show(self):   
		print ('show a')   
			 
class BaseB(Base):   
	def __init__(self):   
		self.httpobj = Http2()   
	def notify(self, k):   
		print ('B notify', k)   
	def show(self):   
		print ('show b'   )
  
#观测者模式   
class Observer:   
	def __init__(self):   
		self.listOB = []   
	def register(self, obj):   
		self.listOB.append(obj)   
	def notify(self):   
		for obj in self.listOB:   
			obj.notify(len(self.listOB))   
  
#适配器模式   
class B1:   
	def http(self):   
		BaseB().http()   
#工厂模式   
class Factory:   
	def CreateA(self):   
		return BaseA()   
	def CreateB(self):   
		return BaseB()   
  
  
#单例模式   
class Logger(object):   
	log = None   
	@staticmethod   
	def new():   
		  
		import threading   
		#线程安全   
		mylock = threading.RLock()   
		mylock.acquire()   
		if not Logger.log:   
			Logger.log = Logger()   
		mylock.release()   
		  
		return Logger.log   
	def write(self, v):   
		print ('Logger ', v)   
  
if __name__ == "__main__":   
	a = Factory().CreateA()   
	b = Factory().CreateB()   
	  
	objS = Observer()   
	objS.register(a)   
	objS.register(b)   
	  
	a.compute()   
	b.compute()   
	objS.notify()   
	  
	b1 = B1()   
	b1.http()   
	  
	Logger.new().log.write('v')   
