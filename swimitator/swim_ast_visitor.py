class SwimAstVisitor():
    """
    Base class for visitor to traverse language parsed by the
    swimitator swim_parser.
    """

    def visit_Node(self, node):
        """
        Visit the base Node instance.
        """
        print "visiting " + node.type
        
