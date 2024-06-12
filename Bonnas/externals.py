from colorama import init

init(autoreset=True)
YELLOW = "\x1b[0;33;40m"
RED = "\x1b[0;31;40m"
BLUE = "\x1b[0;34;40m"
PURPLE = "\x1b[0;35;40m"

def printblue(text):
	return print(f"\n{BLUE}{text}", end='')

def printred(text):
	return print(f"\n{RED}{text}", end='')

def printpurple(text):
	return print(f"\n{PURPLE}{text}", end='')

def printyellow(text):
	return print(f"\n{YELLOW}{text}", end='')
	