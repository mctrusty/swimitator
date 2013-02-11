import sys
sys.path.append("..\\swimitator")

import swim_ast.node as node
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
        self.assertEqual(isinstance(res, node.SetList), True)
        self.assertEqual(res.children, [])

    def test_simple_set(self):
        """
        Check to see that a basic set returns a SetList object and
        returns the correct number of reps and distance
        """
        s = "10 x 100"
        res = self.parser.parse(s)
        self.assertTrue(isinstance(res, node.SetList))

        child = res.get_all_sets()[0].children[0]
        expected = node.Count(10,100)

        self.assertEqual(child.reps,expected.reps)
        self.assertEqual(child.distance, expected.distance)

    def test_nested_set(self):
        """
        Check to see that a nested set returns a multiset object
        """
        s = "2x{10x100 fly @2:00}"
        res = self.parser.parse(s)
        self.assertTrue(isinstance(res.children[0], node.MultiSet))

    def test_no_distance(self):
        """
        Check that a missing distance field throws an error
        """
        s = "2x fr"
        with self.assertRaises(TypeError):
            self.parser.parse(s)
        #self.assertRaises(TypeError, self.parser.parse, s)
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSwimParser)
    unittest.TextTestRunner(verbosity=2).run(suite)
