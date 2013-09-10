# Feed data directly into the formatting, without variable.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

#Referenced and formatted variables, within a variable.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#r puts quotes around string
print "I said: %r." % x

#s does not put quotes around string, so they are added manually
print "I also said: '%s'." % y

hilarious = False

#variable anticipates formatting of yet unkown variable
joke_evaluation = "Isn't that joke so funny?! %r"

#joke_evaluation has formatting delclared in variable, when called formatting statement is completed by closing the formatting syntax
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#since variables are strings python concatenates, rather than perform mathmetic equation with error
print w + e