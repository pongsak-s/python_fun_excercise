

x = range(100)


print([(i,x_i) #create tuple (immutable list) 
	for i,x_i in enumerate(x) # extract index and value
	if (i is not 0) and (x_i % i == 0)  ]) # condition to craft list

