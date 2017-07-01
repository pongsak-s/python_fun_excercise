
from __future__ import division

import random,math

from matplotlib import pyplot as plt
from collections import Counter
from probability import inverse_normal_cdf

def normalized(x, y): return x / y

def bucketize(point, bucket_size): return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size): return Counter(bucketize(point, bucket_size) for point in points)

def plot_historgram(points, bucket_size, title = ""):
	histogram = make_histogram(points, bucket_size)
	plt.bar( list(histogram.keys()), histogram.values(), width=bucket_size)
	plt.title = title
	plt.show()

# find unifor distribution random between -100 and 100
uniform = [200 * random.random() - 100 for _ in range(1000)]
plot_historgram(uniform, 10, "uniform")

# normal distribution with mean 0, sd 57
normalDist = [57 * inverse_normal_cdf(random.random()) for _ in range(1000)]
plot_historgram(normalDist, 10, "normal dist")



