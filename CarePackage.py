"""Optional Imports""""
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
"""Imports"""
import os
import random
import sys
import hashlib
import binascii
"""Varibles"""
colors = ["red", "green", "yellow", "blue"]
flag = sys.argv[1:]
"""Classes"""
class hasher: # Upon request of Dylan Hamer, I am making this class. This class is about hashing your data and passwords
	def hashing(data): # Good for hashing files or strings
		if type(data) != str: # Makes sure the input data is indeed a string
			raise ValueError("Please use a string for inputted data!")
		return {"md5":hashlib.md5(bytes(data, "UTF-8")), "sha1":hashlib.sha1(bytes(data, "UTF-8")), "sha256":hashlib.sha256(bytes(data, "UTF-8")), "sha512":hashlib.sha512(bytes(data, "UTF-8"))}
	def printout(data): # Prints out hashed strings or data
		hashes = hasher.hashing(data)
		print("MD5:", hashes["md5"])
		print("SHA1:", hashes["sha1"])
		print("SHA256:", hashes["sha256"])
		print("SHA512:", hashes["sha512"])
	class password: # Password part of the hasher class
		def make(password, salt=None, saltSpecific=False): # Hashes and salts passwords
			if type(password) != str:
				raise ValueError("Please make passwords strings only")
			if not saltSpecific:
			  salt = str(binascii.hexlify(os.urandom(64)))
			password = str(binascii.hexlify(hashlib.pbkdf2_hmac('sha512', bytes(password, 'UTF-8'), salt, 1000000)), "UTF-8")
			return [password, str(salt, "UTF-8")]
		def save(username, password): # Saves passwords, salts, and usernames.
			if type(username) != str:
				raise ValueError("Please make usernames strings only")
			passfile = open("passwords/"+username+".txt", "r+") # Opens files for storing login data
			saltfile = open("salts/"+username+".txt", "r+")
			passnsalt = hasher.password.make(password) # Gets password hash and salt
			password = passnsalt[0]
			salt = passnsalt[1]
			userfile.write(username) # Saves username, password hash, and salt
			userfile.close()
			passfile.write(password)
			passfile.close()
			saltfile.write(salt)
			saltfile.close()
		def checkAccount(username):
			if type(username) != str:
				raise ValueError("Please make usernames strings only")
			return os.path.isfile("password/"+username+".txt")
		def login(username, password):
		  password = open("passwords/"+username+".txt", "r")
		  salt = open("salts/"+username+".txt", "r")
		  check = hasher.password.make(password, bytes(salt.read(), "UTF-8"), True)[0]
		  return password.read() == str(check, "UTF-8")
		  
"""Functions"""
def version():
	CarePackage.rainbow("CarePackage Terminal: 1.0")
	CarePackage.rainbow("CarePackage Module: 1.1")
def loadData(file="save"): # Load text files, line by line
	if type(file) != str:
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
	if type(file) != str:
		raise ValueError("Please use a string for the file name!")
	if(append):
		if type(adding) != str:
			raise ValueError("Please use a string for the adding!")
		data = open(file+".txt", "r+") # Opens data file
		x = loadData() # Gets the data pre record
		for i in range(len(x)):
			data.write(x[i] + '\n') # Writes old data to the now blank file
		data.write(adding) # Writes new data
		data.close # Closes file
	elif(not append):
		if type(adding) != list:
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
	if type(adding) != str:
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
def menu(choices, message="What is your choice? ", exit=False):
	if type(choices) != list:
		print("Please put in a list of choices!")
	for i in choices:
		print(str(choices.index(i)+1)+".", i)
	if exit:
		print("0. Exit")
	try:
		choice = int(input(message))
	except:
		print("Please input a number.")
	if choice in range(len(choices)):
		return choice
	else:
		print("Invalid Option!!!")
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