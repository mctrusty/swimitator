import sys
sys.path.append("..\\swimitator")

import swim_ast.node as node
import swim_parser
import unittest

class TestSwimParser(unittest.TestCase):
    """Unit tests for swim_parser"""
    
    def setUp(self):
        self.parser = swim_parser.parser

    def cleanUp(self):
        self.parser = None
        
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
        self.assertIsInstance(res.children[0], node.MultiSet)

    def test_kick_set(self):
        """
        Check to see that a kick set creates the correct object
        """
        s = "2x100 K @1:00"
        res = self.parser.parse(s)
        kick = res.get_all_sets()[0].children[1]
        self.assertIsInstance(kick, node.Kick)
        
    def test_zone_entry(self):
        """
        Check to see that entering a zone creates a zone object
        """
        s = "10x50 fly EN3 @1"
        res = self.parser.parse(s)
        zone = res.get_all_sets()[0].children[2]
        self.assertIsInstance(zone, node.Zone)

    def test_interval_entry(self):
        """
        Check to see that entering an interval creates an Interval
        node object
        """
        s = "10x50 fly EN3 @1:30"
        res = self.parser.parse(s)
        interval = res.get_all_sets()[0].children[3]
        self.assertIsInstance(interval, node.Interval)

    def test_multiple_children_in_multi_set(self):
        """
        Check to see that multiple children can be added to a
        multiple set
        """
        s = "2 x {3 x 50 fly @1:00 2 x 50 K @1:00}"
        res = self.parser.parse(s)
        sets = res.get_all_sets()[0].children
        self.assertEqual(len(sets[0].children), 2)
    
    def test_missing_distance(self):
        """
        Check that a missing distance field throws an error
        """
        s = "2x kick"
        self.assertRaises(TypeError, self.parser.parse, s)

    def test_empty_distance_at_string_end(self):
        """
        Check that an empty ditance value at the end of a string
        raises a Missing Token error
        """
        s = "2x "
        with self.assertRaises(TypeError) as err:
            self.parser.parse(s)

        the_exception = err.exception
        self.assertEqual(the_exception[0], 'Token Missing')
        

    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSwimParser)
    unittest.TextTestRunner(verbosity=2).run(suite)
