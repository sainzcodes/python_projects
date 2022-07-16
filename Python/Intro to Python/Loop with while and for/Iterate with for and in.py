#To show iteration we need somethign to iterate over. It is legal to step through a string like this:

word = 'Santiago'
offset = 0 
while offset < len(word):
	print(word[offset])
	offset += 1


#This is the lean version of the code

For letter in words:
	print(letter)