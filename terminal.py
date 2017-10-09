"""Imports"""
import CarePackage
import os
"""Classes"""
class login:
	def create():
		while True:
			username = input("What do you want your username to be? ")
			if CarePackage.hasher.password.checkAccount(username):
				print("Error! That username is taken!")
			else:
				break
		CarePackage.hasher.password.save(username, input("What do you want your password to be? "))
		CarePackage.clearScreen()
	def signin():
		while True:
			username = input("What is your username? ")
			if CarePackage.hasher.password.checkAccount(username):
				break
			else:
				print("Error! That user does not exist!")
		while True:
			password = input("What is your password? ")
			CarePackage.clearScreen()
			if CarePackage.hasher.password.login(username, password):
				print("Welcome", username+"!")
				break
			else:
				print("Error! Wrong password!")
	def delete():
		while True:
			username = input("What is your username? ")
			if CarePackage.hasher.password.checkAccount(username):
				break
			else:
				print("Error! That user does not exist!")
		while True:
			password = input("What is your password? ")
			CarePackage.clearScreen()
			if CarePackage.hasher.password.login(username, password):
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
		CarePackage.rainbow(command[1])
	elif command[0] == "hash":
		if command[1] == "file":
			CarePackage.hasher.printout(open(command[2]).read())
		elif command[1] == "string":
			CarePackage.hasher.printout(command[2])
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