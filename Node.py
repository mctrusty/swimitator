class Node:
        pass

class Set(Node):
        def __init__(self, type, children=None, leaf=None):
		self.type = type
		if children:
			self.children = children
		else:
			self.children = []
		self.leaf = leaf
		
	def __repr__(self):
		return "Set info %s" % (self.children)

		
class Interval(Node):
	def __init__(self, minutes=0, seconds=0):
		self.type = "interval"
		self.minutes = minutes
		self.seconds = seconds
		
	def __repr__(self):
		return str(self.minutes * 60 + self.seconds)
		
	def total_seconds(self):
		return self.minutes * 60 + self.seconds
		
