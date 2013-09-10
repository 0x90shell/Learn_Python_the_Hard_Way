#Note: %formatting has been depricated from python 3.0+
#% means formatting in python.

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = 74 * 2.54
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
#%s formats to String, using sing str()).

print "Let's talk about %s." % name

#%d formats to Signed integer decimal.
print "He's %d centimeters tall." % height_cm
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."

#%s or %d are placed in order of occurence, parenthesis required
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

#What does %r do?
print "%r" % teeth
print "%r" % height
