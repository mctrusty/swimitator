import swim_parser
import swim_ast.traversal as traversal
from swim_ast.xml_visitor import SwimXmlVisitor, SwimXmlCloseVisitor

def get_xml(workout):
    p = swim_parser.parser
    res = p.parse(workout)
    sv = SwimXmlVisitor()
    cv = SwimXmlCloseVisitor()
    out = []
    
    traversal.xml_traverse(res, sv, cv, out)
    return out
