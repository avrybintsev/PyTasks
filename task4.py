#!/usr/bin/python

def ireduce(function, iterable, initial = None):
    '''
       ireduce(function, iterable[, initial]): returns generator
       applies specified function to pair of elements from left to right on each step
       for one element returns this value or initial value
       Ex: ireduce(function, [a b c d]): function(function(function(a, b), c), d)
    '''

    iterator = iter(iterable)

    if initial is None:
        try:
            initial = next(iterator)
        except StopIteration:
            raise IndexError('Illegal ireduce call')

    yield initial

    result = initial
    for item in iterator:
        result = function(result, item)
        yield result