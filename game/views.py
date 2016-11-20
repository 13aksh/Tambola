from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

#def index(request):
#	return HttpResponse("papa")


def creatematrix():
	a = [ 0 for _ in range(9)]
	# Creating a random matrix of 90 numbers changing ten's place in every row
	for i in range(9):
		a[i] = [x for x in range((i*10+1),(i+1)*10+1)]
		a[i] = random.sample(a[i],10)
	# print a
	return a

def index(request):
	# Initializing the resultant ticket array
	b = []

	new = []

	# Input the required number of tickets
	n = 500#int(raw_input())

	# Initialize the resultant array with zero for every ticket.
	# Every element will become ticket after processing.
	b = [0 for _ in range(n)]


	#Final ticket
	c = [0 for _ in range(n)]

	# Looping for every random ticket.
	for j in range(n):
		# Taking the fresh random matrix of 90 elements.
		a = creatematrix()

		# Base list from which five elements will be chosen at random,
		# and same will act as indexes in the ticket rows.
		base = [x for x in range(9)]

		# Defining the ticket array for rows
		aout = [ 0 for x in range(3)]
		for k in range(3):
			# Selecting five random numbers from base list, for indexes of rows.
			
			if k == 1:
				temps = []
				templ = []
				for x in range(9):
					if len(a[x]) == 10:
						temps.append(x)
					else:
						templ.append(x)
				new = random.sample(temps,4)
				new += random.sample(templ,1)
			else:
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

				if len(a[i])<9:
					for g in range(len(base)):
						if base[g] == i:
							del base[g]
							break
			aout[k] = ain
		#print aout
		b[j] = aout

	for i in range(n):
		c[i] = [[0 for _ in range(9)] for y in range(3)]
		#print c[i]
		for j in range(3):
			#print b[i][j]
			for k in b[i][j]:
				if k<11:
					c[i][j][0] = k
				elif (k>10)and(k<21):
					c[i][j][1] = k
				elif (k>20)and(k<31):
					c[i][j][2] = k
				elif (k>30)and(k<41):
					c[i][j][3] = k
				elif (k>40)and(k<51):
					c[i][j][4] = k
				elif (k>50)and(k<61):
					c[i][j][5] = k
				elif (k>60)and(k<71):
					c[i][j][6] = k
				elif (k>70)and(k<81):
					c[i][j][7] = k
				elif (k>80)and(k<91):
					c[i][j][8] = k
	# for i in range(n):
	# 	for j in range(3):
	# 		print c[i][j]
	# 	print '\n'
	x = 1
	maamla = "<body>"
	for i in range(n):
		maamla += "<table border ='1' style='border-collapse: collapse'>"
		for j in range(3):
			# maamla += ["<td>"+str(c[i][j][x])+"</td>" for x in range(9) if c[i][j][x]!=0]
			maamla += "<tr>"
			for k in range(9):
				if c[i][j][k]!=0:
					maamla += "<td style='width: 80px; height:80px;'>"+str(c[i][j][k])+"</td>"
				else:
					maamla += "<td style='width: 80px; height:80px;'></td>"
			maamla += "</tr>"
		maamla += "</table>"
		maamla += "<br>"
	maamla += "</body>"
	return HttpResponse(maamla)