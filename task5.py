eratosthenes = lambda k: filter( lambda x: x not in [n*q for q in xrange(2,int(k ** 0.5 + 1)+1) for n in xrange(2, k//q+1)], xrange(2,k+1) )
