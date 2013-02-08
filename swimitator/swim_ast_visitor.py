from Node import *

class SwimAstVisitor():
    """
    Base class for visitor that processes language parsed by the
    swimitator swim_parser.
    """

    def visit(self, node):
        """
        Visit the base Node instance.
        """
        if isinstance(node, Set):
            self.visit_Set(node)
        if node.type:
            print "visiting " + node.type
            
    def visit_Set(self, set):
        print "<set>"        

        
        
    
