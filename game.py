#Choose your own adventure game!


from sys import exit
import os

os.system('cls')

# USE "RETURN" FUNCTION!!

score = 0


def pr_score(score):

	if score == 10:
		print "Your score 10! You do not, however, get back the time you wasted here. "
		exit(0)

	if score <= 3:
		print "Your score is %d out of 10. Humph! Pathetic." % score
		exit(0)

	if score >= 8:
		print "Your score is %d out of 10. Nice work." % score
		exit(0)

	else: 
		print "Your score is %d out of ten." % score
		print "A tepid effort, symptomatic of a feeble mind."
		exit(0)

def lib_game2(score):
	#print score
	score += 1
	os.system('cls')
	print "Do you:"
	print "a) play ROCK"
	print "b) play SCISSORS"
	print "c) play PAPER"

	ch_lib_game2 = raw_input (">")
	print "The Librarian plays SCISSORS."


	if ch_lib_game2 == "a":
		score += 2
		print "Rocks destroy scissors."
		print "You.... Win?"
		print "Umm... I never really gave much thought to what happens here."
		print "I mean, what was the pont of this game?"
		print "OK, how about this:"
		print "There's like, a chest with gold in it behind the librarians' desk."
		print "Press <enter> to open the box"
		Wait_input = raw_input (">")
		os.system('cls')
		print "You open the box!"
		print "It's full of gold, and jewls, and awesomeness!"
		print "But then the lid shuts on your head."
		print "You have died."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_lib_game2 == "b":
		print "Scissors don't beat scissors!"
		print "The Librarian eyes you kinda seductively, but then kills you."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		lib_game2(score)

	if ch_lib_game2 == "c":
		print "Paper is destroyed by Scissors."
		print "The librarian slams a book shut on you."
		print  "You died. And near the end too. Try again!"
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	lib_game(score)

def lib_game(score):
	os.system('cls')
	print "Do you:"
	print "a) play ROCK"
	print "b) play SCISSORS"
	print "c) play PAPER"
	print 'd) Say "Librarian? More like a... Hey can I borrow a rhyming dictionay?" '
	
	ch_lib_game = raw_input (">")
	print "The Librarian plays PAPER."

	if ch_lib_game == "a":
		print "Rocks are beaten by paper."
		print "The librarian shushes you. Permamently."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_lib_game == "b":
		print "Scissors cut paper!"
		print "The librarian almost says something, but remembers where she is."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		lib_game2(score)

	if ch_lib_game == "c":
		print "Paper doesn't beat paper."
		print "The librarian slams a book shut on you."
		print  "You died. And near the end too. Try again!"
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_lib_game == "d":
		print "The librarian looks at you..."
		print "'Death OVERDUE.'' She announces."
		print "You're dead. And so close to the end, too...."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	lib_game(score)

def final_room(score):

	print "You quietly enter the library."
	print "There is a librarian here."
	print "The librarian towers over you. She has glasses and a stern look."
	print "She says: 'You know the drill.'"
	print "You notice that she has blood coming from cuts on her fingers."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	lib_game(score)


def bank_door(score,):
	#print score
	print "You are in a room with a dead Banker slug thing in it."
	print "There are 3 exits."
	print "a) The door that leads back to the Bereaucrat."
	print "b) That damn 'Doom' door."
	print "c) A door marked 'Library'."

	ch_bank_door = raw_input (">")

	if ch_bank_door == "a":
		print "You go back. There's nothing there, but it makes me feel good about coding it."
		Have_MacGuffin = True
		ber_doors(score, Have_MacGuffin)


	if ch_bank_door == "b":
		print "An electric guitar starts playing franticly."
		print "Shit."
		print "You are fragged by player1."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)
		

	if ch_bank_door == "c":
		print "You go through the door into the library."
		print "SHHH!!!"
		final_room(score)
	
	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	ber_doors()

def bank_game2(score):
	score += 1
	#print score
	os.system('cls')
	print "Do you:"
	print "a) play ROCK"
	print "b) play SCISSORS"
	print "c) play PAPER"
	
	ch_bank_game2 = raw_input (">")


	if ch_bank_game2 == "a":
		print "The Banker plays PAPER."
		print "Rocks are eaten by paper. The Banker suffocates you with $100 bills."
		print "What a way to go."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_bank_game2 == "b":
		print "The Banker plays PAPER."
		print "Scissors beat paper!"
		print "The Banker shrivels up like a slug in salt."
		print "'Ha! Take that capitalist pig!'' You shout to nobody in particular."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		bank_door(score)

	if ch_bank_game2 == "c":
		print "The Banker plays PAPER."	
		print "Paper doesn't win against paper!"
		print "The Banker makes it rain so hard you're smothered."
		print "You really suck at this game, you know."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	bank_game2(score)

