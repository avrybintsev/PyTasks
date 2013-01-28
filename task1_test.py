#!/usr/bin/python

from task1 import *
import unittest

@curry
def sum5(a, b, c, d, e):
    return a + b + c + d + e

class test_task1(unittest.TestCase):

   def test_sum5(self):
       '''Test sum5 function'''
       self.assertEqual(sum5(0,0,0,0,0),0)
       self.assertEqual(sum5(1,1,1,1,1),5)
       self.assertEqual(sum5(1,2,3,4,5),15)

   def test_curry(self):
       '''Test curry decorator on sum5 function'''
       self.assertEqual(sum5(1,2,3,4,5), sum5(1,2,3,4,5))
       self.assertEqual(sum5(1,2,3,4,5), sum5(1,2,3,4)(5))
       self.assertEqual(sum5(1,2,3,4,5), sum5(1,2,3)(4,5))
       self.assertEqual(sum5(1,2,3,4,5), sum5(1,2)(3,4,5))
       self.assertEqual(sum5(1,2,3,4,5), sum5(1)(2,3,4,5))
       self.assertEqual(sum5(1,2,3,4,5), sum5(1,2,3)(4)(5))
       self.assertEqual(sum5(1,2,3,4,5), sum5(1,2)(3)(4,5))
       self.assertEqual(sum5(1,2,3,4,5), sum5(1)(2)(3,4,5))
       self.assertEqual(sum5(1,2,3,4,5), sum5(1)(2)(3)(4)(5))

if __name__ == '__main__':
    unittest.main()
