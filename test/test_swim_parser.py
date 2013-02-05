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

    def test_simple_set(self):
        """
        Check to see that a basic set returns a SetList object
        """
        s = "10 x 100"
        res = self.parser.parse(s)
        self.assertTrue(isinstance(res, Node.SetList))

        child = res.get_all_sets()[0].children[0]
        expected = Node.Count(10,100)

        #have to cast child and expected to strings right now bc
        #comparing 2 different objects, albeit with the same exact
        #values results in a fail. Might look at overriding the object
        #hashing methods at some point to change that.
        self.assertEqual(str(child),str(expected))
        
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSwimParser)
    unittest.TextTestRunner(verbosity=2).run(suite)
