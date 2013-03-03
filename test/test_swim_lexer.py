import sys
sys.path.append("..\\swimitator")

import swim_lexer
import unittest

class TestSwimLexer(unittest.TestCase):
	'''Unit tests for swim_lexer'''
	
	def setUp(self):
		self.lexer = swim_lexer.lexer

	def tearDown(self):
		self.lexer = None
		
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSwimLexer)
    unittest.TextTestRunner(verbosity=2).run(suite)