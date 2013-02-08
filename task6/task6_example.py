#!/usr/bin/python
# coding: my_infix_codec

#
# Usage examples 
# Ex.1: 'import codec' before running this code 
# Ex.2: add 'codec' code to site.py
# Ex.3: run ./task6_launcher.py
#

a = 2
b = 3

# test case 1: func1(a, b)
c = a op1 b 

# test case 2: func2(a, b)
d = a op2 b

# test case 3: func1(func1(a, b), c)
e = a op1 b op1 c

# test case 4: func1(func2(func2(a, b), c), e)
f = a op2 b op2 c op1 e

# test case 5: func1(func2(func3(a, b), c), d)
g = a op3 b op2 c op1 d

# 2 3 5 6 10 40 46
print a, b, c, d, e, f, g
