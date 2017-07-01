from string import ascii_lowercase as allchars
#from string import ascii_uppercase as allchars
#from string import ascii_letters as allchars
import random

def randomChar():
	return random.choice(allchars)

def randomString(x):
	return [randomChar() for i in range(x)]


print( ''.join(randomString(10)) )