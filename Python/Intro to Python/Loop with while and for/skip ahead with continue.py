while True:
	value = input("Integer, please [q to quit]: ")
	if value == 'q': 		#quit
		break
	number = int(value)
	if number % 2 == 0:		#an even number
		continue
	print(number, "square is", number*number)

