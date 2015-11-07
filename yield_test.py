#! /usr/bin/env python

def jis():
	yield 'A'
	yield 'B'
	yield 'C'
	yield 'D'

a = jis()

the_list = [i for i in a]
for i in the_list:
	print i
