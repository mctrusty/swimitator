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

class Count(Node):
        def __init__(self, reps, value):
                self.type = "count"
                self.reps = reps
                self.distance = value

        def __repr__(self):
                return "<reps>" + str(self.reps) + "</reps>" + "<distance>" + str(self.distance) + "</distance>"
        
class Interval(Node):
	def __init__(self, minutes=0, seconds=0):
		self.type = "interval"
		self.minutes = minutes
		self.seconds = seconds
		
	def __repr__(self):
		return str(self.minutes * 60 + self.seconds)
		
	def total_seconds(self):
		return self.minutes * 60 + self.seconds

class Zone(Node):
        def __init__(self, zone=""):
                self.type="zone"
                self.zone = zone

        def __repr__(self):
                return "<zone>" + self.zone + "</zone>"

class Kick(Node):
        def __init__(self, stroke="free"):
               self.type="kick"
               self.stroke = stroke

        def __repr__(self):
                return self.stroke

class Drill(Node):
        def __init__(self,stroke="",drill=""):
                self.type = "drill"
                self.stroke = stroke
                self.drill = drill

        def __repr__(self):
                return self.drill + ' ' + self.stroke

class Stroke(Node):
        def __init__(self, stroke=""):
                self.type = "stroke"
                self.stroke = stroke

        def __repr__(self):
                return "<stroke>" + self.stroke + "</stroke>"

