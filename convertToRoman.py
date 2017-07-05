



mapping = {"I" : 1, "IV":4, "V": 5, "IX":9, "X": 10,"XL":40, "L": 50, "XC":90, "C": 100, "D": 500, "CD":400, "CM":900, "M": 1000}
invmapping = {1:"I", 4:"IV" , 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
orders = ["M", "CM", "D", "CD", "C", "XC", "L","XL", "X", "IX", "V", "IV", "I"]
loopIT = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

def toString(values):
	sb = []
	for x_i in orders:
		for _ in range(values[x_i]):
			sb.append(x_i)
	return "".join(sb)


def convert(x):
	values = {"I" : 0, "IV":0, "V": 0, "IX":0, "X": 0,"XL":0, "L": 0, "XC":0, "C": 0, "D": 0, "CD":0, "CM":0, "M": 0}
	temp = x
	for item in loopIT:
		print( "loop=%d" % item)
		while x >= item and x > 0:
			print( "    x=%d" % x)
			#update value
			values[invmapping[item]] += 1
			#decrement x
			x = x - item
	print("convert:%d, result:%s" % ( temp, toString(values)))
	return toString(values)

def tst_convert():
	convert(2)
	convert(902)
	convert(499)
	convert(2150)
	convert(6)
	#print( "tst: get mapping: %s" % (",".join([key for key,val in (test.getMapping()).items()])))


if __name__ == '__main__':
	tst_convert()