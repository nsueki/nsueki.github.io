#jeff kim and nathan sueki
# definitions ******************************
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    #used to clear the screen
def intro():
	#Introduction
	print ("Welcome to the Dice Game! Here's how the game works:")
	print ("")
	print ("This is (obviously) a dice-based game, so heres the rules:")
	print ("")
	print ("1: If you roll less than a 5, you move back that much. Anything above, you move that much.") 
	print ("")
	print ("2: The goal is to reach 100 steps before the other players, so think wisely about your choices. With a bit of luck, you'll be on you're way to victory!")
	print ("")
	input("Press enter to continue!")
	cls()
	#intro function, just prints bunch of lines
def playerAmount(player):
	player = input("Please enter the amount of players that are playing(Up to four players):")
	while True:
		try:
			player = int(player)#trys to change the input into an int type
			if player == int(player):#if it is, check if the input is between 1 and 4
				if player > 0:
					if player <= 4:
						cls()
						return player
					else:#asks again until user inputs a number between 1 and 4
						cls()
						print ("Input a number between 1 and 4 please!")
						print ("")
						player = input("Please enter the amount of players that are playing(Up to four players):")
						
				else:#asks again until user inputs a number between 1 and 4
					cls()
					
					print ("Input a number between 1 and 4 please!")
					print("")
					player = input("Please enter the amount of players that are playing(Up to four players):")
		except ValueError:#if it can't be changed into an int type, asks user again until user puts in a valid number
			cls()
			print("That's not a number!")
			print("")
			player = input("Please enter the amount of players that are playing(Up to four players):")##gathers amount of player, between 1 and 4
def scoreKeeper(player,a,key):
	a = {}#Creates a dictonary variable to keep track of users and later on, score
	for i in range(1,player+1): #does plrAmt fnct once more, fix but still works
		key = ("Player" + str(i)) #looks ungly, fix later//dynamically makes keys to amount of players gathered from function playerAmount
		value = 0#set blank;will be updated with player score
		a[key] = value #create dictionary
	print (a)
	return a, key
def dice(die):
	while True:#loops
		roll = input("Press the enter key to roll the dice: ")
		if roll == "":
			die = random.randint(0,8)#randomly choose between a number between 0 and 8 
			print ("The dices rolled a " + str(die) + ".")
			if die >= 5:
				print ("Move forward " + str(die) + " steps.")#move foward when functions returns a number above or equal to 5
				while True:#lets player see results before moving on
					procede = input("Please press enter to continue!")
					if procede == "":
						return die
					else:
						cls()
						procede
					
			else:
				print ("Move back " + str(die) + " steps.")#move back when functions return a number lower than 5
				die = -die
				while True:#lets player see results before moving on
					procede = input("Please press enter to continue!")
					if procede == "":
						return die
					else:
						cls()
						procede
					
		else:#requires player to hit enter key
			cls()
			print ("Please press the enter key!")
			roll
def game(die,a,player,key):
	while True:
		for c in list(a.values()):
			if c < 99:#checks for score if less than 10;9because if you gwt 100, still win
				for i in range(1,player+1):#range of players returned from function playerAmount		
					key = ("Player" + str(i))	
					print (a)
					print ("It's Player ",i,"'s turn!")
					die = dice(die)#executes dice function
					a[key] += die#updates dictonary(score) according to appropriate player
					cls()
			else:
				print (key, "wins!")
				print (a)
				while True:
					closing = input("Press enter to exit the game!")
					if closing == (""):
						exit
					else:
						closing
# variables ********************************

player = 0
a = {}
die = 0
key = ""


#main **************************************

intro()
player = playerAmount(player)
a,key = scoreKeeper(player,a,key)
game(die,a,player,key)

