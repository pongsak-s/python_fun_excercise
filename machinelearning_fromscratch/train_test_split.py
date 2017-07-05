
import random


def split_data(data, prob):
	"""split data into fractions [prob, 1-prob]"""
	results = [], []
	for row in data:
		results[0 if random.random() < prob else 1].append(row)
	return results

def train_test_split(x, y, test_pct):
	"""split test/train data
		x = data
		y = expected result"""
	data = zip(x,y)
	train, test = split_data(data, 1 - test_pct)
	x_train, y_train = zip(*train)
	x_test, y_test = zip(*test)
	return x_train, y_train, x_test, y_test

if __name__ == '__main__':
	x = range(10)
	y = range(10)
	x_train, y_train, x_test, y_test = train_test_split(x,y, 0.33) #30%
	print(x_train, y_train, x_test, y_test)


