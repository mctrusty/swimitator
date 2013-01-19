# coding: utf-8
# swim_parser parses a shorthand language often used to notate swimming workouts
# it uses David Beazley's PLY parser to do the parsing 
# @author: Michael J. Cox

from ply import lex
from ply import yacc
from swim_lexer import tokens

class Node:
	def __init__(self, type, children=None, leaf=None):
		self.type = type
		if children:
			self.children = children
		else:
			self.children = []
		self.leaf = leaf
		
	def __repr__(self):
		return "Set info %s" % (self.children)

def p_set(p):
	"""
	set : 
	set : count skill
	"""
	if len(p) == 1:
		p[0] = []
	else:
		p[0] = Node("set",[p[1] ,p[2]])
	
def p_count(p):
	"""
	count : NUMBER
			 | NUMBER MULT NUMBER
	"""
	if len(p) == 2:
		p[0] = (1,p[1])
	elif len(p) == 4:
		p[0] = (p[1] ,p[3])

def p_skill(p):
	"""
	skill : DRILL
	"""
	if len(p) == 3:
		p[0] = (p[1],[p2])
	else:
		p[0] = (p[1],'')

def p_error(p):
	raise TypeError("Unknown Text '%s'" % (t.value,))

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
	