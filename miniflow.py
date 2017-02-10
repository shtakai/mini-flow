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

# The topological_sort function implements the topological sorting using Kahn's Algorithm
# It returns a sorted list of nodes in which all the calculation can run in series
# It takes in a feed_dict, which is how we initially set a value for an Input node.
# feed_dict is represented by the Python dictionary data structure
def topological_sort(feed_dict):
	'''
	Kahn's algorithm
	https://en.wikipedia.org/wiki/Topological_sorting#Kahn.27s_algorithm
	
	L <- Empty list that will contain the sorted elements
	S <- Set of all nodes with no incomming edges
	while S is non-empty do
		remove a node n from S
		add n to tail of L
		
		for each node with an edge e from n to m do
		remove edge e from the graph
		if m has no incoming edge then
			insert m into S
		
	if graph has edges then
		return error (graph has at least one cycle)
	else
		return L (topically sorted order)
	'''
	
	input_nodes = [n for n in feed_dict.keys()]	
	G = {}
	nodes = [n for n in input_nodes]
	while len(nodes) > 0:
		n = nodes.pop(0)
		if n not in G:
			G[n] = {'in': set(), 'out': set()}
		
		for m in n.outbound_nodes:for m in n.outbound_nodes:
			if m not in G:	
				G[m] = {'in': set(), 'out': set()}
			G[n]['out'].add(m)
			G[m]['in'].add(n)
			nodes.append(m)
	
	L = []
	S = set(input_nodes)
	while len(S) > 0:
	n = S.pop()
	
	if isinstance(n, Input):
		n.value = feed_dict[n]
	
	L.append(n)
        for m in n.outbound_nodes:
		G[n]['out'].remove(m)
		G[m]['in'].remove(n)
		if len(G[m]['in']) == 0:
			S.add(m)

	return L
