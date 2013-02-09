#!/usr/bin/python

from task3 import *
import unittest


class test_task3(unittest.TestCase):

   def test_len_myxrange(self):
       for i in [0, 1, 2, 3, 4, 5, 10, 20, 100, 1000, 1001]:
           self.assertEqual(len(myxrange(i)), len(xrange(i)))

   def test_myxrange(self):   
       for i in [0, 1, 2, 3, 4, 5, 10, 20, 100, 1000, 1001]:    
           self.assertEqual(list(myxrange(i)), list(xrange(i)))
       self.assertEqual(list(myxrange(2, 9)), list(xrange(2, 9)))
       self.assertEqual(list(myxrange(2, 10)), list(xrange(2, 10)))

   def test_myxrange_step(self):
       for i in [1, 2, 3]:
           self.assertEqual(list(myxrange(2, 10, i)), list(xrange(2, 10, i)))

   def test_myxrange_negstep(self):
       for i in [-1, -2, -3]:
           self.assertEqual(list(myxrange(10, 2, i)), list(xrange(10, 2, i)))

   def test_myxrange_get(self):
       self.assertEqual(myxrange(2, 10, 2)[0], 2)
       self.assertEqual(myxrange(2, 10, 2)[1], 4)
       self.assertEqual(myxrange(2, 10, 2)[-2], 6)
       self.assertEqual(myxrange(2, 10, 2)[-1], 8)

   def test_myxrange_neg(self):
       self.assertEqual(list(myxrange(2, -10, -2)), [2,0,-2,-4,-6,-8])
       self.assertEqual(list(myxrange(2, -10, -2)), list(xrange(2, -10, -2)))

   def test_myxrange_slice(self):       
       self.assertEqual(myxrange(2, 10, 2)[1:][0], 4)
       self.assertEqual(myxrange(2, 10, 2)[1:][-2], 6)
       self.assertEqual(myxrange(2, 10, 2)[::-1][0], 8)

if __name__ == '__main__':
    unittest.main()


