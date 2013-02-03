# coding: utf-8
# swim_parser parses a shorthand language often used to notate swimming workouts
# it uses David Beazley's PLY parser to do the parsing 
# @author: Michael J. Cox

from ply import lex
from ply import yacc
from swim_lexer import tokens
from Node import *

def p_workout(p):
        """
        set_list : empty
	set_list : set_list set
        set_list : set_list multi_set
	"""
        if len(p) == 2:
                p[0] = SetList()
        else:
                p[0] = p[1].add_set(p[2])

def p_set_list(p):
	"""
	set_list : set
                 | multi_set
	"""
	p[0] = SetList(p[1])

def p_super_set(p):
        """
        multi_set : NUMBER MULT L_BRACKET set_list R_BRACKET
        """

        p[0] = MultiSet(p[4],p[1])

def p_set(p):
	"""
	set : count skill zone interval
	    | count kick zone interval
	"""
	if len(p) == 1:
		p[0] = []
	else:
		p[0] = Set([p[1] ,p[2], p[3],p[4]])
        
def p_empty(p):
	'empty :'
	pass
	
def p_count(p):
	"""
	count : NUMBER
	      | NUMBER MULT NUMBER
	"""
	if len(p) == 2:
		p[0] = Count(1,p[1])
	elif len(p) == 4:
		p[0] = Count(p[1] ,p[3])

def p_skill_stroke(p):
	"""
	skill : empty 
	      | STROKE
	"""
	if len(p) == 2:
		p[0] = Stroke(p[1])
	else:
		p[0] = Stroke('choice')
		
def p_skill_drill(p):
	"""
	skill : DRILL
	      | STROKE DRILL
	"""
	if len(p) == 3:
		p[0] = Drill(p[1],p[2])
	else:
		p[0] = Drill('choice',p[1])

def p_kick(p):
	"""
	kick : KICK
	     | STROKE KICK
	"""
	if len(p) == 3:
		p[0] = Kick(p[1])
	else:
		p[0] = Kick('choice')
		
def p_zone(p):
	"""
	zone : ZONE
	     | empty
	"""
	if len(p)==2:
		p[0] = Zone(p[1])
	else:
		p[0] = 'none'
	
def p_interval(p):
	"""
	interval : AT NUMBER COLON NUMBER
		 | AT NUMBER
		 | empty
	"""
	if len(p) == 5:
		p[0] = Interval(p[2],p[4])
	elif len(p) == 3:
		p[0] = Interval(0,p[2])
	else:
		p[0] = Interval(0,0)
		
def p_error(p):
	raise TypeError("Unknown Text '%s'" % (t.value,))

parser = yacc.yacc(debug=True)

if __name__ == "__main__":
        import logging
        logging.basicConfig(
                level = logging.DEBUG,
                filename="parselog.txt",
                filemode="w",
                format="%(filename)10s:%(lineno)4d:%(message)s",
        )
        log = logging.getLogger()

        while True:
                try: 
                        s = raw_input('set>')
                except EOFError:
                        break
                if not s: continue
                if s=='q':
                        break
                result = parser.parse(s,debug=log)
                print result
	
