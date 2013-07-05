from prims import *
from graph import *

###############################################################################		
## Test code
###############################################################################
MAX = 9999999999

test = [
[MAX,16,12,21,MAX,MAX,MAX],
[16,MAX,MAX,17,20,MAX,MAX],
[12,MAX,MAX,28,MAX,31,MAX],
[21,17,28,MAX,18,19,23],
[MAX,20,MAX,18,MAX,MAX,11],
[MAX,MAX,31,19,MAX,MAX,27],
[MAX,MAX,MAX,23,11,27,MAX]]

g = Graph(test)
print g.to_string()
print "\n"
gp = Graph(prim(g.matrix,g.not_edge))
print gp.to_string()
print gp.random_locations(500,500)
print g.greedy_locations(500,500)
###############################################################################		
## End test code
###############################################################################