# \t = tab
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."

#\\ = backslash
backslash_cat = "I'm \\ a \\ cat."

#\t* creates tab asterisk
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print """
%r
%s
"""

# 1. All python escape sequences: \\, \', \", \a, \b, \f, \n, \N{name}, \r, \t, \uxxxx, \Uxxxxxxxx, \v, \ooo, \xhh
print "All python escape sequences: \\ \' \" \a \b \f \n \N{name}, \r, \t, \uxxxx, \Uxxxxxxxx, \v, \ooo, "
# 2. If you were printing python code, you'd need to use ''' if you were printing a long python string starting with """