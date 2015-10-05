#!/usr/bin/env python

#try:
#	x = raw_input("input N1 : ")
#	y = raw_input("input N2 : ")
#	print int(x)/int(y)
#except ZeroDivisionError:
#	print "Divided by Zero"
#except ValueError:
#	print "That wasn't a number"


#try:
#	x = raw_input("input N1 : ")
#	y = raw_input("input N2 : ")
#	print int(x)/int(y)
#except (ZeroDivisionError,ValueError):
#	print "Enter Valid Numbers"

#try:
#	x = raw_input("input N1 : ")
#	y = raw_input("input N2 : ")
#	print int(x)/int(y)
#except (ZeroDivisionError,ValueError), cd:
#	print cd

#try:
#	x = raw_input("input N1 : ")
#	y = raw_input("input N2 : ")
#	print int(x)/int(y)
#except:
#	print "Enter Valid Numbers"

#while True:
#	try:
#		x = raw_input("input N1 : ")
#		y = raw_input("input N2 : ")
#		print int(x)/int(y)
#	except:
#		print "Enter Valid Numbers"
#	else:
#		break

try:
	x = raw_input("Get N1:")
	y = raw_input("Get N2:")
	print int(x)/int(y)
except Exception, e:
	print 'give correct input'
else:
	print "Its fine"
finally:
	print 'Cleaning Up'