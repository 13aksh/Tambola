#tambola

import random

def creatematrix():
	a = [ 0 for _ in range(9)]
	# Creating a random matrix of 90 numbers changing ten's place in every row
	for i in range(9):
		a[i] = [x for x in range((i*10+1),(i+1)*10+1)]
		a[i] = random.sample(a[i],10)
	# print a
	return a
# Initializing the resultant ticket array
b = []

# Base list from which five elements will be chosen at random,
# and same will act as indexes in the ticket rows.
base = [x for x in range(9)]

new = []

# Input the required number of tickets
n = int(raw_input())

# Initialize the resultant array with zero for every ticket.
# Every element will become ticket after processing.
b = [0 for _ in range(n)]

# Looping for every random ticket.
for j in range(n):
	# Taking the fresh random matrix of 90 elements.
	a = creatematrix()

	# Defining the ticket array for rows
	aout = [ 0 for x in range(3)]
	for k in range(3):
		# Selecting five random numbers from base list, for indexes of rows.
		new = random.sample(base,5)

		#print new
		# Defining the ticket array for coloumns.
		ain = []

		#container element
		cont = -1
		# Looping each item as index of the random matrix for selection of one number in a tens range.
		for i in new:
			# Contains the index of the row
			cont = random.sample(range(len(a[i])),1)
			#print cont[0]
			
			cont = cont[0]
			
			#print cont
			
			# Appending to the ticket array of coloumns.
			ain.append(a[i][cont])
			
			#print a[i]
			
			# Deleting the element so it is not repeated
			del a[i][cont]
		aout[k] = ain
	#print aout
	b[j] = aout

for i in range(n):
	for j in range(3):
		print b[i][j]
	print '\n'