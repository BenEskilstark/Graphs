# takes in a matrix representing a graph. Returns a matrix that is that tree
def prim(matrix, not_edge):
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

def in_tree(tree,coord):
	for node in tree:
		if node[0] == coord[0] and node[1] == coord[1]:
			return True
		if node[0] == coord[1] and node[1] == coord[0]:
			return True
	return False

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
