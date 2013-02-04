class Node:
        """
        Base class for swim AST. It contains no methods or members
        """
        pass

class SetList(Node):
        """
        Contains list of sets that comprise a workout.

        
        """
        def __init__(self, set=None, repeats=1):
                self.type = "set_list"
                if set:
                        self.set_list= [set]
                else:
                        self.set_list = []
                self.repeats = repeats

        def add_set(self, set):
                self.set_list.append(set)
                return self

        def get_all_sets(self):
                return self.set_list

class MultiSet(Node):
        """
        Contains a set of sets, for when you want to iterate over a
        series of sets mutliple times.

        Example::
        
            3 x {
                2 x 50 freestyle EN1 @45
                3 x 100 K EN3 @2
            }
        
        """
        def __init__(self, children, repeats=1):
                self.type = "multi_set"
                if children:
                        self.children = children
                else:
                        self.children = []
                self.repeats = repeats
                
class Set(Node):
        """
        The basic representation of one unit of work in a swimming
        workout. It describes number of reps, distance, stroke, skill,
        intensity level, and interval

        Example::

            10 x 100 fly EN3 @2:00

        """
        def __init__(self, children=None, leaf=None):
		self.type = "set"
		if children:
			self.children = children
		else:
			self.children = []
		self.leaf = leaf
		
	def __repr__(self):
		return "Set info %s" % (self.children)

class Count(Node):
        """
        Tracks information on number of reps and distance of those
        reps for a Set.

        Example::
        
            5 x 50
            
        """
        def __init__(self, reps, value):
                self.type = "count"
                self.reps = reps
                self.distance = value

        def __repr__(self):
                return "<reps>" + str(self.reps) + "</reps>" + "<distance>" + str(self.distance) + "</distance>"
        
class Interval(Node):
        """
        Time length of a single rep in a set. Can be given in
        minutes:seconds (1:00) or in seconds (90s).
        """
	def __init__(self, minutes=0, seconds=0):
		self.type = "interval"
		self.minutes = minutes
		self.seconds = seconds
		
	def __repr__(self):
		return str(self.minutes * 60 + self.seconds)
		
	def total_seconds(self):
		return self.minutes * 60 + self.seconds

class Zone(Node):
        """
        Intensity level at which a rep is to be performed. Can be
        given in "EN#" or "Zone #" notation.

        Example::
        
            EN3

        """
        def __init__(self, zone=""):
                self.type="zone"
                self.zone = zone

        def __repr__(self):
                return "<zone>" + self.zone + "</zone>"

class Kick(Node):
        """
        Denotes set is a kick set.
        """
        def __init__(self, stroke="free"):
               self.type="kick"
               self.stroke = stroke

        def __repr__(self):
                return self.stroke

class Drill(Node):
        """
        Denotes set is a drill set.
        """
        def __init__(self,stroke="",drill=""):
                self.type = "drill"
                self.stroke = stroke
                self.drill = drill

        def __repr__(self):
                return self.drill + ' ' + self.stroke

class Stroke(Node):
        """
        Indicates stroke to be performed on a Set.

        (butter)fly, fr(eestyle), back(stroke), br(eaststroke) are the
        competetive strokes that may be indicated.
        """
        
        def __init__(self, stroke=""):
                self.type = "stroke"
                self.stroke = stroke

        def __repr__(self):
                return "<stroke>" + self.stroke + "</stroke>"

