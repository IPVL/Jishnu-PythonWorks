#!/usr/bin/env python

arr = [0,1,2,3,4,5,6,7,8,9]
print min(arr)
print max(arr)
print len(arr)
print min(1,5,8,96,-6)
print max(1,5,85,2,4,45,10)

a = list('hello')
print a
arr[3]=123
print arr
del arr[3]
print arr
arr[:3] = [0,1,200]
print arr
arr[2:2]=['a','b','c','d']
print arr
arr[2:5] = []
print arr

array = [1,2,3]
array.append(1234);
print array
print arr.count(9)

_new = [[1,2],3,4,4,[[5,6],[1,2]]]
print _new.count(4)
print _new.count([1,2])

array.extend([4,5,6])
print array

#extend function just modifies a list
#doesn't return anything

a = [1,2,3]
b = [4,5,6]
a[len(a):]=b
print a

have_fun = 'haveFunF'
print have_fun[4]
print have_fun.index('F')

#in case, same attributes repeat
#index function always output the first one

x = [1,2,3,4,5,6]
x.insert(3,3)
print x
x[3:3] = [3]
print x