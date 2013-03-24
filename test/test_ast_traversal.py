import pdb
import sys
sys.path.append("..\\swimitator")

import swim_ast.node as node
from swim_ast.xml_visitor import SwimXmlVisitor, SwimXmlCloseVisitor
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
        self.json_visitor = None
        self.json_close_visitor = None
        expected = ''
        
    def test_empty_set(self):
        s = ''
        with self.assertRaises(Exception) as exc:
            res = self.parser.parse(s)

        the_exception = exc.exception
        self.assertEqual(the_exception[0], 'Empty Input')
        
    def test_set_with_only_distance(self):
        """
        Takes a set that is defined only by yards, e.g. 1000.
        Should return a json structure like:
        { setlist: { set: { reps: 0, yards: 1000, zone: None, stroke: None}}}
        """
        s = '1000'
        result = self.parser.parse(s)
        actual = traversal.json_traverse(result, self.json_visitor, self.json_close_visitor, [])
        expected = '{"setlist": [{"reps": 1, "distance": 1000, "stroke": null, "zone": null, "time": 0}]}'
        self.assertEqual(actual, expected)

    def test_multi_set(self):
        """
        Test a multiset (e.g 2 x {1 x 50 ... } 
        """
        s = '2 x {2 x 100 fr @1:20 2 x 100 IM @1:30}'
        result = self.parser.parse(s)
        actual = traversal.json_traverse(result, self.json_visitor, self.json_close_visitor, [])
        expected = '{"setlist": [{"reps": 2, "setlist": [{"reps": 2, "distance": 100, "stroke": "fr", "zone": null, "time": 80}, {"reps": 2, "distance": 100, "stroke": "IM", "zone": null, "time": 90}]}]}'
        self.assertEqual(actual, expected)
        
class TestXmlTraversal(unittest.TestCase):
    """ 
    Unit tests for traversal module.
    """
    
    def setUp(self):
        self.parser = swim_parser.parser
        self.xml_visitor = SwimXmlVisitor()
        self.xml_close_visitor = SwimXmlCloseVisitor()
        
    def tearDown(self):
        self.parser = None
        self.xml_visitor = None
        self.xml_close_visitor = None
        
    def test_empty_set(self):
        s = ''
        with self.assertRaises(Exception) as exc:
            res = self.parser.parse(s)

        the_exception = exc.exception
        self.assertEqual(the_exception[0], 'Empty Input')
        
    def test_set_with_only_distance(self):
        """
        Takes a set that is defined only by yards, e.g. 1000.
        """
        expected = '''<setlist xmlns="http://swimparser.appspot.com/xml">
<set>
<count>
<reps>1</reps>
<distance>1000</distance>
</count>
<stroke></stroke>
<zone></zone>
<time>0</time>
</set>
</setlist>'''
        s = '1000'
        out = []
        result = self.parser.parse(s)
        traversal.xml_traverse(result, self.xml_visitor, self.xml_close_visitor, out)
        actual = '\n'.join(out) 
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase([TestJsonTraversal, TestXmlTraversal])
    unittest.TextTestRunner(verbosity = 2).run(suite)
        
