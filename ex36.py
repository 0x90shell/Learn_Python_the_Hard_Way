#make program like ex35
#1 - 3 choices 
#2 - 2 choices, both end
#3 - 4 choices - 3 end & 1 goes to 4
#4 - 3 choices - 1 end, 1 goes to choice 1, 1 goes to 5th choice
#5 - 2 choices, 1 ends, 1 6th choice
#6 - 3 choices all end
#mapped on ex36.vsd

from sys import exit
import random

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
	print "\nYou stumble into a whino, near the slot machines."
	print "He challenges you to a sword duel, cause thats how he rolls."
	print "You have no time to react, as he immediately draws out his blade."
	print "He lunges towards you!"
	print "\nDo you: (1) Sidestep and apologize to this drunk bastard."
	print "\n\t or\n"
	print "\t(2) Draw your own blade for a counter."
	
	whino = raw_input("> ")
	
	if "1" in whino:
		End("\nYou evade his attack, but stumble on to the floor.\nHe swirls back and kills you.")
	elif "2" in whino:
		End("He kills you before your blade leaves the sheath.")
	else:
		print "\nPlease type 1 or 2.".upper()
		Stage_2()
	
def Stage_3 ():
	"""Four Choice Stage"""
	print "\nYou walk up to a blackjack table, and the dealer deals you in."
	print "You lose multiple hands, but being a masochist you throw everything in on a last hurrah."
	print "Your hand totals 15."
	print "\nDo you: (1) Hit."
	print "\n\t or\n"
	print "\t(2) Stay."
	
	hand = raw_input("> ")
	
	def Decision_2():
		print "\nDo you: (1) Play another hand.."
		print "\n\t or\n"
		print "\t(2) Wonder to an adjacent room."
		
		new_hand = raw_input("> ")
		
		if "1" in new_hand:
			End("You lose everything. Should have got out while ahead.")
		elif "2" in new_hand:
			Stage_4()
		else:
			print "\nPlease type 1 or 2.".upper()
			Decision_2()
	
	if "1" in hand:
		End("You bust and lose everything.")
	elif "2" in hand:
		print "\nYou win the hand!"
		Decision_2()
	else:
		print "\nPlease type 1 or 2.".upper()
		Stage_3()
	
def Stage_4 ():
	"""Three Choice Stage"""
	print "\nYou walk into a neon-bathed room with stripers."
	print "The realization dawns that they are whores, not simply stripers."
	print "A man walks up asking if you would like to bed one of his women."
	print "Looking past him you see several pretty woman and two doorways."
	
	print "\nDo you: (1) Pay the man and take a woman."
	print "\n\t or\n"
	print "\t(2) Enter the first room."
	print "\n\t or\n"
	print "\t(3) Enter the second room."
		
	decision = raw_input("> ")
		
	if "1" in decision:
		print "You enjoy the woman for several hours and then decide to wonder around some more."
		Stage_2()
	elif "2" in decision:
		print "You politely turn down to pimp's offer and wonder on."
		Stage_5()
	elif "3" in decision:
		End("You make the mistake of walking into the pimp's office, and he beats the shit out of you.")
	else:
		print "\nPlease type 1, 2, or 3.".upper()
		Stage_4()
	
def Stage_5 ():
	"""Two Choice Stage"""
	print "\nYou see a man standing on a large scale."
	print "Another man stands in front of the scale."
	print "This second man is calling for people to guess the weight of the fellow on the scale."
	
	print "\nDo you: (1) Play the game."
	print "\n\t or\n"
	print "\t(2) Keep wondering through the Golden Saucer."
		
	decision = raw_input("> ")
		
	if "1" in decision:
		End("You get scammed and lose everything.")
	elif "2" in decision:
		Stage_6()
	else:
		print "\nPlease type 1 or 2.".upper()
		Stage_5()	

def Stage_6 ():
	"""Three Choice Stage"""
	print "\nThis room has a slot machines, roulette, and poker."
	
	print "\nDo you: (1) Play slots."
	print "\n\t or\n"
	print "\t(2) Play roulette."
	print "\n\t or\n"
	print "\t(3) Play poker."
		
	decision = raw_input("> ")
		
	if "1" in decision:
		Random()
	elif "2" in decision:
		End("You lose everything.")
	elif "3" in decision:
		End("Gambling favors the house. You lose everything.")
	else:
		print "\nPlease type 1, 2, or 3.".upper()
		Stage_6()

def Start ():
	"""This starts the sequence."""
	print "Welcome to the Golden Saucer."
	print "You may remember us from FF7."
	print "Anyways, lets see if you can win something."
	
	Stage_1()
	
def End (what_happened):
	"""This ends the sequence."""
	print "\n",what_happened, "\n"
	exit(0)
	
def Random():
	"""This adds some variety to outcome."""
	random_number = random.random()
	
	if random_number < 0.5:
		End("You lost a lot, but decide to call it quits.")
	else:
		End("You won big at slots!")
			
Start()

