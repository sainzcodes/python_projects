#The following are examples on the syntax
empty_tuple = ()
print(empty_tuple)

#If you have more than one element, follow all but the last one with a comma:
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

#Tuples let you assign multiple variables at once: 
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a)
print(b)
print(c)

#If you have more than one element, follow all but the last one with a comma:
marx_tuple = 'Groucho', 'Chico', 'Harpo'

#You can use tuples to exchange values in one statement without using a temporary variable:

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password

#Iterate with for and in

Tuple iteration is like iteration of other types:

words = ('fresh','out', 'of', 'ideas')
for word in words:
     print(word)

#A list is made from zero or more elements, separated by commas and surrounded by square brackets:

empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]
randomness = ['Punxsatawney", {"groundhog": "Phil"}, "Feb. 2"}']

