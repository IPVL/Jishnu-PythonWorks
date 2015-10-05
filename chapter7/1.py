#!/usr/bin/env python

def add(a,b):
	return a+b

print add(2,2)
print add('bangla','desh')

class person:
	def setname(self,name):
		self.name = name
	def getname(self):
		return self.name
	def greet(self):
		print "Hello: "+self.name

jishnu = person()
jishnu.setname("jishnu")
print jishnu.getname
jishnu.greet

class Bird:
	song = 'quack'
	def sing(self):
		print self.song

bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()
print '  ------  '

class bangla:
	def __inaccessible(self):
		print '9'
	def _kemne(self):
		print 'ommitted'
		self.__inaccessible()

_a = bangla()
#_a.__inaccessible()
_a._kemne()
_a._bangla__inaccessible()

class Filter:
	def init(self):
		self.blocked = [3]
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
	def init(self):
		self.blocked = ['SPAM']

f = Filter()
print f.init()
print f.filter([1,2,3])
print f.filter(['a',5,'r',3,9,0])

s = SPAMFilter()
s.init()
print s.filter(['SPAM','JB','ASH'])

print issubclass(SPAMFilter, Filter)
print issubclass(Filter, SPAMFilter)

print SPAMFilter.__bases__
print Filter.__bases__
print bangla.__bases__

print isinstance(f,Filter)
print isinstance(s,Filter)
print isinstance(f,SPAMFilter)
print isinstance(s,SPAMFilter)

print s.__class__
print hasattr(s,'SPAMFilter')