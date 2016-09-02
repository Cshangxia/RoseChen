#! /usr/bin/env python
#-*- coding:utf-8 -*-


class ATest(object):

	a = ''

	def __init__(self,value):
		self.b = value

	def __setattr__(self,name,value):
		print 'i\'m setting %s = %s'%(name,value)
		self.__dict__[name] = value

	def __getattr__(self,name):
		print 'can not find attr %s!'%name

class BTest(ATest):
	
	def __init__(self,value):
		print 'initing BTest!'
		super(BTest,self).__init__(value)


#t = ATest(171)
#print 'print a = %s'%t.a
#print 'print b = %s'%t.b
#t.a = 123
t.b = 'hello,world'
print 'print a = %s'%t.a
#print 'print b = %s'%t.b
print 'print c = %s'%t.c
t.c = 'testting!!'
bt = BTest('hello,world')
bt.a = 'B'
#bt.c = 'gew'
print 'print bt.c = %s'%bt.c
setattr(ATest,'btest','heihei')
#bbt = BTest('i want nothing')
print 'bbt.btest = %s'%bbt.btest
print 't.btest = %s'%t.btest
