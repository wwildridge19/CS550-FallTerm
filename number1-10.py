import sys
import random

again = 'y'
while again =='y':

	x = random.randrange(1,101)
	#(int)(random.random()*10)+1 
	userinput = int(input('Guess the random number between 1 and 10: '))
	if x == userinput:
		print('you win!')
		y = False
	else:
		print('you lose. :(')

again = input('do you want to play again? y/n ')


'''import sys
import random

again = 'y'
while again =='y':

	x = random.randrange(1,101)
	#(int)(random.random()*10)+1 
	userinput = int(input('Guess the random number between 1 and 100: '))
	while userinput != x: 
		if userinput>x: 
			print('Too high')
		else:
			print('Too low.')

		userinput = int(input('Guess again: '))
	print ('You win!')
	again = input ('Do you want to play again? y/n')

print ('thanks for playing')'''


