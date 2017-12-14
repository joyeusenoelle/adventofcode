##values = [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147, 304, 330, 351, 362, 747, 806]
##for i in range(len(values)):
##	j = i+1
##	print("i: {}\tval: {}\n\tdiv: {}\tmod: {}".format(j, values[i], values[i]/j, values[i]%j))

N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)
NW, NE, SW, SE = (-1, -1), (-1, 1), (1, -1), (1, 1)
turn_left = {N: W, W: S, S: E, E: N}

def spiral(width, height):
	if width < 1 or height < 1:
		raise ValueError
	x, y = width//2, height//2
	dx, dy = E # initial direction
	matrix = [[0] * (width+1) for _ in range(height+1)]
	matrix[y][x] = 1
	x, y = x+1, y
	while True:
		matrix[y][x] = matrix[y][x] + \
						matrix[y-1][x-1] + matrix[y-1][x] + matrix[y-1][x+1] + \
						matrix[y][x-1] + matrix[y][x] + matrix[y][x+1] + \
						matrix[y+1][x-1] + matrix[y+1][x] + matrix[y+1][x+1]
		if matrix[y][x] > 312051:
			return matrix
		new_dx, new_dy = turn_left[dx,dy]
		new_x, new_y = x + new_dx, y + new_dy
		if (0 <= new_x < width and 0 <= new_y < height and matrix[new_y][new_x] == 0): #can turn left
			x, y = new_x, new_y
			dx, dy = new_dx, new_dy
		else: #can't turn left, move straight
			x, y = x + dx, y + dy
			if not (0 <= x < width and 0 <= y < height): # nowhere to go
				return matrix

def print_matrix(matrix):
	width = len(str(max(el for row in matrix for el in row if el is not None)))
	fmt = "{:0%dd}" % width
	for row in matrix:
		print(" ".join(fmt.format(el) for el in row))

print_matrix(spiral(10, 10))