# Assigned the boolean value True to the variable named disaster
#Since furry and large are set to true, the selection result for the first return line will be It's a yeti!
furry = True
large = True
if furry :
	if large:
		print("It's a yeti!.")
	else:
		print("It's a cat!")
else:
	if large:
		print("It;s a whale!")
	else:
		print("It's a human. Or a hairless cat.")

# Assigned the boolean value True to the variable named disaster
#Since furry is set to true and large is set to false, the selection result for the second return line will be It's a cat!
furry = True
large = False
if furry :
	if large:
		print("It's a yeti!.")
	else:
		print("It's a cat!")
else:
	if large:
		print("It;s a whale!")
	else:
		print("It's a human. Or a hairless cat.")


# Assigned the boolean value True to the variable named disaster
#Since furry and large are set to False, the selection result for the third return line will be It's a human or a hairless cat!
furry = False
large = False
if furry :
	if large:
		print("It's a yeti!.")
	else:
		print("It's a cat!")
else:
	if large:
		print("It;s a whale!")
	else:
		print("It's a human. Or a hairless cat.")


# Assigned the boolean value True to the variable named disaster
#Since furry is set to true and large is set to False, the selection result for the fourth return line will be its a whale!
furry = False
large = True
if furry :
	if large:
		print("It's a yeti!.")
	else:
		print("It's a cat!")
else:
	if large:
		print("It's a whale!")
	else:
		print("It's a human. Or a hairless cat.")
