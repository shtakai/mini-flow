# nn.py
# This file describes the Nueral Net Architecture
# This script builds and runs a graph with miniflow.

from miniflow import *

x, y = Input(), Input()

f = Add(x, y, z)

feed_dict = {x: 10, y: 5}

sorted_nodes = topological_sort(feed_dict)
output = forward_pass(f, sorted_nodes)

print("{} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], output))
