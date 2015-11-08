#! /usr/bin/env python

def fibo():
	a,b=0,1
	while 1:
		yield a
		a,b=b,a+b

def gen(IT, n):
	for i in range(n):
		yield IT.next()

print list(gen(fibo(), 25))
