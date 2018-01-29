def secure(password):
	nums = set('0123456789')
	caps = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	foundNumber = False
	foundCaps = False

	for n in password:
		if (n in nums):
			foundNumber = True
		if (n in caps):
			foundCaps = True

	if foundNumber and foundCaps:
		return True
	else:
		return False

def getPassword():
	while True:
		password = input('Enter Password : ')
		if secure(password):
			return password
		else:
			print("%s must contain at least one number and one capital letter" %(password))

# main code starts here
username = input('Enter username : ')
password = getPassword()
print ("Username %s has password %s." %(username, password))
