# coding: utf-8
# swim_parser parses a shorthand language often used to notate swimming workouts
# it uses David Beazley's PLY parser to do the parsing 
# @author: Michael J. Cox

import pdb
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
		p[0] = p[1] 
	
def p_count(p):
	"""
	count : NUMBER
			 | NUMBER MULT NUMBER
	"""
	pdb.set_trace()
	if len(p) == 2:
		p[0] = (1,p[1])
	elif len(p) == 4:
		p[0] = (p[1] ,p[3])

import logging
logging.basicConfig(
	level = logging.DEBUG,
	filename="parselog.txt",
	filemode="w",
	format="%(filename)10s:%(lineno)4d:%(message)s",
)
log = logging.getLogger()
parser = yacc.yacc(debug=True)

while True:
	try: 
		s = raw_input('set>')
	except EOFError:
		break
	if not s: continue
	result = parser.parse(s,debug=log)
	print result
	