

def splitall(time):
	hh, mm, ss = time.split(":")

	if int(hh) >= 10: 
		h1 = int(str(hh)[0])
		h2 = int(str(hh)[1])
	else:
		h1 = 0
		h2 = int(str(hh)[0])

	if int(mm) >= 10: 
		m1 = int(str(mm)[0])
		m2 = int(str(mm)[1])
	else:
		m1 = 0
		m2 = int(str(mm)[0])


	if int(ss) >= 10: 
		s1 = int(str(ss)[0])
		s2 = int(str(ss)[1])
	else:
		s1 = 0
		s2 = int(str(ss)[0])

	return h1,h2,m1,m2,s1,s2

def tobin(temp):
	h1,h2,m1,m2,s1,s2 = temp
	print([h1,h2,m1,m2,s1,s2])
	dummy = ""
	dummy = "".join(["." if int(x_i) == 0 else "-" for x_i in '{0:02b}'.format(h1)])
	print(h2)
	dummy += " " + "".join(["." if int(x_i) == 0 else "-" for x_i in '{0:03b}'.format(h2)])


	dummy += " : "+ "".join(["." if int(x_i) == 0 else "-" for x_i in '{0:03b}'.format(m1)])
	dummy += " " + "".join(["." if int(x_i) == 0 else "-" for x_i in '{0:04b}'.format(m2)])



	dummy += " : "+ "".join(["." if int(x_i) == 0 else "-" for x_i in '{0:03b}'.format(s1)])
	dummy += " " + "".join(["." if int(x_i) == 0 else "-" for x_i in '{0:03b}'.format(s2)])

	return dummy

if __name__ == '__main__':
	print(tobin(splitall("2:21:12")))


