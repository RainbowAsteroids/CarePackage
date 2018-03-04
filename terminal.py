"""Imports"""
import CarePackage
import os
"""Classes"""
class login:
	def create():
		skip = False
		while not skip:
			username = input("What do you want your username to be? (Type \"exit\" to exit) ")
			if username == "exit":
				skip = True
			elif CarePackage.hasher.password.checkAccount(username):
				print("Error! That username is taken!")
			else:
				break
		if not skip:
			CarePackage.hasher.password.save(username, input("What do you want your password to be? "))
			CarePackage.clearScreen()
	def signin():
		skip = False
		while not skip:
			username = input("What is your username? (Type \"exit\" to exit) ")
			if username == "exit":
				skip = True
			elif CarePackage.hasher.password.checkAccount(username):
				break
			else:
				print("Error! That user does not exist!")
		while not skip:
			password = input("What is your password? (Type \"exit\" to exit) ")
			CarePackage.clearScreen()
			if password == "exit":
				skip = True
			elif CarePackage.hasher.password.login(username, password):
				print("Welcome", username+"!")
				break
			else:
				print("Error! Wrong password!")
	def delete():
		skip = False
		while not skip:
			username = input("What is your username? (Type \"exit\" to exit) ")
			if username == "exit":
				skip = True
			elif CarePackage.hasher.password.checkAccount(username):
				break
			else:
				print("Error! That user does not exist!")
		while not skip:
			password = input("What is your password? (Type \"exit\" to exit) ")
			CarePackage.clearScreen()
			if password == "exit":
				skip = True
			elif CarePackage.hasher.password.login(username, password):
				os.remove("passwords/"+username+".txt")
				os.remove("salts/"+username+".txt")
				break
			else:
				print("Error! Wrong password!")
"""Functions"""
def commandHandler(command):
	command = command.split(" ")
	if command[0] == "help":
		helpText()
	elif command[0] == "version":
		version()
	elif command[0] == "rainbow":
	  try:
		  CarePackage.rainbow(command[1])
	  except IndexError:
		  print("Usage: rainbow [TEXT]")
	elif command[0] == "hash":
	  try:
		  if command[1] == "file":
			  CarePackage.hasher.printout(open(command[2]).read())
		  elif command[1] == "string":
			  CarePackage.hasher.printout(command[2])
	  except IndexError:
	    print("Usage: hash <file/string> [FILENAME/TEXT]")
	elif command[0] == "login":
		loginMode()
	elif command[0] == "signoff":
		signOff()
	elif command[0] == "exit":
		leave()
	else:
		print("Error! Command not found!")
def version():
	if CarePackage.importCl:
		CarePackage.rainbow("CarePackage Terminal: 1.0")
		CarePackage.rainbow("CarePackage Module: 1.1")
	else:
		print("CarePackage Terminal: 1.0")
		print("CarePackage Module: 1.1")
def helpText():
	version()
	print()
	print("""
	Command list:
	
	help - Prints helptext - help
	version - Prints the version of this program - version
	rainbow - Prints the desired text in rainbow. Requires click - rainbow [TEXT]
	hash - Prints hashes of a string or file - hash <file/string> [FILENAME/TEXT]
	login - Puts the terminal into login mode - login
	signoff - Gives the signoff message - signoff
	exit - exits the terminal - exit
	
	As more functions are added to CarePackage, more cool commands will be available.
	""")
	signOff()
def signOff():
	if CarePackage.importCl:
		CarePackage.rainbow("Happy Programming!")
	else:
		print("Happy Programming!")
def leave():
	CarePackage.clearScreen()
	signOff()
	exit()
def loginMode():
	while True:
		option = CarePackage.menu(["Login", "Create a New Account", "Delete Account"], exit=True)
		if option == 0:
			break
		elif option == 1:
			login.signin()
		elif option == 2:
			login.create()
		elif option == 3:
			login.delete()
"""Rest of the Program"""
CarePackage.clearScreen()
try:
	while(True):
		commandHandler(input(">>> "))
except KeyboardInterrupt:
	CarePackage.clearScreen()
	signOff()
	exit()
