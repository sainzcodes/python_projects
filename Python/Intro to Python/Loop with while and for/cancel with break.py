''' To use a loop that will cancel until something happens, an infinite loo with a break
statement can be used. Te following eexample reads a line of input from the keyboard via 
Python's input() function and then prints it with the first letter capitalized. The loop breaks
when the letter 'q' is typed

while True:
	stuff = input("String to capitalize [type q to quit]: ")
	if stuff == "q":
		break
	print(stuff.capitalize())

'''
''' A break in a for loop breaks out of the loop, as it does for a while loop:
'''
word = 'thud'
for letter in word:
	if letter == 'u':
		break
	print(letter)