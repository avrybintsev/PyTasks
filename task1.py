#!/usr/bin/python

def curry(f, *a, **kw):

    default = f.func_code.co_argcount
    current = len(a) + len(kw)

    if current >= default:
	return f(*a, **kw)
    else:
        def inf(*fa, **fkw):
            return curry(f, *(a+fa), **dict(kw, **fkw))
        return inf
