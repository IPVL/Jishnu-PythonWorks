#!/usr/bin/env python

from sys import argv

#script, "input1.txt" = argv

output1 = open("input1.txt", 'w')

output1.write("line1")
output1.write("\n")
output1.write("line2")
output1.write("\n")
output1.write("line3")
output1.write("\n")

print 'truncating ... '
output1.truncate()
#output1.close()

line1 = "Jishnu Banerjee"
line2 = "Ashraful Islam"
line3 = "Fahad Hasan"

print 'going to write ... '

output1.write(line1)
output1.write("\n")
output1.write(line2)
output1.write("\n")
output1.write(line3)
output1.write("\n")

#output1.close()
#output1.open()
#output1.readline()

output1.close()
