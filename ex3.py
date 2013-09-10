# statement
print "I will now count my chickens:"

#statement, followed by math (order of operations places multiplication BEFORE additon)
print "Hens", 25 + 30 / 6
#statement, followed by math (order of operations places multiplication & modulo BEFORE subtraction
#reading from left to right, multiplication comes first
#4 goes into 75(25*3) 18 times (72), so the remainder(modulo) is 3 (75-72)
#100 - 3 = 97
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

#modulo and multiplication take priority
#2 goes into 4 evenly, meaning modulo is zero 
#1/4 is 0.25 but since this is not floating point it is rounded down to zero
#6-5=1 ....  1+0-0+6=7 
#making 1 into 1.0 will show the correct answer of 6.75
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"
#5 is not less than -2
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > - 2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2