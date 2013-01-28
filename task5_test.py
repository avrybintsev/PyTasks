#!/usr/bin/python

from task5 import *
import unittest

class test_task5(unittest.TestCase):
    def test_eratosthenes(self):
        '''Test Sieve of Eratothenes'''
        self.assertEqual(eratosthenes(1),[])
	self.assertEqual(eratosthenes(2),[2])
	self.assertEqual(eratosthenes(17),[2,3,5,7,11,13,17])
	dump = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293 ]
	self.assertEqual(eratosthenes(300), dump)
	self.assertEqual(eratosthenes(294), dump)
	dump = dump[:-1]
	self.assertEqual(eratosthenes(292), dump)

if __name__ == '__main__':
    unittest.main()
