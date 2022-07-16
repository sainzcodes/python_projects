#check break use with else

word = 'Thud'
for letter in word:
	if letter == 'x':
		print("Eek! An 'x'!")
		break
	print(letter)
else:
	print("No 'x' in there.")