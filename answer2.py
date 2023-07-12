print ("Would you like to convert to hours or minutes?")
userInput = (input("> "))
if (userInput == ("h" or "hours")):
	print (userInput)
	print ("Enter minutes")
	userInput = int (input("> "))
	print (userInput/60, "hours.")
elif (userInput == ("m" or "minutes")):
	print ("Enter hours")
	userInput = int (input("> "))
	print (userInput*60, "minutes.")
else:
	quit