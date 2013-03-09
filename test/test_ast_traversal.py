import pdb
import sys
sys.path.append("..\\swimitator")

import swim_ast.node as node
from swim_ast.json_visitor import SwimJsonVisitor, SwimJsonCloseVisitor
import swim_ast.traversal as traversal
import swim_parser
import unittest

class TestJsonTraversal(unittest.TestCase):
	""" 
	Unit tests for traversal module.
	"""
	
	def setUp(self):
		self.parser = swim_parser.parser
		self.json_visitor = SwimJsonVisitor()
		self.json_close_visitor = SwimJsonCloseVisitor()
		
	def tearDown(self):
		self.parser = None
		json_visitor = None
		json_close_visitor = None
		
	def test_empty_set(self):
		self.fail("Need to figure out how to handle empties")
		
	def test_set_with_only_distance(self):
		"""
		Takes a set that is defined only by yards, e.g. 1000.
		Should return a json structure like:
		{ setlist: { set: { reps: 0, yards: 1000, zone: None, stroke: None}}}
		"""
		expected = '{"setlist": {"set": {"reps": 1, "distance": 1000, "stroke": null, "zone": null, "time": 0}}}'
		s = '1000'
		out = []
		result = self.parser.parse(s)
		traversal.json_traverse(result, self.json_visitor, self.json_close_visitor, out)
		actual = ''.join(out)	
		self.assertEqual(actual, expected)
	
if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestJsonTraversal)
	unittest.TextTestRunner(verbosity = 2).run(suite)