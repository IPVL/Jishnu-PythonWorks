#!/usr/bin/env python

import math
import test
import webbrowser

print math.sin(1.570)  #value in radian
test.hello()

print __name__
print test.__name__

print range.__doc__
webbrowser.open

print ''
print ''
print ''
print '   ----   '
print ''
print ''
print ''

a = set([1,2,3])
b = set([2,3,4])
print a&b
print a|b
print a-b
print (a&b).issubset(a)
print (a&b)<=a
print (a&b)>=b
print b>=(a&b)
print a.intersection(b)
print a.issuperset(a&b)
print (a&b).issuperset(a)
print a^b
print a.copy() is a
print a.copy()==a
print set([1,8,4,5,2,4])
print set([1,2,3,4,5,6,7,8,9,0])
print set([5,5,5,5,5])
print random()