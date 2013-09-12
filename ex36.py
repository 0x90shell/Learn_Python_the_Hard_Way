#make program like ex35
#1 - 3 choices 
#2 - 2 choices, both end
#3 - 4 choices - 3 end & 1 goes to 4
#4 - 3 choices - 1 end, 1 goes to choice 1, 1 goes to 5th choice
#5 - 2 choices, 1 ends, 1 6th choice
#6 - 3 choices all end
#mapped on ex36.vsd

from sys import exit

def Stage_1 ():
	"""Three Choice Stage"""
	print "\nYou see three rooms to enter."
	print "Do you enter room one, two, or three?"
	
	door = raw_input("> ").lower()
		
	if "one" in door:
		Stage_2()
	elif "two" in door:
		Stage_3()
	elif "three" in door:
		Stage_4()
	else:
		print "\nPlease type one, two, or three.".upper()
		Stage_1()
	
def Stage_2 ():
	"""Two Choice Stage"""
	print "test2"
	
def Stage_3 ():
	"""Four Choice Stage"""
	print "test3"
	
def Stage_4 ():
	"""Three Choice Stage"""
	print "test4"
	
def Stage_5 ():
	"""Two Choice Stage"""

def Stage_6 ():
	"""Three Choice Stage"""

def Start ():
	"""This starts the sequence."""
	print "Welcome to the Golden Saucer."
	print "You may remember us from FF7."
	print "Anyways, lets see if you can win something."
	
	Stage_1()
	
def End (what_happened):
	"""This ends the sequence."""
	print what_happened, "\nSee you next time!"
	exit(0)
	
def Random():
	"""This adds some variety to outcome."""
	
Start()

