def f():
	global s
	print(s)
	s = "Inside f"
	print(s)

# main code starts here
s = "Main code area"
f()
print(s)
