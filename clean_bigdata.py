

bigData = ["a", 1, 3, 4, None]


def cleanData(x):
	try: return int(x)
	except: return None

cleanedData = [cleanData(x_i) for x_i in bigData]

if __name__ == '__main__':
 	print(cleanedData) 

