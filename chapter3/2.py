#!/usr/bin/env python
from math import pi

print '%s + %s = %s' % (1,1,2)

print 'price of eggs: %d taka' % 10 
print 'Hexadecimal price of eggs: %x taka' % 10
print 'Pi: %f ' % pi
print 'Very Inexact Estimate of Pi: %d' %pi
print '%s' % 42L
print '%r' % 42L

#Field Width

print '%10f' % pi  # Fills up at least 10 fields
print '%1f' % pi
print '%10.2f' % pi  #Fills up at least 10 fields befor . and exactly 2 fields after .
print '%.2f' % pi  #2 fields after .
print '%.6s' % 'Bangladesh' #first 6 characters of the string
print '%.*s' % (6,'Bangladesh') # as above
print '%010.2f' % pi
print '%-10.2f' % pi #leaves the required space to the right
print '%+10d' % 32 	#means the sign of the number is set to the left 
					#whether it is positive or negative


#A formatted price list

width = 35
price_width = 10
item_width = 25

header_format = '%-*s%*s'
formatt = '%-*s%*.2f'

print "="*35
print header_format % (item_width, 'Item', price_width, 'Price')
print 35*"_"
print formatt%(item_width, 'mango', price_width, 50.0)
print formatt%(item_width, 'banana', price_width, 12.0)
print formatt%(item_width, 'jellatto', price_width, 70.0)
print formatt%(item_width, 'vegetable', price_width, 30.0)
print 35*"="