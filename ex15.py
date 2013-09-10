#import module for argument handeling
from sys import argv

#define arguments, script is always the filename for python file
script, filename = argv

#open txt you submitted as argument
txt = open(filename)

#print "Here's your file %r:" %filename
#print the text in the .txt file
#print txt.read()
#
print "Type the filename again:"
#enter txt file
file_again = raw_input ("> ")

#open and print txt file again
txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()