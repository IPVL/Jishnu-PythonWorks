#! /usr/bin/env python

def fibo():
	a,b=0,1
	while 1:
		yield a
		a,b=b,a+b

c=0
x = fibo()
for i in x:
	print i
	c+=1
	if c>25: break


