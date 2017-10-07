"Optional Imports"
importCl = True
importCo = True
try:
	import click
except ModuleNotFoundError:
	importCl = False
try:
	import coinmarketcap
except ModuleNotFoundError:
	importCo = False
"Imports"
import os
import random
import sys
"Varibles"
colors = ["red", "green", "yellow", "blue"]
"Functions"
def version():
	CarePackage.rainbow("CarePackage Terminal: 1.0")
	CarePackage.rainbow("CarePackage Module: 1.1")
def loadData(file="save"): # Load text files, line by line
	if file != str:
		raise ValueError("Please use a string for the file name!")
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
	if file != str:
		raise ValueError("Please use a string for the file name!")
	if(append):
		if adding != str:
			raise ValueError("Please use a string for the adding!")
		data = open(file+".txt", "r+") # Opens data file
		x = loadData() # Gets the data pre record
		for i in range(len(x)):
			data.write(x[i] + '\n') # Writes old data to the now blank file
		data.write(adding) # Writes new data
		data.close # Closes file
	elif(not append):
		if adding != list:
			raise ValueError("Please use a list for the adding!")
		data = open(file+".txt", "r+") # Opens data file
		x = adding[-1] # Gets the last thing in the data
		adding.pop(-1)
		for i in range(len(adding)):
			data.write(adding[i] + '\n') # Writes old data to the now blank file
		data.write(x)
		data.close # Closes file
	else:
		print("Error!")
def rainbow(text, nl=True, bold=True):
	if adding != str:
			raise ValueError("Please use a string for the text!")
	if(not importCl):
		print("Error! You need to get click! pip3 install click!")
	elif(importCl):
		text = list(text)
		x = text[-1]
		text.pop[-1]
		for letter in text:
			click.secho(letter, bold=bold, nl=False, fg=random.choice(colors))
		click.secho(x, bold=bold, nl=nl, fg=random.choice(colors))
	else:
		print("Error!")
def menu(choices, message="What is your choice? "):
	if type(choices) != list:
		print("Please put in a list of choices!")
	for i in choices:
		print(str(choices.index(i)+1)+".", i)
	return input(message)
"""Rest of the Program"""
try:
  if sys.argv[1] == "-v" or "--version":
	  if importCl:
		  rainbow("CarePackage Terminal: 1.0")
		  rainbow("CarePackage Module: 1.1")
	  else:
		  print("CarePackage Terminal: 1.0")
		  print("CarePackage Module: 1.1")
except:
  pass