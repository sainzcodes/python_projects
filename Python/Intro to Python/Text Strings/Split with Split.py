#Split with split()
tasks = 'get gloves, get mask, give cat vitamins, call ambulance'
tasks.split(',')
tasks.split()

#Combine by Using join()
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)

#Substitute by Using replace()
setup = "a duck goes into a bar..."
setup.replace('duck', 'marmoset')
setup
setup.replace('a ', 'a famous ', 100)
setup.replace('a', 'a famous', 100)

#Combine by Using join()
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)

#Strip with strip()
world = "    earth   "
world.strip()
'earth'
world.strip(' ')
'earth'
world.lstrip()
'earth   '
world.rstrip()
world.strip('!')
blurt = "What the...!!?"
blurt.strip('.?!')

#Search and Select
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
poem[:13]
len(poem)
poem.startswith('All')
poem.endswith('That\'s all, folks!')
word = 'the'
poem.find(word)
poem.index(word)
word = 'the'
poem.rfind(word)
poem.rindex(word)
word = "duck"
poem.find(word)
poem.rfind(word)
poem.index(word)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found
poem.rfind(word)
poem.rindex(word)
Traceback (most recent call last):
word = 'the'
poem.count(word)


