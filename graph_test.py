from prims import *
from graph import *

###############################################################################		
## Test code
###############################################################################
MAX = 9999999999	# if I was being more careful, in the graph definitions 
					# below, I'd use MAX instead of the default (but I know 
					# that they are the same and like the implicit not_edge)

test = [
[MAX,16,12,21,MAX,MAX,MAX],
[16,MAX,MAX,17,20,MAX,MAX],
[12,MAX,MAX,28,MAX,31,MAX],
[21,17,28,MAX,18,19,23],
[MAX,20,MAX,18,MAX,MAX,11],
[MAX,MAX,31,19,MAX,MAX,27],
[MAX,MAX,MAX,23,11,27,MAX]]

g = Graph(test) # make a graph of the test matrix
print g.to_string() # see what it looks like
print "\n" 
gp = Graph(prim(g,g.not_edge)) # make a new graph of the minimal spanning 
									  # tree of test
print gp.to_string() 
print gp.random_locations(500,500)  # test randomly assigning coordinates
print gp.greedy_locations(500,500)	# test the greedy algorithm
###############################################################################		
## End test code
###############################################################################