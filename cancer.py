# cancer.py
# this will import math methods from the math library
# from math import *


def cancer():
	print "we are sorry you have cancer. is this your first time getting it?"
	answer = raw_input("Please type 'y' or 'n' ")
	new_answer = answer.lower()
	a = new_answer 
	if a == 'y':
		print "damn we are sorry to hear that."
	elif a == 'n':
		print "you poor bastard. "
	else:
		print "please choose 'y' or 'n' and try again."
		cancer()
cancer()



# the sqrt() method gets called from the math library
# if we only 'import math' then we need to add math.sqrt() to sqrt() method.