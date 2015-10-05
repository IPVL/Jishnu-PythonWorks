#!/usr/bin/env python

class Bird:
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print "Ahaaaaah ...."
			self.hungry = False
		else:
			print 'No Thanks!'

obj = Bird()
print obj.eat()
print obj.eat()
print obj.eat()

'''
class ArithmeticSequence:
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.changed = {}
	def __getitem__(self,key):
		#checkIndex(key)
		try: return self.changed[key]
		except keyError:
			return self.start+key*self.step
	def __setitem__(self,key,value):
		checkIndex(key)
		self.changed[key] = value

S = ArithmeticSequence(1,2)
#print S[4]
for i in range (0,10):
	print S[i]

''' #It doesn't work

class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def next(self):
		self.a, self.b = self.b, self.a+self.b
		return self.a
	def __iter__(self):
		return self

fibs = Fibs()

for i in fibs:
	if i>1000:
		print i
		break
