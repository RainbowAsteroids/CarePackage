"""Imports"""
import os
import random
import sys
import hashlib
import binascii
import subprocess
"""Varibles"""
colors = ["red", "green", "yellow", "blue", "pink"]
flag = sys.argv[1:]
color = {
	"red":"\033[91m",
	"green":"\033[92m",
	"yellow":"\033[93m",
	"blue":"\033[96m",
	"pink":"\033[95m",
	"grey":"\033[90m",
	"exit":"\033[0m",
	"bold":"\033[1m"}
"""Classes"""
class hasher: # Upon request of Dylan Hamer, I am making this class. This class is about hashing your data and passwords
	def hashing(data): # Good for hashing files or strings
		if type(data) != str: # Makes sure the input data is indeed a string
			raise ValueError("Please use a string for inputted data!")
		return {"md5":hashlib.md5(bytes(data, "UTF-8")).hexdigest(), "sha1":hashlib.sha1(bytes(data, "UTF-8")).hexdigest(), "sha256":hashlib.sha256(bytes(data, "UTF-8")).hexdigest(), "sha512":hashlib.sha512(bytes(data, "UTF-8")).hexdigest()}
	def printout(data): # Prints out hashed strings or data
		hashes = hasher.hashing(data)
		print("MD5:", str(hashes["md5"]))
		print("SHA1:", str(hashes["sha1"]))
		print("SHA256:", str(hashes["sha256"]))
		print("SHA512:", str(hashes["sha512"]))
	class password: # Password part of the hasher class
		def make(password, salt=None, saltSpecific=False): # Hashes and salts passwords
			if type(password) != str:
				raise ValueError("Please make passwords strings only")
			if not saltSpecific:
			  salt = binascii.hexlify(os.urandom(64))
			password = binascii.hexlify(hashlib.pbkdf2_hmac('sha512', bytes(password, 'UTF-8'), salt, 1000000))
			return [str(password, "UTF-8"), str(salt, "UTF-8")]
		def save(username, password): # Saves passwords, salts, and usernames.
			if type(username) != str:
				raise ValueError("Please make usernames strings only")
			passfile = open("passwords/"+username+".txt", "x+") # Opens files for storing login data
			saltfile = open("salts/"+username+".txt", "x+")
			passnsalt = hasher.password.make(password) # Gets password hash and salt
			password = passnsalt[0]
			salt = passnsalt[1]
			passfile.write(password) # Saves username, password hash, and salt
			passfile.close()
			saltfile.write(salt)
			saltfile.close()
		def checkAccount(username):
			if type(username) != str:
				raise ValueError("Please make usernames strings only")
			return os.path.isfile("passwords/"+username+".txt")
		def login(username, password):
		  passfile = open("passwords/"+username+".txt", "r")
		  salt = open("salts/"+username+".txt", "r")
		  check = hasher.password.make(password, bytes(salt.read(), "UTF-8"), True)[0]
		  return passfile.read() == check
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
def rainbow(text, bold=True):
	text = list(text)
	x = text[-1]
	text.pop(-1)
	y = ""
	for letter in text:
		y += style(letter, bold=bold, fg=random.choice(colors))
	return y
def style(text, bold=False, fg):
	if not bold:
		return color[fg]+text+color["end"]
	elif bold:
		return color[fg]+color["bold"]+text+color["end"]
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
	if choice in range(len(choices)+2):
		return choice
	else:
		print("Invalid Option!!!")
def cmd(command, pipe=False):
	if not pipe:
		os.system(command)
	else:
		return subprocess.run(command.split(" "), stdout=subprocess.PIPE).stdout
def capitalize(string):
	y = ""
	string = string.split()
	string[0] = string[0].capitalize()
	for x in string:
		y += x
	return y
"""Rest of the Program"""
try:
	if sys.argv[1] == "-v" or "--version":
		if importCl:
			rainbow("CarePackage Terminal: 1.1.1")
			rainbow("CarePackage Module: 1.2.3")
except:
	pass 
