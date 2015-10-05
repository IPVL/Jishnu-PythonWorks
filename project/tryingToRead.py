#!/usr/bin/env python

f = open('input1', 'r+')
print f.read(2)
print f.read(2)
print f.read(6)
f.close()
f = open('input1', 'r+')
print ' -- '
print f.read(2)
f.seek(5)
print f.read(2)
f.close()
f = open('input1', 'r+')
jb = f.read()
#jb = f.open()
f1 = open('output1', 'w')
f1.write(jb)