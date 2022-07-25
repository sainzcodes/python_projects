guess_me = 7
number = 23
while True: 
	if number > guess_me:
		print("Too high")
		break
	elif number == guess_me:
		print("found it!")
		break
	elif  number < guess_me:
		print("Too low")
		break
number+=1
guess_me = 5
number = 1 
while True: 
	
