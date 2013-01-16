# coding: utf-8
from ply import lex
tokens = (
	"SYMBOL",
	"COUNT"
)
t_SYMBOL = (
	r"{|}|x|X"
)
def t_COUNT(t):
    r"\d+"
    t.value=int(t.value)
    return t
def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))
lex.lex()
wkout = "{2x50}"
lex.input(wkout)
for tok in iter(lex.token, None):
    print repr(tok.type), repr(tok.value)
    