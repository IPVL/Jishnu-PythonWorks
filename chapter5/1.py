#!/usr/bin/env python

_1 = 'Hello'
_2 = 'World'
print _1, _2

x,y,z = 1,2,3
print y
x,z=y,x
print " ----  "
print x
print y
print z
print " ----- "
print x,y,z


x,y,z=1,2,3
z,x=x,y
print " ----  "
print x
print y
print z
print " ----- "
print x,y,z

data = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = data.popitem()
print key
print value

a = 2
a+=1
a*=2
print a

b = 'bangla'
b+='desh'
b*=2
print b

print True
print False
True = 1
False = 0
print True
print False
print 42+1+0

print bool('bangladesh')
print bool('')
print bool(234)
print bool(0)
print bool(-25)