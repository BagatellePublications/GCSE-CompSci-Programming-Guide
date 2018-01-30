def report1(L):
    print ('-- report 1 --')

def report2(L):
    print ('-- report 2 --')

def report3(L):
    print ('-- report 3 --')

def reportMenu(L):
	while True:
		print ('1. Create report to match unique ID to surname')
		print ('2. Create report to identify girls and boys')
		print ('3. Create report to identify missing information')
		print ('4. Return to main menu')

		option = raw_input('Select an option : ')
		if option == '1':
			report1(L)
		elif option == '2':
			report2(L)
		elif option == '3':
			report3(L)
		elif option == '4':
			return
		else:
			print ('Not a valid choice - try again')

# main program starts here
reportMenu([])
