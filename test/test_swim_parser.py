import sys
sys.path.append("..\\swimitator")

import Node
import swim_parser
import unittest

class TestSwimParser(unittest.TestCase):
    """Unit tests for swim_parser"""
    
    def setUp(self):
        self.parser = swim_parser.parser
        
    def test_empty_set(self):
        """
        Check to see that an empty string generates a set_list with no
        child sets
        """
        s = ""
        res = self.parser.parse(s)
        self.assertEqual(isinstance(res, Node.SetList), True)
        self.assertEqual(res.set_list, [])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSwimParser)
    unittest.TextTestRunner(verbosity=2).run(suite)
