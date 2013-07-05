###############################################################################
# takes in a graph and also the value the matrix is using
# to represent a non-edge. Returns a matrix that is the minimal spanning tree
# of that graph (assuming it is connected, else behavior undefined). 
# Prim's algorithm works by taking one vertex as the start, and then adding 
# edges to the tree s.t one end of the edge is in the (currently-defined) tree
# and the other end is outside of the tree. It takes the smallest edge with 
# that property each iteration. Note that in this implementation seed is 
# actually return an edge and not a vertex, effectively seeding with two 
# vertices. It can be proven that the smallest edge in a graph is necessarily 
# in the minimal spanning tree as is integral to the functioning of Kruskall's 
# algorithm which also returns the minimal spanning tree.
def prim(graph, not_edge):
	matrix = graph.matrix
	tree = seed(matrix,not_edge)
	for vertex in range(0,len(matrix)-2):
		smallest = not_edge
		smallest_coord = []
		for i in range(0,2):
			node = 0
			while node < len(tree):
				u = tree[node][i]
				v = 0
				while v < len(matrix[u]):
					if not in_tree(tree, (u,v)) and matrix[u][v] < smallest:
						smallest = matrix[u][v]
						smallest_coord = (u,v)
					v += 1
				node += 1
		tree.append(smallest_coord)
	return make_tree(tree,matrix,not_edge)
###############################################################################

###############################################################################
# takes in the tree list, and the matrix and returns a graph that is the 
# minimal spanning tree of that matrix's graph.
def make_tree(tree,matrix,not_edge):
	tree_matrix = copy_matrix(matrix)
	row = 0
	while row < len(tree_matrix):
		col = 0
		while col < len(tree_matrix[row]):
			if in_tree(tree, (row,col)):
				tree_matrix[row][col] = matrix[row][col]
			else:
				tree_matrix[row][col] = not_edge
			col += 1
		row += 1
	return tree_matrix
###############################################################################

###############################################################################
# regrettably an exact copy of a Graph method, I don't know how python works 
# well enough to not need this. Advice welcome.
def copy_matrix(matrix):
	new_matrix = []
	row = 0
	while row < len(matrix):
		row_val = []
		col = 0
		while col < len(matrix[row]):
			row_val.append(matrix[row][col])
			col += 1
		new_matrix.append(row_val)
		row += 1
	return new_matrix
###############################################################################

###############################################################################
# returns true if the given coordinate (or its inverse) is in the tree
def in_tree(tree,coord):
	for node in tree:
		if node[0] == coord[0] and node[1] == coord[1]:
			return True
		if node[0] == coord[1] and node[1] == coord[0]:
			return True
	return False
###############################################################################

###############################################################################
# returns the smallest non_empty edge in the matrix. The reason I chose to seed 
# with an edge rather than a vertex as is customary in Prim's algorithm is 
# because minimal spanning trees necessarily include all vertices, but they 
# do not include all edges. And with the adjacency matrix representation of the
# graph, it is conceptually easier to think of the tree as a set of edges 
# rather than as a set of vertices, thus leading me to make seed return an 
# edge and not a vertex.
def seed(matrix,not_edge):
	i = 0
	smallest = not_edge
	smallest_coord = []
	while i < len(matrix):
		j = 0
		while j < len(matrix[i]):
			if matrix[i][j] < smallest:
				smallest = matrix[i][j]
				smallest_coord = (i,j)
			j += 1
		i += 1
	return [smallest_coord]
# And just for funsies...
# Proof that the edge returned by seed will be in the minimal spanning tree:
# the above algorithm necessarily returns the smallest edge in the graph
# using a two-dimensional version of linear search. Let's call the edge (u,v).
# If (u,v) was NOT in the minimal spanning tree then there must be some other 
# edge that connects u to v, either directly or through some other vertices,
# but in order for this edge to be in the minimal spanning tree, it would have 
# to have smaller weight than (u,v) and by definition it does not.
# Then, by extension, if the second smallest edge does not also connect u to
# v, then it will also be in the minimal spanning tree, and if the third 
# smallest edge does not connect u,v, or the vertices from the second-smallest
# edge then that will bein the minimal spanning tree too. And in fact, this is
# the basis of Kruskall's algorithm.
###############################################################################
