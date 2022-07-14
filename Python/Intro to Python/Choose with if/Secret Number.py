# Choose a number betweeh 1 and 10 and assig it to the variable secret
secret = 5

#Select another number betweeh 1 and 10 and assign it to the variable 
guess = 5

''' conditional tests (if, else, and elif) to print the string 'too low' if guess is less than 
	secret, 'too high' if greater than secret, and 'just right' if equal to secret.
'''

if guess > secret:
	print ('Too high.')
elif guess == secret:	
	print ('Just right')
else:
	print ('Too low.')

