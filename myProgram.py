from externals import *
from database import *

#===========================SETUP====================================
print("Loading...")
path = "C:/Users/chris/Desktop/Bonnas/myProgram.py"
print("done - paths set")
#====================================================================

#===================GLOB VARS==========
count = 0
#======================================

#Create a menu with a colour scheme
def menu():
	printblue("_________MAIN MENU_________")
	printblue("[menu] Display Menu Options")
	printblue("[0] Logout")
	printblue("[1] Login")
	printblue("[2] Create Account")
	printblue("[3] DAB functionality")
	printblue("[4] Bonnas functionality")
	printblue("[opt] Options")
	printblue("===========================")

def bonMenu():
	global count
	if count == 1:
		printblue("[pwr] Power readings")
		printblue("[occ] Update house occupants")
	else :
		printred('error - login not sattisfied')

def pwrReading():
	global count
	if count == 1 :
		house = input("For which house are you recording a power reading? \n")
		reading = input("What was the meter reading that you recorded? \n")
	else :
		printred("error - login not sattisfied")
		
#Create a new account and save details to userDetails.csv
def createAcc():
	f = open("C:\\Users\\chris\\Desktop\\Bonnas\\login.csv", "a")
	f.write("\n" + input("Create a username: ") + ',' + input("Create a Password: "))
	printpurple("done - account Created and credentials saved")
	f.close()

#Login with login credentials from file
def login():
	global count
	if count == 1:
		printpurple("error - user already logged in")
	else :
		printpurple("=========LOGIN========")
		login_f = open("C:/Users/chris/Desktop/Bonnas/login.csv", "r")
		un = input("\nUsername: ")
		pw = input("Password: ")
		#get username and password from csv file
		for k in login_f.readlines():
			k = k.split(",")
			password = k[1]
			userName = k[0]
			password = password.strip()
			userName = userName.strip()
			#check entered username and password for name and password in file
			if un == userName:
				if pw == password:
					count = 1
			if count == 1 :
				printpurple("done - user " + userName + " logged in")
				break
		if count != 1 :
			count = count - 1
			printred("error - wrong credentials")
			login()
			if count == -3 :
				pass
		login_f.close()


def options():
	global count
	if count == 1:
		print("> To escape the program choose option '' and type yes when prompted if you want to exit.")
		print("> The default login details are 'admin' and 'admin'.")
	else :
		printred("error - login not sattisfied")
#==============================DAB================================
def dabMenu() :
	global count
	if count == 1:
		printblue("[dbConn] Connect to the database")
		printblue("[dbCls] Terminate the conncetion to the database")
		printblue("[dbApp] Add user to the database")
	else :
		printred("error - login not sattisfied")

#=================================================================


#Exit the prorgam and reset the login counter
def logout():
	global count
	count = 0
	printpurple("done - logged out")

menu()
loop = True
while loop:
	option = input("\n  -->   Option: ")
	if option == 'menu':
		menu()
	elif option == '0':
		logout()
	elif option == '1':
		login()
	elif option == '2':
		createAcc()
	elif option == '3' :
		dabMenu()
	elif option == '4':
		bonMenu()
	elif option == 'opt':
		options()
	elif option == '':
		if input("\n  -->   exit? ") == '': #tbd confirmation to exit
			exit()
	else:
		pass
