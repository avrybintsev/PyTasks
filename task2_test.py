#!/usr/bin/python

from task2 import *
import unittest

var = 0

def decor1(f):
    global var
    var += 1
    print 'decor1 started'
    def tmp(*args, **kwargs):
        print 'decor1'
        f(*args, **kwargs)
    return tmp

@lazy_decorator
def decor2(f):
    global var
    var += 1
    print 'decor2 started'
    def tmp(*args, **kwargs):
        print 'decor2'
        f(*args, **kwargs)
    return tmp

@decor1
def func1():
    print 'func1'

@decor2
def func2():
    print 'func2'

class test_task2(unittest.TestCase):

   def test_lazy(self):
       '''Test lazy decorator'''
       global var
       self.assertEqual(var, 1)
       print 'in test'
       func1()
       func2()
       self.assertEqual(var, 2)

if __name__ == '__main__':
    unittest.main()

