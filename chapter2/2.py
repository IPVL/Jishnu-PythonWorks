#!/usr/bin/env python

#slicing

country = 'my homeland bangladesh is a beautiful country'
print country[12:22]

number = [0,1,2,3,4,5,6,7,8,9]
print number[:]
print number[:5]
print number[5:]
print number[-3:]
print number[:-2]
print number[-3:-1]

#Like Loop

print number[::2]
print number[-20::3]

str = 'beautiful'+'bangladesh'
print str

#Membership

S = ['asd','fgh','jkl']
print 'asd' in S
print 'bangladesh' in country
print 'sadgas' in country
print "--> Here"
#print sdfkljg in country
print "--> There"
print 'desh' in raw_input("Name : ")

data = [['jb',27],['ash',26],['fahad',28]]
name = raw_input("Name: ")
userid = raw_input("User ID : ")

print [name,int(userid)] in data
print data
