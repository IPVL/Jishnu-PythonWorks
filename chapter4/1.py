#!/usr/bin/env python
from copy import deepcopy

names = ['ashraful', 'jishnu', 'fahad']
numbers = [26,27,28]
print numbers[names.index('jishnu')]
phonebook = {'Ashraful': '26', 'Jishnu': '27', 'Fahad': '28' }
print phonebook['Fahad']
items = [('name', 'Jishnu'), ('age', 42)]
d = dict(items)
print d

x = {}
x[32]='JB'
print x

#clear
a = {}
b=a;
a['a']=12
a['b']=13
a['c']=14
print a
print b
a = {}
print a
print b

#copy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy();
y['username'] = 'root'
y['machines'].remove('bar')
print x
print y
p = {}
p['numbers'] = [0,1,2,3,4]
q = p.copy()
O_O = deepcopy(p)
p['numbers'].remove(2)
print q
print O_O

#get
print p.get('numbers')