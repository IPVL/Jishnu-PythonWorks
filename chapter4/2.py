#!/usr/bin/env python

#has key
d = {}
print d.has_key('jb')
d['jb'] = [1,2,3,4]
print d.has_key('jb')

#items and iteritems
d = {'a':1, 'b':2, 'c':3}
print d.items()
it = d.iteritems()
print list(it)

#pop
d.pop('b')
print d

#setdefault
d={}
d.setdefault('name', 'N/A')
print d

#update
d['name'] = 'JB'
x = {'name' : 'Shakib'}
d.update(x)
print d