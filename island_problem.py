


def isAdjacent(a,b):
	"""check if two coordinate is adjacent"""
	a_i = a[0]
	a_j = a[1]
	b_i = b[0]
	b_j = b[1]

	# row must be less than one
	# col must be also less then one
	print("a_j: %d b_j: %d" % (a_j, b_j))
	#print(str(abs(a_j - b_j)))
	if abs(a_i - b_i) > 1 or abs(a_j - b_j) > 1:
		return False

	return True

def isTwoIslandsAreOnSameLand(island1, island2):
	"""check if two islands are on the same land"""
	for space in island1.tuples:
		if island2.isAdjacentToThisIsland(space[0], space[1]):
			return True
	return False

class Island():
	"""Island object to be reuse for each island"""
	def __init__(self):
		self.tuples = []

	def addTuple( self,a,b):
		self.tuples.append( (a,b) )

	def isAdjacentToThisIsland(self, a,b):
		for t_i in self.tuples:
			if(isAdjacent(t_i, (a,b))):
				return True
		return False

	def expandIsland(self,a,b):
		if self.isAdjacentToThisIsland(a,b):
				self.addTuple(a,b)
				return True
		return False

	def countSpaceInIsland(self):
		return len(self.tuples)

	def __str__(self):
		return str(self.tuples)


def findIslands(land):
	"""find all islands"""
	islands = []
	for index_i, columns in enumerate(land):
		for index_j, value in enumerate(columns):
			# if it's not a water
			if(value):
				foundExistingIsland = False
				for island in islands:
					if( island.expandIsland(index_i, index_j) ):
						print("found exist island at %d, %d" % (index_i, index_j))
						foundExistingIsland = True
						break

				if(not foundExistingIsland):
					print("add new island for %d, %d" % (index_i, index_j))
					newIsland = Island()
					newIsland.addTuple(index_i, index_j)
					islands.append(newIsland)


	# optimize the islands
	islands_blueprint = list(islands)

	index = len(islands) - 2
	while index >= 0:
		island1 = islands_blueprint[index + 1]
		island2 = islands_blueprint[index]

		# join tuples and delete dup island
		if isTwoIslandsAreOnSameLand(island1,island2):
			islands[index].tuples += islands[index + 1].tuples
			del islands[index + 1]

		index = index - 1


	return islands


if __name__ == '__main__':

	# Test isadjacent
	assert( isAdjacent( (1,2), (0,0) ) == False )
	assert( isAdjacent( (1,1), (0,0) ) == True )
	assert( isAdjacent( (1,1), (0,2) ) == True )

	# mock island
	island = Island()
	island.addTuple(1,2)

	# test island->tuple
	assert( island.tuples[0] == (1,2) )

	# test island->addtuple
	island.addTuple(2,2)
	assert( island.tuples[0] == (1,2) )
	assert( island.tuples[1] == (2,2) )

	# test island->expandisland
	assert( island.expandIsland(3,4) == False)
	assert( island.expandIsland(3,3) == True)
	assert( island.expandIsland(2,3) == True)
	assert( island.expandIsland(5,5) == False)

	# mock basic land
	land1 = [ [0,1,0],
	[0,1,0]]

	# count one island
	assert(len(findIslands(land1)) == 1)

	# mock land
	land2 = [[0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]]


	# count two island
	assert(len(findIslands(land2)) == 2)

	print(sorted(["%d" % (island.countSpaceInIsland()) for island in findIslands(land2)]))

	print("all test passed")


