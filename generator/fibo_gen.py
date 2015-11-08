#! /usr/bin/env python

def fibo(n):
	a,b,c=0,1,0
	while (c<n):
		yield a
		a,b=b,a+b
		c=c+1

x = fibo(10)
for i in x:
	print i
