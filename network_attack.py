
max_loop = 1000 #10k mins .. too long

# psedo code
# construct the variable to store the progress

# node1 and node2 have not yet started .. 
# node3 is completed
# node4 is in progress and will take 8 more minutes
# sample x = {1:-1, 2:-1, 3:0, 4:8} 

# for each min until all complete (all zeros) or reach max_loop
# 	  if any progress hit 0, kick off next node
#         next node need to not already in progress or completed (== -1)
#     decrement the progress .. 


def capture(matrix):

	x = {x_i:-1 for x_i in range(len(matrix))}

	duration = 0
	y = max_loop

	while (duration <=max_loop) and (y > 0):


		if duration is 0: x[0] = 0

		completedItemInThisRound = [x_i for x_i,x_v in x.items() if x_v is 0]

		for eachRowIndex in completedItemInThisRound:
			targetRow = matrix[eachRowIndex]
			nextPossibleWorkingNodes = [x_i for x_i, x_v in enumerate(targetRow) if x_v is 1 and x_i is not eachRowIndex]

			for node in nextPossibleWorkingNodes:
				if x[node] is -1 :
					x[node] = matrix[node][node]

		#end .. let decrement
		x = {x_i:x_v - 1 if x_v>0 else x_v for x_i,x_v in x.items()}

		duration += 1
		y = len([0 for _,x_v in x.items() if x_v is not 0])
		print("x: %s" % (str(x)))
		print("duration: %d" % duration)
		print("len: %d" % y)
	print("answer:%d" % duration)
	return duration 


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0,1,0],[1,9,1],[0,1,9]]) == 18



