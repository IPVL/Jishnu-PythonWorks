#!/usr/bin/env python

name = 'jb'

while not name:
	name = raw_input('')
	print 'Y or N?'
print name + ', good luck!'

alpha = ['a','b','c','d','e','f']
for x in alpha:
	print x

print range(1,10)
print range(10)

for i in range(15):
	print i

dictonary = {'jb':32, 'ash':35, 'fahad':37}
for aVeryRandomIterator in dictonary:
	print aVeryRandomIterator ,' = ',dictonary[aVeryRandomIterator]

#zip function
A = [1,2,3,4]
B = [5,6,7,8]
zip(A,B)
for i,j in zip(A,B):
	print i,j
 #C = zip(A,B)
 #print zip(A,B)


for i,j in zip(range(10),range(100)):
 	print i,j

string = 'ksdfhgkjlashgklajshg'
for X in string:
	print X
	if 'k' in X:
		print 'qwerty'

while True:
	word = raw_input('Word: ')
	if not word: break
	print '--->',word

#del
x=[1,2,3,4]
y=x
del x
#print x
print y
