people = 30
cars = 40 
buses = 15 

# if 40 is greater than 30
if cars > people:
	#do this
	print "We should take the cars."
#if not true check to see if 40 is less than 30
elif cars < people:
#if so do this
	print "We should not take the cars."
#if neither is true 
else:
#do this
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."

""" 
else = otherwise do this
elif = else if or if not do check if this is true
"""