def bank_game(score):

	os.system('cls')
	print "Do you:"
	print "a) play ROCK"
	print "b) play SCISSORS"
	print "c) play PAPER"
	print 'd) Say "Too easy! Banker? More like WANKER!! High five!!" '
	
	ch_bank_game = raw_input (">")

	if ch_bank_game == "a":
		print "The Banker plays ROCK."
		print "Rocks don't beat rocks. The Banker crushes you and makes it rain on your corpse."
		print "Bam! Dead!."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_bank_game == "b":
		print "The Banker plays ROCK."
		print "Scissors are crushed by rocks!"
		print "The Banker knocks you across the room, and puts a dollar in your mouth."
		print "The Million Dollar Dream!"
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_bank_game == "c":
		print "The Banker plays ROCK."
		print "Paper somehow beats rock! You win!"
		print "The Banker focuses."
		print '"Well played. But I will win this time!" '
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		os.system('cls')
		bank_game2(score)

	if ch_bank_game == "d":
		print "The Banker stares."
		print "The banker declares 'Death and taxes, I'm afraid'."
		print "You die under a mountain of money." 
		#score = score +2
		pr_score(score)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	bank_game(score)

def bank_room(Have_MacGuffin, score): 
	print "You enter a room full of money, some sort of mad banker is here."
	print "He asks: 'Did you get the MacGuffin from the Kitty of Doom?'"
	print "a) Yes! Of course I did!"
	print "b) Umm, no... But..."
	print "c) Kitty of Doom? More like Kitty of... Umm, Headroom?"

	MacGuffin_q = raw_input (">")
	os.system('cls')

	if MacGuffin_q == "a" and Have_MacGuffin == True :
		print "Drat. Now I have to destroy you."
		print "The Banker holds up a fist full of dollars, then throws them in the air."
		print "It's time for rock, paper, scissors!!"
		print "Press <enter> to continue."
		#print score
		score += 1
		Wait_input = raw_input (">")
		os.system('cls')
		bank_game(score)

	if MacGuffin_q == "a" and Have_MacGuffin == False :
		print "The Banker yells: Liar! The 'Have_MacGuffin' flag is set to 'False'!!"
		print "I am INSIDE the code, punk!"
		print "He crushes you with piles of cash."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		os.system('cls')
		pr_score(score, Have_MacGuffin)

	if MacGuffin_q == "b" and Have_MacGuffin == True :
		print "The Banker yells: Liar! The 'Have_MacGuffin' flag is set to 'True'!!"
		print "You can't hide from me! I'm inside the code!"
		print "The Banker punches you and throws dollar bills on your corpse."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		os.system('cls')
		pr_score(score, Have_MacGuffin)

	if MacGuffin_q == "b" and Have_MacGuffin == False :
		print "The Banker furrows his brow and waves you back to the Bereaucrats office."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		os.system('cls')
		ber_doors(score, Have_MacGuffin)


	if MacGuffin_q == "c":
		print "The Banker is unamused."
		print "'Wait!' You say 'Banker? More like wa...'"
		print "Mercifully, the Banker kills you."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		os.system('cls')
		pr_score(score)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	bank_room(score)

def riddle_correct(score):
	score += 1
	#print score
	print "The cat swishes its' tail, then demands a scratch."
	print "The cat says: 'Meow, you're right.'"
	print "You have the MacGuffin!"
	print "You confidently head out of the exit, to the bank."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	os.system('cls')

	Have_MacGuffin = True
	bank_room(Have_MacGuffin, score)

def cat_riddle(score):
	print "Test line."
	guess_count = 2
	cat_threat = "none"
	riddle_answer = "none"
	
	while (guess_count > -1):

		riddle_answer = raw_input (">").lower()

		if "cheetah" in riddle_answer:
			riddle_correct(score)


		if guess_count == 0:
			cat_threat = "and attacks with giant flaming whip, sending you to Mandos."

		elif guess_count == 1 :
			cat_threat = "and wiggles its bum."

		elif guess_count == 2 :
			cat_threat = "and hisses."

		

		print "The cat looks displeased %s" % cat_threat # It's %s for the st %d!
		print "It says: You can guess, meow, %d more time(s)." % guess_count
	
		guess_count -= 1
	
	print "You havce died a horrible, horrible death."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	pr_score(score)

