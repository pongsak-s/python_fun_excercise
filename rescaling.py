
import random
import numpy

# create the random number between -10 to 10
bigscale = [ (random.random() * 20 ) -10 for _ in range(5) ]


def rescale(x, mean, std):
	return (x - mean) / std

rescale = [rescale(x_i, numpy.mean(bigscale), numpy.std(bigscale)) for x_i in bigscale ] 




if __name__ == '__main__':
	print(rescale)
