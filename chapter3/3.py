#!/usr/bin/env python
from string import maketrans

#Find
print 'Start, The Shuru -> Find'
S = 'laskdfhgaslkjdbgasjklfhga;sjklgh'
print S.find('dfh')
print S.find('dfg')
S = 'abc abc abc';
print S.find('abc')
print S.find('abc',1)
print S.find('abc', 1,3)

#Join
print 'Start, The Shuru -> Join'
sep = ['1','2','3','4','5']
seq = '+'
print seq.join(sep)

#lower title replace split strip translation
print 'Start, The Shuru -> lower - title - replace - split - strip - translation'
print 'YABSfsdghYASDGfksdhb'.lower()
print 'Haks jsdU jUUU JnJnur'.title()
print "this is a test".replace('teSt'.lower(), 'Sudden test')
print "this is a test".replace('text', 'Sudden test')
print '1+2+3+4+5'.split('+')
print 'default splitting technique'.split()
print '  sdgf sdegt segt  '.strip()
table = maketrans('cs','kz')
print "this is an incredible test".translate(table);
print "this is an incredible test".translate(table, 'n');  #deletes all 'n'