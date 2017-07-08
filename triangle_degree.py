import math

def find_radian(a,b,c):

    try:
        dummy = pow(b,2) + pow(c,2) - pow(a,2)
    	dummy = dummy / (2*b*c)
    	dummy = math.acos(dummy)
    except: dummy = 0
    
    # can't be more than 180
    if dummy >= math.radians(180): return 0
    
	return dummy

def find_degree(a,b,c):
	radian = find_radian(a,b,c)
	return round(math.degrees(radian))

def find_all_degree(a,b,c):
	return [find_degree(a,b,c), find_degree(b,c,a), find_degree(c,a,b)]

def checkio(a, b, c):

    #replace this for solution
    print(find_all_degree(a,b,c))
    return sorted(find_all_degree(a,b,c))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    #assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"


