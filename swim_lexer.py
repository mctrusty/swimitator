# coding: utf-8
# swim_lexer tokenizes a shorthand language often used to notate swimming workouts
# it uses David Beazley's PLY parser to do the lexing 
# @author: Michael J. Cox

from ply import lex

tokens = (
    "L_BRACKET",
    "R_BRACKET",
    "KICK",
    "DRILL",
    "STROKE",
    "OTHER",
    "NUMBER",
    "MULT",
    "COLON",
    "AT",
    "ZONE"
)

t_ignore = ' \t'

def t_newline(t):
	r"\n"
	t.lexer.lineno += len(t.value)
	
t_AT = (r"@")

t_L_BRACKET = ( r"{")

t_R_BRACKET = ( r"}")

t_COLON = (r":")

t_MULT = (
    r"x|X"
)

t_KICK = ( r"[Kk](ick)?")

t_DRILL = ( r"[Dd]r(ill)?")

t_STROKE = ( r"[Cc]h(oice)?|[Ff]ly?|[Bb]r(east)?|[Bb](a|k)(ck)?|[Ff]r(ee)?")

t_ZONE = (
    r"(EN|ZONE)\s?\d+"
)

def t_NUMBER(t):
    r"\d+"
    t.value=int(t.value)
    return t

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))
    
lex.lex()

if __name__ == "__main__":
	wkout = """3 x { 
		2x50 fr @1:00 
		1x100 drill @2 
		}
		10 x 100 K EN3 @1:30
	"""
	lex.input(wkout)	
	for tok in iter(lex.token, None):
		print repr(tok.type), repr(tok.value)