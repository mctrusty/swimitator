# coding: utf-8
# swim_parser parses a shorthand language often used to notate swimming workouts
# it uses David Beazley's PLY parser to do the parsing 
# @author: Michael J. Cox

from ply import lex
from ply import yacc
from swim_lexer import tokens

def p_stroke(p):
	"""
	set : 
	set : count
	"""
	if len(p) == 1:
		p[0] = []
	else:
		p[0] = p[1] + [p[2]]
	
def p_count(p):
	"""
	count : NUMBER
	count : NUMBER MULT NUMBER
	"""
	if len(p) == 2:
		p[0] = p[1]
	elif len(p) == 4:
		p[0] = p[1] + p[2] + p[3]

parser = yacc.yacc()

while True:
	try: 
		s = raw_input('5 x 50')
	except EOFError:
		break
	if not s: continue
	result = parser.parse(s)
	print result
	