"Optional Imports"
importCl = True
try:
	import click
except ModuleNotFoundError:
	importCl = False
"Imports"
import os
import random
"Varibles"
colors = ["red", "green", "yellow", "blue"]
"Functions"
def loadData(file="save"): # Load text files, line by line
	data = open(file+".txt", "r") # Opens up save file
	x = []
	for line in data:
		x.append(line) # Appends every entry by line
	for i in range(len(x)): # "Fixes" the entries
		y = x[i]
		x[i] = y[0:-1]
	data.close # Closes file
	data = x
	return data # Sends back collected data
def clearScreen(): # Clears the screen
	os.system('cls' if os.name == 'nt' else 'clear')
def addData(adding, file="save", append=True): # Adds data to the record or makes a new record
	if(append):
		data = open(file+".txt", "r+") # Opens data file
		x = loadData() # Gets the data pre record
		for i in range(len(x)):
			data.write(x[i] + '\n') # Writes old data to the now blank file
		data.write(adding) # Writes new data
		data.close # Closes file
	elif(not append):
		data = open(file+".txt", "r+") # Opens data file
		x = adding # Gets the data pre record
		for i in range(len(x)):
			data.write(x[i] + '\n') # Writes old data to the now blank file
		data.close # Closes file
	else:
		print("Error!")
def rainbow(text, nl=True, bold=True):
	if(not importCl):
		print("Error! You need to get click! pip3 install click!")
	elif(importCl):
		text = list(text)
		x = text[-1]
		text.pop(-1)
		for letter in text:
			click.secho(letter, bold=bold, nl=False, fg=random.choice(colors))
		click.secho(x, bold=bold, nl=nl, fg=random.choice(colors))
	else:
		print("Error!")