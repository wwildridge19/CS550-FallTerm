import sys 
from random import randint 
import time 
# did not understand why time function wasnt working so I had to work on it and figure it out so it would work... turns out to be a simple mistake of not importing time
class Chosen:
	def __init__(self, health, attack, luck, money, thetype):
		#special method
		self.health = health 
		self.attack = attack
		self.luck = luck 
		self.money = money 
		self.thetype = thetype

		'''Just simple definition of the class although simple it took me a little while to understand
		I looked on line to figure out some good basic stats to give and had to think it all through 
		before writing class and how i would do the fighting (aka luck stat) '''
		
	def __str__(self): 
		global result
		result = ("stats:\n")
		result += ("health:" +str(self.health)+'\n')
		result += ("attack:" +str(self.attack) + '\n')
		result += ("luck:" + str(self.luck) + '\n')
		result += ("money:" + str(self.money))
		return result
		'''just defining stats pretty basic'''
class Dragon: 	
	def __init__(self):
		#special method
		self.health = randint(1,10) 

	def __str__(self):

		result = (" DRAGON health:" +str(self.health))
		return result
		'''making a dragon so i can fight him, pretty happy that i got both my classes working well and understandable for me
		happy with the result of the two'''


def sleep(): 
	sleepforsure = input("sleeping will help you gain health but you lose money for the hotel rent! are you sure you want to sleep? \n")
	if sleepforsure == 'yes':
		print ('zzzzz') 
		time.sleep(5)
		'''function I had to find not very complicated just an interesting addition pretty happy with it because it makes sense with sleeping and it adds a little bit of depth to the game'''
		character.health += randint(1,3)
		character.money -= 1  
		'''editing the character was a little difficult for me because originally i had chosen.health which meant 
		that chosen.health wasnt defined which i had trouple understanding. However, I figured out that I needed to 
		do character. which allowed me to edit the stats of my character as i go. '''
		print(character)
		option()
	if sleepforsure == 'no':
		option()
		'''recalling option() allowed me to feel like i had a better game that wasnt only one branch but instead had multiple options'''

def lottery():
	'''for this function I went and looked back at previous project althoguh rewriting it would have been 
	simpler because its pretty simple.'''
	lotterynumber = randint(1,5)
	print ('your lottery number is ' + str(lotterynumber))
	'''the theme of picking a number and comparing it to a random number is something i used throughout the whole game 
	so I like that I used it for this as well.'''
	if lotterynumber ==5: 
		print ('Phew it worked!')
		character.money += 3
	else: 
		print ('it didnt work :(')
		character.money -= 1 
		'''How well you do against the bigger stronger dragons really depends on how much potions you have meaning how much money 
		you have so the only way to really beet the biggest dragon is get lucky against smaller dragons building up more money or win this lottery '''

def potionstore(): 
	while character.money > 0: 
		potionselection = input('what would you like to buy \n Rapid Attack \n Quick Heal \n Leprechaun Luck \n Gambling Grinch \n')
		if potionselection == 'rapid httack':
			character.attack += 1 
			character.money -= 1 
		if potionselection == 'quick heal':
			character.health += 1 
			character.money -= 1 
		if potionselection == 'leprechaun luck':
			character.luck -= 1
			character.money -=1
		if potionselection == 'gambling grinch':
			lottery()
		print (character)
	option()
	'''pretty happy that this works for me. A couple potions with different things they each do I think is pretty cool and allows you to have a personalized game
	I liked this for its ability to make the game more interesting.'''

def whogoesfirst():
	whoattacksfirstdrag = randint(1,2) 
	print('here comes the dragon!')
	whoattacksfirstyou = input('pick a number 1 or 2 to decide who goes first \n')
	if whoattacksfirstyou == whoattacksfirstdrag:
		print ('you attack first!')
		return 'you'
	else: 
		print ('too bad the dragon will attack first')
		return 'dragon'
	'''this was just another interesting addition I added. One of my main goals for this project was to have a lot of interaction making it more intereting 
	and so I like this because it gives the user more to do.'''

def fight(): 
	dragon = Dragon()
	askwho = True
	first=''
	while character.health > 0 and dragon.health > 0 :
		if askwho: 
			first = whogoesfirst()
			askwho = False
		print (character)
		print (dragon)
		if first == 'you': 
			print('-------YOU-------', first)
			print ('get ready to attack')
			luckchoice = randint (1, int(character.luck))
			fightchoice = input('guess your number between 1 and your luck score. your luck score is:' + str(character.luck))
			if luckchoice ==  fightchoice: 
				print(dragon.health, character.attack)
				print ('you hit him')
				dragon.health -= character.attack
				first = ('dragon')
		if first == 'dragon':
			print('-------DRAGON-------', first) 
			print('Get ready to defend its the dragons turn')
			dragonattack = randint(1,2)
			deffend = input('guess your number (1 or 2)')
			print('you guessed ' + str(deffend))
			print('he attacked with' + str(dragonattack))
			if dragonattack != deffend: 
				print ('you have been burned!')
				character.health -= 1
				first = ('you')
		if character.health < 1: 
			print ('you lose')
		if dragon.health < 1: 
			print ('you defeated the dragon')
			character.money += 2
			option()
			'''this was the biggest part of the game and i got it working and i am really happy it works. 
			I had a lot of probelms with getting this to work but I am happy it does. One of the most confusing 
			things was getting the turns to alternate but I asked you and then we got it to work and now it works 
			well allowing you to fight the dragon and have a part in the random battle'''

def option():
	action = input('What would you like to do? \n fight \n potion store \n sleep \n')
	action.lower()
	if action == 'fight':
		fight()
	if action == 'potion store':
		potionstore()
	if action == 'sleep':
		sleep()
	'''just some basic like homescreen kind of options that i returned to as the baseling of the project'''




def class_choice():
	global character
	class_choice = input('Which class would you like? \n Warlock \n Barbarian \n Knight \n Assasin \n')
	class_choice.lower()

	while True:
		if class_choice != 'warlock' or 'barbarian' or 'knight' or 'assasin':
			input('Which class would you like? \n Warlock \n Barbarian \n Knight \n Assasin \n')
		if class_choice == 'warlock' or 'barbarian' or 'knight' or 'assasin':
			if class_choice == 'warlock':
				character = Chosen(2,3,2,2, "warlock") 
				print('You are a Warlock your stats are:')
			if class_choice == 'barbarian':
				character = Chosen(3,3,4,2, "barbarian") 
				print('You are a Barbarian your stats are:')
			if class_choice == 'knight':
				character = Chosen(2,3,4,3, "knight") 
				print('You are a Knight your stats are:')
			elif class_choice == 'assasin':
				character = Chosen(1,4,2,2, "assasin") 
				print('You are an Assasin your stats are:')
	print(character)
	'''defining the different characters. this made me happy because i was able to really use the classes that i set up and define different characters.'''

'''ideas that i tired to use: 
print to console 
using user input
casting different intergers as strings 
lots of if statements 
while loops 
lots of functions 
some lists 
classes'''

'''overall I am pretty happy with the result of this project although it is far from my best, i put a good amount of time into it however not as much as usual 
and wish i had more time to do more error checking because i think it is incomplete without it'''
#_________________________main code__________________________

class_choice()
option()
# if chosen.thetype=="warrior"




	


		



