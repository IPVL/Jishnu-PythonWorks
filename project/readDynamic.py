# Links : 
#       1. http://code.davidjanes.com/blog/2008/11/27/how-to-dynamically-load-python-code/
#       2. http://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python
#

#!/usr/bin/python

import sys
import md5
import os.path
import imp
import traceback

code_path = '/home/jishnu/Desktop/Jishnu-PythonWorks/project'

def load_module(code_path):
    try:
        try:
            code_dir = os.path.dirname(code_path)
            code_file = os.path.basename(code_path)

            fin = open(code_path, 'rb')

            return  imp.load_source(md5.new(code_path).hexdigest(), code_path, fin)
        finally:
            try: fin.close()
            except: pass
    except ImportError, x:
        traceback.print_exc(file = sys.stderr)
        raise
    except NameError:
        traceback.print_exc(file = sys.stderr)
        raise
    except IOError:
        traceback.print_exc(file = sys.stderr)
        raise

m = load_module("1.py")
#print m.__dict__

import sys, inspect
def print_classes():
    for name, obj in inspect.getmembers(m):
        if inspect.isclass(obj):
            print 'paichi_the_found'
            print "Class      Name ->  "+name
            #print obj.__doc__
            #print(obj)
        if inspect.ismethod(obj):
            print 'paichi_the_found'
            print "Method     Name ->  "+name
        if inspect.isfunction(obj):
            print 'paichi_the_found'
            print "Function   Name ->  "+name


ZZ = print_classes()
ZZ()

# clsmembers = inspect.getmembers(m, inspect.isclass)
# print clsmembers
