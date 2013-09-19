
#Step 1
#def foo():
#	return 1

# foo()

#a_string = "This is a gloval variable."

#def foo():
	#a_string = "test" #1
	#print locals()
#	x=1
#print globals() 

#foo()

#print a_string
#print
#print x #error since x is local

def foo(x):
	print locals()

foo(1)

#Continue http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/ @ step 5