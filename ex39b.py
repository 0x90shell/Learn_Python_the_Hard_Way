ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

#split(' ', ten_things)
#splits the string by spaces between items (delimiter = ' ')
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#Measures length by # of items in list, not length of words.
while len(stuff) != 10:
	#pop(more_stuff) = next_one
	#pop the last item in the list into a new variable
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	
	#append(next_one,stuff)
	#adds the new variable(last item popped) to the end of stuff
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

#stuff item 1, 2nd item in list(count starts at 0)
print stuff[1]

#stuff item 0-1 (last item in list) (-2 would be second to last item)
print stuff[-1] # whoa! fancy

#pulls out the last item from stuff
print stuff.pop()

#join(' ',stuff)
#joins the stuff list into a string by spaces
print ' '.join(stuff) # what? cool!

#join('#', stuff[3:5])
#Joins by pound symbol list item 3 through list item 4(item 5 marks end)
print '#'.join(stuff[3:5]) # super stellar!