def MacGuffin_Room(score):
	score += 1
	#print score
	print "You are in the room of the MacGuffin."
	print "There is a small black cat here, that is also a powerful demonic entity."
	print "The cat speaks to you."
	print "Did I mention that the cat can talk?"
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	os.system('cls')
	print "Anyway, the cat tells you:"
	print "Meow. I know you're here for the MacGuffin. But to get it, you must answer my riddle."
	print "If you're wrong, you die, which is pretty standard for this game, really... Meow."
	print "But, to make your life easy, you get three guesses. Prr."
	print "So tell me, which cat don't you want to play games with?"
	cat_riddle(score)

def ber_doors(score, slide_used):
	print "You have a choice of 2 doors, in a room filled with bits of bereaucrat."
	print 'One is labeled  "DOOM!!" One is labeled "Bank office."'
	print 'There is also a slide labeled "MacGuffin". '
	print "Which door do you take?"
	print "a) Take the DOOM! door."
	print "b) Go to the bank."
	print "c) Take the slide to the MacGuffin."

	ch_ber_door = raw_input (">")

	if ch_ber_door == "a":
		print "You foolishly head to your doom."
		print "To be honest, the music is pretty good, but you're killed by that spider thing."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_ber_door == "b":
		print "You walk through a series of corridors to the Bank."
		Have_MacGuffin = False
		bank_room(score,Have_MacGuffin)

	if ch_ber_door == "c" and slide_used == False:

		print "You take the slide."
		print "Although several teeth are knocked out, you arrive in the MacGuffin room."
		slide_used = True
		MacGuffin_Room(score)

	if ch_ber_door == "c" and slide_used == True:
		print "Considering how many teeth you lost last time, you decide to not take the slide."
		ber_doors(score)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	ber_doors(score)

def bereaucrat_game_2(score):
	os.system('cls')
	print "Round two begins!"
	print "Do you play:"
	print "a) ROCK."
	print "b) PAPER."
	print "c) SCISSORS."
	ch_ber_game2 = raw_input (">")

	if ch_ber_game2 == "a":
		print "He plays PAPER."
		print "Your pathetic rock is covered with paper. What were you thinking?"
		print "You have died."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_ber_game2 == "b":
		print "He plays PAPER."
		print "Why give a bereaucrat more paper? You're dead now, fool."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_ber_game2 == "c":
		print "He plays PAPER."
		print "The bereaucrat plays paper. This hands you an easy win."
		print "The Bereaucrat explodes in a disgusting fountain of fat."
		slide_used = False
		ber_doors(score, slide_used)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	bereaucrat_game_2(score)

def bereaucrat_game(score):
	#print score
	score += 1
	print "You find yourself in a messy office."
	print "There is a bald, chubby man in a suit and tie here."
	print "He has a fat face, thick glasses, and poor hygene."
	print 'He speaks: "I am the Bereaucrat! I will void your permit to live!'
	print  "It's time to play Rock, Paper, Scissors."
	print "Press <enter> to continue."
	
	Wait_input = raw_input (">")
	os.system('cls')
	print "The bereaucrat licks his saussage lips."
	print "Do you:"
	print "a) Play ROCK."
	print "b) Play PAPER."
	print "c) Play SCISSORS."
	print "d) Say 'Bereaucrat? More like BereaFAT! Amirite?'"
	
	ch_ber_game = raw_input (">")
	os.system('cls')
	


	if ch_ber_game == "a":
		print "The Bereaucrat plays PAPER."
		print "Your silly rock is smothered by the paper."
		print "You die, the life slowly leaving your body."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_ber_game == "b":
		print "The Bereaucrat plays PAPER."	
		print "You cannot beat a bereaucrat attack with more paper."
		print "You are crushed under the mounds of paper."
		print "You have died a predictable death."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_ber_game == "c":
		print "The Bereaucrat plays PAPER."	
		print "Your scissors cut through paper!"
		print "The bereaucrat narrows his beady eyes."
		print "'I'll get you with my cunning next round!' He says."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		bereaucrat_game_2(score)

	if ch_ber_game == "d":
		print "The bereaucrat's fat face turns even more red."
		print "He shakes with range, and brings a giant VOID stamp down on your head."
		print "You're dead, but I'll give you bonus points for isulting the jerk."
		score +=3 
		pr_score(score)

	else:
		print "Please type a, b, or c."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		bereaucrat_game(score)



