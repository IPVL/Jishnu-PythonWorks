#!/usr/bin/env python

def square(x):
	return x*x

print square(5)

def fibo(x):
	R = [0,1]
	for i in range(x-2):
		R.append(R[i]+R[i+1])
	return R
print fibo(10)

def void():
	return

x = void();
print x