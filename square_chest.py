
import numpy

# readable version

def generateTuples(matrix):
	"""for each square matrix .. find path in tuple (change to list) to make that square"""
	row, col = numpy.shape(matrix)
	"""go from top left->top right->bottom right->bottom left->top left"""
	return [ [matrix[0,x_j],matrix[0,x_j+1]] for x_j in range(col-1) ] + [ [matrix[x_i,row-1],matrix[x_i+1,row-1]] for x_i in range(row-1) ]+[ [matrix[col-1,x_j+1],matrix[col-1,x_j]] for x_j in sorted(range(col-1), reverse=True) ]+ [ [matrix[x_i+1,0],matrix[x_i,0]] for x_i in sorted(range(row-1),reverse=True) ]

def findSquareInPaths(square, paths):
	"""check if square in paths .. each step can be reverse .. because it's not a walk but just a line"""
	for each_step in square: 
		if each_step not in paths and list(reversed(each_step)) not in paths: return False
	return True

def checkio(lines_list):
	matrix_size = 4
	# create matrix from 1 to 16, 4x4
	matrix = numpy.reshape(list(range((matrix_size * matrix_size)+1))[1:], (matrix_size, matrix_size))
	# find all possible square in paths of tuple
	possibleSquares = [generateTuples(matrix[x_col:x_col + square_size, x_row:x_row + square_size]) for square_size in range(2, matrix_size + 1) for x_col in range(matrix_size - square_size + 1) for x_row in range(matrix_size - square_size + 1)]
	# count number of squares found
	return sum([1 if findSquareInPaths(square, lines_list) else 0 for square in possibleSquares])


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"