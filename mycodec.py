import codecs, cStringIO, encodings, tokenize
from encodings import utf_8

op_name = 'infix_op_example'
op_subst = '+'
codec_name = 'my_infix_codec'

def translate(readline):
    for type, name,_,_,_ in tokenize.generate_tokens(readline):
        if type == tokenize.NAME and name == op_name:
            yield tokenize.OP, op_subst
        else:
            yield type, name

class StreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kwargs):
        codecs.StreamReader.__init__(self, *args, **kwargs)
        data = tokenize.untokenize(translate(self.stream.readline))
	self.stream = cStringIO.StringIO(data)

def search_function(s):
    if s != codec_name: 
       return None
    utf8 = encodings.search_function('utf8') 
    return codecs.CodecInfo(name=codec_name, encode=utf8.encode, decode=utf8.decode, incrementalencoder=utf8.incrementalencoder, incrementaldecoder=utf8.incrementaldecoder, streamreader=StreamReader, streamwriter=utf8.streamwriter)

codecs.register(search_function)
