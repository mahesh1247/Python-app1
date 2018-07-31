#!/usr/bin/python
import sys



import bottle
import hello


import os, sys



os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))
print "Hello, World!"
try:
    application = bottle.default_app()
    print "Intialization Succefull"
except:
    print (' Got error %s'%(traceback.format_exc().splitlines()[-1]))