# This is the choice of doors you have in the rockbiter room. They lead to death or the beurocrat.

def rock_doors(score):
	#print score
	score += 1
	print "There are two doors."
	print "The door to the left is marked 'DOOM!' "
	print "The door on the right is marked 'Take this door' "
	print "Do you take:"
	print "a) The 'Doom' door."
	print "b) Or the other door?"
	ch_rock_door = raw_input (">")
	
	if ch_rock_door == "a":
		print "You walk down a long passageway..."
		print "There is a cyberdemon here. He looks angry."
		print "You have died a horrible, horrible death by rocket."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_rock_door == "b":
		bereaucrat_game(score)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	rock_doors(score)

#This is the second game of RPS you play against Rockbiter.
def rock_game2(score):
	print "Do you:"
	print "a) play ROCK"
	print "b) play SCISSORS"
	print "c) play PAPER"
	
	ch_rock_game2 = raw_input (">")
	
	if ch_rock_game2 == "a":
		print "Rockbiter plays ROCK."
		print "Rocks don't beat rocks. Rockbiter crushes your skull."
		print "You have died."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)
	
	if ch_rock_game2 == "b":
		print "Rockbiter plays ROCK."
		print "Scissors are destroyed by rocks!"
		print "Rockbiter smushes you between his hands."
		#print "Press <enter> to continue."
		#Wait_input = raw_input (">")
		pr_score(score)
	
	if ch_rock_game2 == "c":
		print "Rockbiter plays rock again? Who would have thunk it?"
		print "Rockbiter explodes into a pile of rubble!"
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		os.system('cls')
		rock_doors(score)

	else: 
		print "Please type a, b, or c."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		rock_game2(score)


#This is the game of RPS you play against the Rockbiter.
def rock_game(score):
	#print score
	score += 1
	os.system('cls')
	print "Do you:"
	print "a) play ROCK"
	print "b) play SCISSORS"
	print "c) play PAPER"
	print 'd) Say "ROCKBiter? More like COCKBiter! Amirite?" '
	
	ch_rock_game = raw_input (">")

	if ch_rock_game == "a":
		print "Rockbiter plays ROCK."
		print "Rocks don't beat rocks. Rockbiter crushes your skull."
		print "You have died."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_rock_game == "b":
		print "Rockbiter plays ROCK."
		print "Scissors are destroyed by rocks!"
		print "Rockbiter smushes you between his hands."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		pr_score(score)

	if ch_rock_game == "c":
		print "Rockbiter plays ROCK."
		print "Paper wraps rock! You win!"
		print "Rockbiter howls in frustration."
		print 'Rockbiter says: "I will get you this time!" '
		rock_game2(score)

	if ch_rock_game == "d":
		print "Rockbiter is not amused."
		print "Rockbiter rips you arms off."
		print "You're dead, and you haven't got very far. "
		print "but for the joke, I'll give you bonus points." 
		score += 2
		pr_score(score)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	rock_game(score)

#This is the room with the rockbiter in it. It's where you start.
def room_rock(score):
	score = 0
	#print score
	print "You wake up, feeling groggy and slow witted."
	print "So in other words, like yourself."
	print "You can:"
	print "a) Close your eyes and go back to sleep."
	print "b) Get up and look around."
	print "c) Quit and play a better game."
	
	ch_awake = raw_input (">")
	if ch_awake == "a":
		print "You go back to sleep, and wake up..."
		print "In the real world!"
		print "WOAH!"
		print "Your score is One, Neo."
		exit(0)

	if ch_awake == "b":
		score == score + 1 
		#print score
		print "You look around. You are in a large cave."
		print "There is a giant rock monster here."
		print "He looks terrifying."
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		os.system('cls')
		print "He speaks in a loud voice"
		print "I am ROCKBITER!! We will play rock, paper, scissors!"
		print "I will crush you in an AVALANCHE!!"
		print "Press <enter> to continue."
		Wait_input = raw_input (">")
		rock_game(score)
	
	if ch_awake == "c":
		print "To be honest, this is probably the closest you can come to winning."
		print "Press <Enter> to exit."
		Wait_input = raw_input (">")
		os.system('cls')
		exit(0)

	else: print "Please type a, b, or c."
	print "Press <enter> to continue."
	Wait_input = raw_input (">")
	#return score
	room_rock(score)

# cat_riddle()
room_rock(score)