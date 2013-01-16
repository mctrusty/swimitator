# coding: utf-8
# swim_lexer tokenizes a shorthand language often used to notate swimming workouts
# it uses David Beazley's PLY parser to do the lexing 
# @author: Michael J. Cox

from ply import lex

tokens = (
	"L_BRACKET",
	"R_BRACKET",
	"NUMBER",
	"MULT",
	"COLON",
	"AT",
	"ZONE"
)

t_ignore = r" \t"

def t_newline(t):
	r"\n"
	t.lexer.lineno += 1

t_AT = (r"@")

t_L_BRACKET = ( r"{")

t_R_BRACKET = ( r"}")

t_COLON = (r":")

t_MULT = (
	r"x|X"
)

t_ZONE = (
	r"EN|ZONE"
)

def t_NUMBER(t):
    r"\d+"
    t.value=int(t.value)
    return t

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

lex.lex()

wkout = """3 x { 
	2x50@1:00 
	EN1 100@2 
	}"""

lex.input(wkout)
for tok in iter(lex.token, None):
    print repr(tok.type), repr(tok.value)
    