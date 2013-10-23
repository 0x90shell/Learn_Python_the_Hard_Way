import random
# from urllib import urlopen
import sys 

# Original assignment has url import, but I converted to txt file
# WORD_URL = "http://learncodethehardway.org/words.txt"
WORD_FILE = open ('words.txt', 'r' )
WORDS = []

PHRASES = {
	"class ###(###):" : "Make a class named ### that is-a ###.",
	"class ###(object):\n\tdef __init__(self, ***)" : "Class ### has-a __init__ that takes self and *** parameters.",
	"class ###(object):\n\tdef ***(self, @@@)" : "Class ### has-a function named *** that takes self and @@@ parameters.",
	"*** = ###()" : "Set *** to an instance of class ###.",
	"***.***(@@@)" : "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'" : "From *** get the *** attribute and set it to '***'."
	}
	
# Added Terminology
TERMS = {
		"class" : "- Tell Python to make a new kind of thing.",
		"object" : "- Two meanings: the msot basic kind of thing, and any instance of some thing.",
		"instance" : "- What you get when you tell Python to create a class.",
		"def" : "- How you define a function inside a class.",
		"self" : "- Inside the functions in a class, self is a variable for the instance/object being accessed.",
		"inheritance" : "- The concept that one class can inherit traits from another class, much like you and your parents.",
		"composition" : "- The concept that a class can be composed of other classes as parts, much like how a car has wheels.",
		"attribute" : "- A property classes have that are from composition and are usually variables.",
		"is-a" : "- A phrase to say that something inherits from another, as in a Salmon is-a Fish.",
		"has-a" : "- A phrase to say that something is composed of other things or has a trait, as in a Salmon has-a mouth."
		}
		
Keys = TERMS.keys()
		
# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
	
# load up the words from the website, NOW TXT FILE
# for word in urlopen(WORD_URL).readlines():
for word in WORD_FILE.readlines():
	WORDS.append(word.strip())
	
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("###"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		
	for sentence in snippet, phrase:
		result = sentence[:]
		
		# fake class names
		for word in class_names:
			result = result.replace("###", word, 1)
			
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
			
		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
		
	return results
	
# keep going until they hit CTRL-D
#CTRL-Z IN WINDOWS - TRIAL AND ERROR FINDING
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
				
			print question
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
			
			
			#Prints Study Terminology found in the answer, not elegant
			#Print Terms
			answer_lower = answer.lower()
			for k in answer_lower.split():
				if k in TERMS:
					print k, TERMS[k]
					print "\n"
except EOFError:
	print "\nBye"
					