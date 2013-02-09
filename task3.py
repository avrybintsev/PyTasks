#!/usr/bin/python

class myxrange(object):

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0

        if step == 0:
            raise ValueError("myxrange ValueError: step can't equals zero")         

        self.start = int(start)
        self.stop = int(stop)
        self.step = int(step)

    def __len__(self):
        if self.step > 0:
	    length = (self.stop - self.start) // self.step
	    addict = (self.stop - self.start) % self.step	    
        else:
	    length = (self.start - self.stop) // abs(self.step)
	    addict = (self.start - self.stop) % abs(self.step)
	result = addict and length+addict or length
	if result < 0:
	    return 0
	return result

    def __repr__(self):
        return 'myxrange(%s, %s, %s)'%(self.start, self.stop, self.step)

    def __iter__(self):
	self.position = self.start
        return self

    def next(self):
	if self.step > 0:
           if self.position >= self.stop:
              raise StopIteration
           else:
              result = self.position
              self.position += self.step
              return result
	else:
	   if self.position <= self.stop:
              raise StopIteration
           else:
              result = self.position
              self.position += self.step
              return result

    def __getitem__(self, index):
        if not isinstance(index, slice):
	   start = self.start if (index >= 0) else self.stop
           element = start + index * self.step
           if element in list(self):
	      return element 
	   else:
	      raise IndexError('myxrange IndexError: bad index')
	else:
	    start = index.start
            stop = index.stop
	    step = index.step

	    if step == None:
		step = 1
            if step == 0:
                ValueError("myxrange ValueError: slice step can't equals zero")

            if start == None:
		if step > 0:
                    start = 0  
		else:
		    start = len(self)-1
            if stop == None:
		if step > 0:
                    stop = len(self) 
		else:
		    stop = -1

            return myxrange(
			self.start + self.step * start, 
			self.start + self.step * stop, 
			self.step * step
			   )
