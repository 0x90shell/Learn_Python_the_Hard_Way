cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."

# ok pay attention!
cities ['_find'] = find_city

while True:
	print "State? (ENTER to quit)",
	state = raw_input("> ")
	
	if not state: break
	
	#this line is the msot important ever! study!
	city_found = cities['_find'] (cities, state)
	print city_found
	
	"""
	'CA' = key
	
	 More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins.
	 
	 Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed.
	 
	 Continue with these:
	 http://docs.python.org/2/tutorial/datastructures.html
	 http://docs.python.org/2/library/stdtypes.html - mapping types
	 
	 """
	 
	 
	 