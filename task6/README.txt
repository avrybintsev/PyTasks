Infix operator realization 
--------------------------
Usage:

Ex.1: 'import codec' before running code with infix operator
Ex.2: 'import codec' in site.py
Ex.3: run ./task6_launcher.py to watch how task6_example.py works

"a op3 b op2 c op1 d" is processed as func1(func2(func3(a, b), c), d),
where func1 matches op1, func2 matches op2 etc.

brackets are currently not supported
--------------------------
Adding new operators:

1) Open infix.py
2) Define your own function with 2 parameters for new infix operator, 
e.g. "def newfun(a, b): \n  pass"
3) Change getOpDict() method, add new line before "return" statement:
"dictOp['your_op_name'] = your_func_name",
e.g. "dictOp['op4'] = newfun"
4) Save changes in infix.py