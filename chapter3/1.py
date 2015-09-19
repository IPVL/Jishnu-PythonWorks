#!/usr/bin/env python
from math import pi
from string import Template

string1 = "Bangladesh %s %s homeland"
vau = ('is', 'our')
print string1 % vau

S = "The Life of Pi with 3 decimal values: %.3f"
print S % pi

S = "The Life of Pi with 50 decimal values: %.50f"
print S % pi

#template
S = Template('$x, say me $x!')
Z = S.substitute(x='hello')
print Z 	#Doesn't work

SS = Template("It's ${x}tastic")
ZZ = SS.substitute(x='fan')
print ZZ

SSS = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'scold anyone'
ZZZ = SSS.substitute(d)
print ZZZ

