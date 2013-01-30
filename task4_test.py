#!/usr/bin/python

import unittest
import operator
import types
from task4 import *

class test_task4(unittest.TestCase):

    def test_simple_cases(self):
        '''Test simple reduce use cases'''
	#self.assertRaises(IndexError, ireduce(None, []))
        test = ireduce(operator.add, [], 0)
        self.assertEqual(test.next(), 0)
        self.assertRaises(StopIteration, test.next)	

    def test_process(self):
        '''Test ireduce'''
        test = ireduce(operator.mul, [1, 2, 3, 4])
	self.assertEqual(test.next(), 1)
        self.assertEqual(test.next(), 2)
	self.assertEqual(test.next(), 6)
	self.assertEqual(test.next(), 24)
        self.assertRaises(StopIteration, test.next)

    def test_again(self):
        '''Test ireduce'''
        test = ireduce(operator.add, [1, 2, 3], 10)
	self.assertEqual(test.next(), 10)
	self.assertEqual(test.next(), 11)
        self.assertEqual(test.next(), 13)
	self.assertEqual(test.next(), 16)
        self.assertRaises(StopIteration, test.next)

if __name__ == '__main__':
    unittest.main()

