print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print " This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
	
start_point = 10000

#Ths fills in variable 1(jelly_beans) for beans, var2(jars) for jars, and var3(crates) for crates, since the function returns them in that order.
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %s" % start_point

#reference global variables 
print "We'd have %d beans, %d jars, amd %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"

#this utilizes the internal variables of the function to propegate the decimal calls
print "We'd have %d beans, %d jars, and %d crates." %secret_formula(start_point)