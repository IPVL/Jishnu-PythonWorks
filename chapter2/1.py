#!/usr/bin/env python

jb = [1,2,3,4,5]
jj = [6,7,8,9,0]
print jb 
print 'hello world'

jb = ['jishnu', 'sust', 2010331032]
ash = ['ashraful', 'sust', 2010331035]
fahad = ['fahad', 'sust', 2010331037]
sakal = ['sakal', 'buet', 10331029]
database = [jb,ash,fahad,sakal]

print database


string = 'Hello World'
print string[1]
print string[-1]
print string[-5]
print string[-6]

fourth = raw_input("String : ")[3]
print fourth

O_O = 3*[1,2,3]
print O_O

#date print code

last_word = [' ']+['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']
D = raw_input("Day : (1-31) ");
month_name = [' ','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
M = raw_input("Month : (1-12) ")
Y = raw_input("Year: ")

print D+last_word[int(D)]+' '+month_name[int(M)]+', '+Y