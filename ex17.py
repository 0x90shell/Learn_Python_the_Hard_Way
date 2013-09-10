from sys import argv
#exists returns True or False, if a file exists.
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
#input = open(from_file)
#indata = input.read()
input = open(from_file).read()

print "The input file is %d bytes long" % len(input)

print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#output = open(to_file, 'w')
#output.write(indata)
output = open(to_file, 'w').write(input)

print "Alright, all done."

#output.close()
#input.close()