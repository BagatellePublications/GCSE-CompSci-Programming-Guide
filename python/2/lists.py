L = [3.14159, "Frederick", 12, [14, 23, "Thompson"], True]

print('Our list L holds the following items')
for item in L:
	print(item)

print("The second item (a string) consists of the following characters")	
for item in L[1]:
	print(item)
	
print("The list inside L holds the following items")
for item in L[3]:
	print(item)
