"""Imports"""
import CarePackage
"""Functions"""
def commandHandler(command):
	command = command.split(" ")
	if command[0] == "help":
		helpText()
	elif command[0] == "version"
		version()
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
	
	help - Prints commands
	version - Prints the version of this program
	rainbow - Prints the desired text in rainbow. Requires click - rainbow [TEXT]
	
	As more functions are added to CarePackage, more cool commands will be available.
	""")
	signOff()
def signOff():
	if CarePackage.importCl:
		CarePackage.rainbow("Happy Programming!")
	else:
		print("Happy Programming!")
def leave()
	signOff()
	exit()
"""Rest of the Program"""
try:
	while(True):
		commandHandler(input(">>>"))
except KeyboardInterrupt:
	signOff()
	exit()