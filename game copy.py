'''on my honor, I did not give nor recieve unauthorized aid.'''
#Surviving the night
#William Wildridge october 10 
#basic game with if statements and variable changes 
import sys
import random 
#This is just basic importing. Although, at first I forgot that I did not have
#to import random so I kept getting a error with random. 


funds_value = 30.00
'''if had more time i would have had more ways to use the money you can make or more choices 
of how to use the money. '''
def lottery():
	global funds_value
	'''At first I tried assigning variables to every different funds_value and set up
	different variables for the various different routes throughout the program. At 
	extra help Ms. Healey told me about global funds_value. I also did some research
	after about global and local variables and read this link: 
	https://www.python-course.eu/python3_global_vs_local_variables.php. Although this
	did not actually change any of my coding it helped me understand the coding better.'''
	lotresult = random.random() * 100
	'''Kept getting error messages because random.random() does not have parameters and
	I was trying to define it originally with parameters random.random(1,100). I used our
	coin flip project trying to piece this together. I used 
	https://docs.python.org/3/library/random.html trying to understand rand.range,
	but I liked just multiplying by 100 better.'''
	#this is just some more user input I thought was interesting
	while True: 
		try:
			luckynumber = int(input('what is your lucky number'))
			break
		except ValueError:
			print('please pick a number')
			'''needed some major help with this while true loop from Ms. Healey'''
	while int(luckynumber) > 100 or int(luckynumber)< 0:
		'''at first I had this be any value, but I realized I had to limit the numbers to
		the restricrtions of 1 - 100. I did this using a simple or statement, however at
		first I just had ">100 or <0" this did not work for values under 0, and so i had
		to edit and ask at extra help and now realize i have to put the variable twice'''
		luckynumber = input('a number between 1 and 100')
	print (int(lotresult))
	#Had people try and used their input which was display the number that was found so this does that 
	if int(lotresult) == luckynumber:
		print(win)
		funds_value = funds_value + 1000
		print ((funds_value) + '$ remaining')
	'''at first I tried to do the win vs lose with an elif statement assigning win a variable and
	lose a variable and then evaluating them based on the variable. However, when I was doing 
	Code academy I realized I don't need to do this and just the two results can be 
	represented in a single if statement. '''
	print ('you lose :(')
	funds_value = funds_value - 2 
	if funds_value == 0: 
		return 'no' 
	'''This was just a simple add that Ms. Healey helped me with during last day of 
	game.'''
	print ((str(funds_value)) + '$ remaining')
	lotterychoice= input ('would you like to play again?')
	while lotterychoice != 'yes' and lotterychoice != 'no':
		lotterychoice= input('yes or no answer')
	if lotterychoice == 'yes':
		lottery()
	'''I'm proud that I got this lottery function to work. I spent a lot of time 
	reviewing the random functions that we had done in class and reasearching other
	functions online. In the end I was able to get it to work succesfully and repeat as many times 
	as you want and it's the most interesting part of the game in my opinion. '''

def convenientstore(): 
	global funds_value
	print('you leave the motel and see a convenient store. Your stomach growls and you decide to go.')
	food = input('would you like beef jerkey or potato chips')
	'''Would have like to make this a few more choices but am happy that I got a real 
	life applicable choice into the game. I would have liked this convenient store to have
	more lively and add more characters as well, but I am happy in its reduced simple form'''
	food.lower()
	'''I tried here to do an insurace that if they capitalized a part of their input that it would be lower case
	later as a type of user check. This was in the Code academy program in functions'''

	
	while  food != ("beef jerkey") and food !="potato chips":
	
		print('they dont sell that and you need food!')
		food = input('what would you like?')

	funds_value = funds_value - 6
	print('there goes 6 dollars ' + str(funds_value) + '$ remaining')

	lotterychoice = input('would you like to buy a lottery ticket?')
	while lotterychoice != 'yes' and lotterychoice != 'no':
		lotterychoice = input('yes or no') 
	if lotterychoice == 'yes':
		print("Go to lottery!")
		lottery()
	

def hotel1():
	global funds_value
	print ('Welcome to the Drrrrrrive in Motel!')
	name = input('Can I have your name please?')
	party_size = input ('How many people are in your party?')
	while True:
		try: 
			party_size = int(party_size)
			break 
			'''Ms. Healey helped me with the try function, but this was especially difficult 
			for me at first especially with syntax.'''
		except ValueError:
			party_size = input('please input a number')
		'''Ms. Healey helped me a lot on this loop. I was not quite sure how to use the 
		while True loop, because I did not get the exact implications of what true meant. 
		I used this basic page to understand while loops and while True loops more:
		https://wiki.python.org/moin/WhileLoop'''

	if int (party_size) > 4:
		print ('hello ' + str(name) +', Unfortunately, we only have one room available; you will have to find another motel.')
		convenientstore()
	'''niquil (one of my friends) helped me a little with syntax and sending to other 
	functions'''

	if int(party_size) <= 0:
		print ('silly goose...')


	elif int (party_size) <= 4:
		print ('hello ' + str(name) + ', okay, we will put you in a room.')
		print ('the room will cost you 22$ a night')
		stayinhotel = input ('would you like to stay the night?')
		while stayinhotel != 'no' and stayinhotel != 'yes':
			stayinhotel = input('yes or no')
	

		if stayinhotel == 'no':
			print ('Ok, have a nice night')
			convenientstore()
		elif stayinhotel == 'yes':
			print ('your room number is 14')
			funds_value= funds_value - 22 
			print ('you have lost some money! be careful!' + str(funds_value) + '$ left')
			convenientstore()
		''' I was most proud of this being able to send to different functions at different points
		in the actual function itself at different times.'''
	




# -------------------------
#  Main Code
# -------------------------

print('you and your friends find yourselves in the middle of tennessee during your 30 hour drive down the east coast. Tired you pull over to a local motel and approach the concierge. You only have 30 dollars so be careful!!')
hotel1()
print ('game over... come back for more later')


'''with this project I found my main problems were with syntax and coding basics. As a result I 
spent a lot of my time relearning and prefecting my sintax and the basics. I used Code academy 
lessons 1-8 which helped me with functions, a touch of loops, inputs and basic syntax. Although, this 
seems simple to me now it was rather daunting when I got syntax error and had no idea where
my mistakes were in the beggining. I am proud of this project. I spent a long time on it. Although, it seems 
rather simple it took a long time and I am happy I have a playable type game now. I would in the future 
like to come back and make the game more advanced and fun to play with (once I finish the rest of code academy or 
further in the year) but I am happy with the fact that I made something playable.''' 

