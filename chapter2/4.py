#!/usr/bin/env python

print "Start, The Shuru -> Pop Portion"
#pop
a=[0,1,2,3,4,5,6,7,8,9]
print a
a.pop()
print a
a.pop(0)
print a
a.pop(3)
print a
a.append(a.pop(0))
print a
a=[0,1,2,3,4,5,6,7,8,9]

print "Start, The Shuru -> Remove Portion"
#remove
a.remove(4)
print a
a[3:3]=[4,4,4,4,4]
print a
a.remove(4)
print a
a.remove(4)
print a
a.remove(4)
print a
a.remove(4)
print a

print "Start, The Shuru -> Reverse Portion"
#reverse
a.reverse()
print a
a.reverse()
print a
string = "sustenam"
print reversed(string) 		#doesn't work
print list(reversed(string))

#sort
print "Start, The Shuru -> Sort Portion"
b = [1,5,2,4,0,3,9,8,6,7]
print b
b.sort();
print b
b.reverse();
print b
c = sorted(b)
print c

#doesn't return any function
#just modifies the array

S = ['sdgjdagsjsdgj','asd','dfhgdfh','erty']
S.sort();
print S
S.sort(key=len)
print S
S.sort(reverse=True)
print S
