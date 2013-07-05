from random import randint
from math import sqrt

###############################################################################
## Graph class
# Graphs are represented as two-dimensional adjacency matrices where each row 
# and column is a vertex and whenever two vertices have an edge, that 
# (row,col) (or (col,row)) pair in the matrix will have that edge's value. 
# Negative-weight edges are acceptable. For weightless edges, just use 
# weight 0 (since this is not the same as not having an edge). 
# For more information about how this works:
# http://en.wikipedia.org/wiki/Adjacency_matrix
# http://en.wikipedia.org/wiki/Graph_(data_structure)
###############################################################################
class Graph:

	def __init__(self,matrix=[],not_edge=9999999999):
		self.matrix = matrix
		self.not_edge = not_edge # the value in the matrix when there is no
		# edge between the two vertices. Except in very specific situations
		# you shouldn't need to specify this.

	###########################################
	# return a pretty-looking string of the matrix
	def to_string(self):
		graph_string = ""
		for row in self.matrix:
			row_string = "["
			i = 0
			while i < len(row):
				val = row[i]
				if val == self.not_edge:
					row_string += "-"
				else:
					row_string += str(val) 
				if i != len(row)-1:
					row_string += ", "
				i += 1
			row_string += "]"
			graph_string += row_string + "\n"
		return graph_string
	###########################################

	###########################################
	# return a copy of the matrix
	def copy_matrix(self):
		new_matrix = []
		row = 0
		while row < len(self.matrix):
			row_val = []
			col = 0
			while col < len(self.matrix[row]):
				row_val.append(self.matrix[row][col])
				col += 1
			new_matrix.append(row_val)
			row += 1
		return new_matrix
	###########################################

	###########################################
	# returns true if vertex a and b share an edge
	# in the matrix
	def share_edge(self,a,b):
		if self.matrix[a][b] != self.not_edge:
			return True 
		return False  
	###########################################

	##################################################################
	# Everything from here to the end of the class will handle graphical
	# representations of graphs. Pay no attention to this stuff if you
	# don't plan on drawing the graphs to the screen.
	# If you do, the methods that matter (currently) are greedy_locations()
	# and random_locations(). Everything else is just helper-methods

	###########################################
	# returns a list of pairs of pairs: ((row, col), (x,y)) saying the
	# pixel locations for the vertex at (row,col) where (x,y) is assigned
	# greedily. Width and height are the window dimensions.
	def greedy_locations(self,width,height):
		locs = []
		row_num = 0
		while row_num < len(self.matrix):
			# put the first vertex in randomly
			if len(locs) == 0:
				locs.append((randint(0,width),randint(0,height)))
			else:
				rand_start_point = (randint(0,width),randint(0,height))
				coord = self.min_dist_all(locs,row_num,rand_start_point,10)
				locs.append(coord)
			row_num += 1
		return locs
	###########################################

	###########################################
	# returns a list of randomly generated (x,y) 
	# coordinates corresponding to the rows in the matrix
	def random_locations(self,width,height):
		locs = []
		for row in self.matrix:
			locs.append((randint(0,width),randint(0,height)))
		return locs
	###########################################	

	###########################################
	# locs is the list as defined above and vertex is a row_num 
	# Returns the (x,y) for the vertex such that it's distance to 
	# every vertex it is connected to in locs is minimal
	# Going to try to find this minimal distance by picking a random x,y 
	# point for the vertex, and then seeing which direction it can move in
	# to minimize this distance
	def min_dist_all(self, locs, vertex, point, min_dist):
		dist = self.dist_sum(locs,vertex,point)
		x = -1
		while x < 2:
			y = -1
			while y < 2:
				if y != x:
					new_point = (point[0]+x,point[1]+y)
					if self.dist_sum(locs,vertex,new_point) < dist and \
					dist > min_dist:
						point = self.min_dist_all(locs,vertex,new_point,
						min_dist)
				y += 1
			x += 1
		return point
	###########################################

	###########################################
	# returns the total distancs from vertex at point to all
	# other vertices with which it shares an edge
	def dist_sum(self,locs,vertex,point):
		dist_sum = 0
		loc_num = 0
		while loc_num < len(locs):
			if self.share_edge(vertex,loc_num):
				dist_sum += self.dist(point,locs[loc_num])
			loc_num += 1
		return dist_sum
	###########################################

	###########################################
	# cartesian distance form a to b
	def dist(self,a,b):
		return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
	###########################################
	# End graphical stuff
	##################################################################

###############################################################################		
## End Graph class
###############################################################################