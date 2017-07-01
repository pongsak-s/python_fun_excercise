import timeit

data = range(10000)
searchKey = len(data) - 1 #worst case

# test function
def testFn():
	return searchKey in data #bool if find key in data

print("let's timeit")
benchmark = timeit.Timer('testFn()', 'from __main__ import testFn, data, searchKey')

print(benchmark.timeit(10)) #run ten times


