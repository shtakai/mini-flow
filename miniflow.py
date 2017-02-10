# Node holds the base set of properties that every node holds.
class Node(object):
	def __init__(self):
	# Each node recieves inputs from multiple other nodes
	# Node(s) from which this Node recieves values
	self.inbound_nodes = inbound_nodes
	
	# Each node creates a single output, which will be passed to other nodes
	# Node(s) to which this Node passes values
	self.outbound_nodes = []
	
	# For each inbound Node here, add this Node as an outbound Node
	# to _that_ Node.
	for n in self.inbound_nodes:
		n.outbound_nodes.append(self)	
	
	# Each node calculates a value to represent its output
	# Initialize the value to None to indicate that it exists but hasn't been set up yet
	self.value = None

	# Each node will need to be able to pass values forward and perform backpropagation
	def forward(self):
		'''
		Forward Propagation

		Computes the output value based on inbound nodes and
		stores the result in self.value 
		'''
		raise NotImplemented

# Input is a subclass of Node that performs calculations and holds values
# The Input subclass holds a value, such as a data feature or a model parameter(weight/bias)
class Input(Node):
	def __init__(self):
	'''
	An Input Node has no inbound nodes,
	hence we do not need to pass anything to the Node instantiator
	'''
	Node.__init__(self)

	'''
	Input node is the only node that may receive its value as an argument to forward().
	
	All other node implications should calculate their values from 
	the previous nodes, using self.inbound_nodes
	'''
	def forward(self, value = None):
		'''
		The value can be set explicitly or with the forward() method. 
		This value is then fed through the rest of the neural network.
		'''
		if value is not None:
			self.value = value



