#i = 0
numbers1 = []
numbers2 = []

print "Pick a number to go to."
external_variable1 = int(raw_input("> "))

print "Pick a number to increment by."
external_variable2 = int(raw_input("> "))

def my_while_function(internal_variable1, internal_variable2):
	i = 0
	print "\nThe while function results: \n"
	while i < internal_variable1:
		print "At the top i is %d" % i
		numbers1.append(i)
	
		i = i + internal_variable2
		print "Numbers now: ", numbers1
		print "At the bottom i is %d" % i
		
def my_for_function(internal_variable1, internal_variable2):
	print "\nThe for function results: \n"
	for i in range(0,internal_variable1, internal_variable2):
		print "At the top i is %d" % i
		numbers2.append(i)
		print "Numbers now: ", numbers2
		print "At the bottom i is %d" % i
			
my_while_function(external_variable1, external_variable2)

my_for_function(external_variable1, external_variable2)
	
	
print "\nThe numbers1: "

for num in numbers1:
	print num
	
print "\nThe numbers2: "

for num in numbers2:
	print num