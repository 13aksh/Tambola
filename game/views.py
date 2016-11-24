# -*- coding: utf-8 -*-
from django.utils.encoding import smart_str
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def diction():
	d = {}
	d[1] = u'स्टेज'
	d[2] = u'शहनाई'
	d[3] = u'पायल'
	d[4] = u'बाराती'
	d[5] = u'गुलदस्ता'
	d[6] = u'स्वागत'
	d[7] = u'गहना'
	d[8] = u'सिन्दूर'
	d[9] = u'जोड़ी'
	d[10] = u'परिवार'
	d[11] = u'मंगलसूत्र'
	d[12] = 500
	d[13] = 1000
	d[14] = u'मुहूर्त'
	d[15] = u'पालकी'
	d[16] = u'श्रृंगार'
	d[17] = u'हल्दी'
	d[18] = u'गीत'
	d[19] = u'जूते'
	d[20] = u'महफ़िल'
	d[21] = u'मेहबूब'
	d[22] = u'बिंदिया'
	d[23] = u'चूड़ी'
	d[24] = u'मांग'
	d[25] = u'भाई'
	d[26] = u'जीजी'
	d[27] = u'भाभी'
	d[28] = u'जीजा'
	d[29] = u'सासूमाँ'
	d[30] = u'ससुरजी'
	d[31] = u'ससुराल'
	d[32] = u'मायका'
	d[33] = u'बाबुल'
	d[34] = u'रिश्ता'
	d[35] = u'प्यार'
	d[36] = u'साथी'
	d[37] = u'बुढ़ापा'
	d[38] = u'चुन्नू'
	d[39] = u'मुन्नू'
	d[40] = u'मौसा'
	d[41] = u'मौसी'
	d[42] = u'ताई'
	d[43] = u'ताऊ'
	d[44] = u'बन्नो'
	d[45] = u'मेहँदी'
	d[46] = u'साजन'
	d[47] = u'सजनी'
	d[47] = u'सालियाँ'
	d[48] = u'गजरा'
	d[49] = u'देवर'
	d[50] = u'जेठ'
	d[51] = u'ननद'
	d[52] = u'समाज'
	d[53] = u'पिया'
	d[54] = u'जोरू'
	d[55] = u'माँ'
	d[56] = u'मिठाइयां'
	d[57] = u'दूल्हा'
	d[58] = u'दुल्हन'
	d[59] = u'बहु'
	d[60] = u'दामाद'
	d[61] = u'मारवाड़ी'
	d[62] = u'साडी'
	d[63] = u'ज़ेवर'
	d[64] = u'कंगन'
	d[65] = u'घुंगरू'
	d[66] = u'चश्मा'
	d[67] = u'लड़की'
	d[68] = u'लड़का'
	d[69] = u'ख्वाब'
	d[70] = u'मिलन'
	d[71] = u'हमतुम'
	d[72] = u'सुख'
	d[73] = u'दुःख'
	d[74] = u'बंधन'
	d[75] = u'शगुन'
	d[76] = u'सुहाग'
	d[77] = u'सुहागन'
	d[78] = u'बेबी'
	d[79] = u'दुआ'
	d[80] = u'याद'
	d[81] = u'दंपत्ति'
	d[82] = u'लगन'
	d[83] = u'सुन्दर'
	d[84] = u'स्वैगर'
	d[85] = u'ढोलक'
	d[86] = u'सहेली'
	d[87] = u'लाडली'
	d[88] = u'रीति'
	d[89] = u'रस्म'
	d[90] = u'घर'
	return d



def index(request):
	html = """
	<div>
		<div></div>
	</div>
	"""
	return HttpResponse("papa")


def creatematrix():
	a = [ 0 for _ in range(9)]
	# Creating a random matrix of 90 numbers changing ten's place in every row
	for i in range(9):
		a[i] = [x for x in range((i*10+1),(i+1)*10+1)]
		a[i] = random.sample(a[i],10)
	# print a
	return a

def tickets(request, noticks):
	# Initializing the resultant ticket array
	b = []

	new = []

	# Input the required number of tickets
	n = int(noticks)#int(raw_input())

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
	dic = diction()
	for i in range(n):
		c[i] = [[0 for _ in range(9)] for y in range(3)]
		#print c[i]
		for j in range(3):
			#print b[i][j]
			for k in b[i][j]:
				if k<11:
					c[i][j][0] = dic[k]
				elif (k>10)and(k<21):
					c[i][j][1] = dic[k]
				elif (k>20)and(k<31):
					c[i][j][2] = dic[k]
				elif (k>30)and(k<41):
					c[i][j][3] = dic[k]
				elif (k>40)and(k<51):
					c[i][j][4] = dic[k]
				elif (k>50)and(k<61):
					c[i][j][5] = dic[k]
				elif (k>60)and(k<71):
					c[i][j][6] = dic[k]
				elif (k>70)and(k<81):
					c[i][j][7] = dic[k]
				elif (k>80)and(k<91):
					c[i][j][8] = dic[k]
	# for i in range(n):
	# 	for j in range(3):
	# 		print c[i][j]
	# 	print '\n'
	x = 1
	maamla = """
	<html>
	<head>
	<meta charset="UTF-8">
	</head>
	<body>"""
	for i in range(n):
		maamla += "<table border ='1' style='border-collapse: collapse'>"
		for j in range(3):
			# maamla += ["<td>"+str(c[i][j][x])+"</td>" for x in range(9) if c[i][j][x]!=0]
			maamla += "<tr>"
			for k in range(9):
				if c[i][j][k]!=0:
					maamla += "<td style='width: 50px; height:50px;'>"+smart_str(c[i][j][k])+"</td>"
				else:
					maamla += "<td style='width: 50px; height:50px;'></td>"
			maamla += "</tr>"
		maamla += "</table>"
		maamla += "<br>"
	maamla += "<table border ='1' style='border-collapse: collapse'>"
	a = creatematrix()
	for i in range(9):
		maamla += "<tr>"
		for j in range(10):
			maamla += "<td style='width: 50px; height:50px;'>"+smart_str(dic[a[i][j]])+"</td>"
		maamla += "</tr>"
	maamla += "</table>"
	maamla += "<br>"		
	maamla += "</body></html>"

	return HttpResponse(maamla)