
import random

from probability import inverse_normal_cdf
from matplotlib import pyplot as plt

def random_normal():
	"""returns a random draw from a standard normal distribution"""
	return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]

ys1 = [ x + random_normal() / 2 for x in xs ]
ys2 = [ -x + random_normal() / 2 for x in xs ]

#print
plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("verfy different joint distribution")
plt.show()
