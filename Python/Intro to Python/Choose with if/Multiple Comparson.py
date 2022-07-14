#the First method of comparison is by writting a long if statement
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
	or letter == 'o' or letter == 'u':
	print(letter, 'is a vowel')
else:
	print(letter, 'is not a vowel')

#The second method is by using the python's membership operator in, instead
vowels = 'aeuiu'
letter = 'o'
letter in vowels
if letter in vowels:
	print (letter, 'is a vowel')