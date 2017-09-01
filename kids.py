# kids.py


def kids():
	print "we are so glad to hear you have kids!"
	answer = raw_input("please tell us how many yungins you have.	")
	new_answer = answer.lower()
	a = new_answer 
	if len(a) > 0 and (a == "1" or a == "2" or a == "3" or a == "4"):
		print "terrific!"
	elif a == "5" or a == "6" or a == "7" or a == "8":
		print "lots of free time huh!"
	elif a == "0":
		print "sorry bubby."
	elif a.isalpha():
		print "those aren't numbers!"
		kids()
	else:
		print "quit lying. you aint got that many kids."
		kids()
kids()