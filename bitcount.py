print "\nThis program calculates the maximum unsigned integer supported by each bit postion up to the selected bit postion."
print "\nPlease enter the bit position you want to calculate to."

def da_mathz():
	i = 0
	z = 1
	
	try:
		q = int(raw_input("> ")) +1
		
	except:
		print "Enter a number, please."
		da_mathz()
		
	else:
		while (i<q):
			print "Bit position %s equals %s" % (i,z)	
			i+=1 
			z*=2

da_mathz()
	
