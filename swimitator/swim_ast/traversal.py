#!/usr/bin/python

# Copyright 2013 Michael J. Cox

"""
A set of methods for traversing n-ary trees.

* **traverse**: basic pre-order traversal of n-ary tree.
* **stream_traverse**: provide a generator that performs a pre-order traversal of the tree
"""

def traverse(root, callback):
    """
    Walk the AST generated by the swim parser, starting with the
    SetList Node and dumping out the node names

    :param callback: callback function
    :type callback: function
    
    """
    #perform operation on current node
    callback(root)

    if root.children:
        for child in root.children:
            traverse(child, callback)

def stream_traverse(root, callback):
    """
    Provide a generator that will walk the AST at the pace the caller
    desires :).
    """
    if (root):
        yield callback(root)

        for child in root.children:
            for n in stream_traverse(child, callback):
                yield n

def visitor_traverse(root, visitor):
    """
    Accepts a visitor and calls the visit function.
    """
    if (root):
        root.accept(visitor)

        for child in root.children:
            visitor_traverse(child, visitor)

def xml_traverse(root, visitor, close_visitor, out=[]):
    """
    Basically does a pre-order traversal with the first visitor and
    then a post-order traversal with a "closer_visitor" that provides
    closing tags.
    """
    if (root):
        root.accept(visitor)
        out.append(root.xml)

        for child in root.children:
            xml_traverse(child, visitor, close_visitor)

        root.accept(close_visitor)
        out.append(root.xml)

    return out
        
if __name__=="__main__":
    import swim_parser
    import sys
    
    p = swim_parser.parser
    #running parser will generate a SetList node containing all other Nodes.
    res = parser.parse("10x100")
    
    cb = lambda x: sys.stdout.write(str(x) + '\n')
    traverse(res,cb) 
