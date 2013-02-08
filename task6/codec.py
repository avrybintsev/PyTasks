import codecs, cStringIO, encodings, inspect
from encodings import utf_8
from infix import *

codec_name = 'my_infix_codec'

# replace in right order (use ())
# import fund code

def translate(lines):

    op = getOpDict()
    cd = []
    for key, value in op.iteritems():
	codes = inspect.getsourcelines(value)[0]
        func = ' '.join(codes)
	cd.append(func)
    fc = '\n'.join(cd)

    result = fc

    for line in lines:	

	temp = line
	finished = False
	while not finished:
	    finished = True
	    parts = temp.split()
	    for index in xrange(0, len(parts)):
	        part = parts[index]
	        if (part in op.keys()) and (index in xrange(1, len(parts)-1)):
		       lop = parts[index-1]
		       rop = parts[index+1]
		       rpl = op[part].__name__+'('+lop+','+rop+')'
		       finished = False
		       
		       parts[index-1] = ''
		       parts[index] = rpl
		       parts[index+1] = ''
		       temp = ' '.join(parts)
		       break

        result += (temp + '\n')
    return result

class StreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kwargs):
	codecs.StreamReader.__init__(self, *args, **kwargs)
	lines =	self.stream.readlines()
	data = translate(lines)
	self.stream = cStringIO.StringIO(data)

def search_function(codec_string):
    if codec_string != codec_name: 
       return None

    utf8 = encodings.search_function('utf8') 
    return codecs.CodecInfo(
           name=codec_name, 
           encode=utf8.encode, 
           decode=utf8.decode, 
           incrementalencoder=utf8.incrementalencoder,  
           incrementaldecoder=utf8.incrementaldecoder, 
           streamreader=StreamReader, 
           streamwriter=utf8.streamwriter
           )

codecs.register(search_function)
