class Song(object):
	
	#self is required variable for class
	#this is to distinguish between instance and local variables
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you", 
				   "I don't want to get sued",
				   "So I'll stop right there"])
				   
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
						
###STUDY DRILL 1###

ridin_dirty = Song(["They see me rollin'",
					"They hatin'",
					"Patrollin'",
					"Tryin' to catch me ridin' dirty"])

ridin_dirty.sing_me_a_song()		

###STUDY DRILL 2###	
borntorun =  ["Will you walk with me out on the wire",
			    "Cause baby I'm just a scared and lonely rider",
				"But I gotta know how it feels",
				"I want to know if love is wild",
				"Babe I want to know if love is real"]
				
born_to_run = Song(borntorun)

born_to_run.sing_me_a_song()




