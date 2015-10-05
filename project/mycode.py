#!/usr/bin/python

import sys
import inspect
import md5
import os.path
import imp
import traceback

code_path = "/home/jishnu/Desktop/Jishnu-PythonWorks/project/1.py"

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

#jb = _initialization()
jb = load_module(sys.argv[1])
f1 = open(sys.argv[2], 'w')


'''
with open(sys.argv[1],"w") as f1:
    a=f1.read()
    b=f1.read() 
'''
def print_classes():
    for name, obj in inspect.getmembers(jb):
        if inspect.isclass(obj):
            #f1.write('paichi_the_found'
            f1.write('\n')
            f1.write("Class      Name ->  "+name)
            f1.write('\n')
            for N, O in inspect.getmembers(obj):
            	#f1.write(' --- Extra --- '
            	if inspect.isclass(O):
            		f1.write("      "+"SubClass      Name ->  "+N)
            		f1.write('\n')
            	if inspect.ismethod(O):
            		f1.write("      "+"SubMethod     Name ->  "+N)
            		f1.write('\n')
            	if inspect.isfunction(O):
            		f1.write("      "+"SubFunction   Name ->  "+N)
            		f1.write('\n')
        if inspect.ismethod(obj):
            #f1.write('paichi_the_found'
            f1.write('')
            f1.write('\n')
            f1.write("Method     Name ->  "+name)
            f1.write('\n')
        if inspect.isfunction(obj):
            #f1.write('paichi_the_found'
            f1.write('')
            f1.write('\n')
            f1.write("Function   Name ->  "+name)
            f1.write('\n')

print sys.argv[1]
print_classes()
#O_O()
f1.close()
