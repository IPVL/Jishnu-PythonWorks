#! /usr/bin/env python

def per(I):
	l = len(I)
	if l==0: yield []
	else:
		for i in range(len(I)):
			for j in per(I[:i]+I[i+1:]):
#				print "i -> %d , j -> %d" % (i,j)
				yield [I[i]]+j

for x in per(['a','b','c']): print ''.join(x)
