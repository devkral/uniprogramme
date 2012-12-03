#! /usr/bin/python3
import os
import sys
import math


hightolow=[]
lowtohigh=[]
tempdez=[]
tempdez.append("")
tempdez.append(0)
tempdez.append(0)
tempdez.append("")
tempdez.append(0)
tempdez.append(0)
 #0 1. Zahl, 1 1. Zahl nachkomma, 2 operator, 3  2. Zahl, 4 2. Zahl nachkomma

argslen=len(sys.argv)-1 #program arg1 arg2 args

def myhelp():
	print("usage:")
	print(sys.argv[0]+" <stellwertinput> <stellwertoutput> <…Ziffern des Zahlensystems>")


ausgabe35={
 0 : "0",
 1 : "1",
 2 : "2",
 3 : "3",
 4 : "4",
 5 : "5",
 6 : "6",
 7 : "7",
 8 : "8",
 9 : "9",
 10 : "A",
 11 : "B",
 12 : "C",
 13 : "D",
 14 : "E",
 15 : "F",
 16 : "G",
 17 : "H",
 18 : "I",
 19 : "J",
 20 : "K",
 21 : "L",
 22 : "M",
 23 : "N",
 24 : "O",
 25 : "P",
 26 : "Q",
 27 : "R",
 28 : "S",
 29 : "T",
 30 : "U",
 31 : "V",
 32 : "W",
 33 : "X",
 34 : "Y",
 35 : "Z"
}


eingabe35={v:k for k, v in ausgabe35.items()}

operators={
 "*" : "*", # part of sonder elements
 "/" : "/",
 "+" : "+",
 "-" : "-",
 "." : ",",
 "," : ","
}

if argslen < 3:
	print("error: too less arguments")
	myhelp()
	exit(1)
else:
	stellwertin=int(sys.argv[1])
	stellwertout=int(sys.argv[2])

listsepar=[] #low to high

for counter in range(argslen, 2, -1):
	if stellwertin<=36:
		for buchstabe in sys.argv[counter][::-1]: #invert because we calculate right to left
			if buchstabe.upper() in eingabe35:
				listsepar.append(eingabe35[buchstabe.upper()])
			elif buchstabe in operators:
				listsepar.append(operators[buchstabe.upper()])
			else:
				print(eingabe35[buchstabe.upper()])
				print("Error: unknown operator/digit, exit")
				exit(1)
	else:
		if sys.argv[counter] in operators: #operators
			listsepar.append(operators[sys.argv[counter].upper()])
		else:
			listsepar.append(int(sys.argv[counter]))



def toohighdigit(digit):
	print ("Error: Digit: "+str(digit)+" to high. Exit")
	exit(2)

def calczahl(zahlcalc):
	internlowtohigh=[]
	if zahlcalc<0:
		internlowtohigh.append("-")
		counter2=0
	else:
		counter2=-1
	while zahlcalc!=0:
		counter2+=1
		internlowtohigh.append(zahlcalc%stellwertout)
		zahlcalc=int((zahlcalc-internlowtohigh[counter2])/stellwertout)
	return internlowtohigh
	
	
#def getfloatingpoint(zahlcalc):
#	for counter in range(0,len(zahlcalc)):
	

ubertrag=0
position=1
print("(",end="")

for counter in range(0,len(listsepar)):
	#tempcl=len(listsepar)-(counter+1)
	#if listsepar[counter]>=stellwertin:
	#	toohighdigit(listsepar[counter])
		#if counter < len(listsepar) -1:
		#	temprest=listsepar[counter]%stellwertin
		#	listsepar[counter+1]+=(listsepar[counter]-temprest)/stellwertin
		#	listsepar[counter]=temprest
		#else:
		#	temprest=listsepar[counter]%stellwertin
		#	listsepar.append((listsepar[counter]-temprest)/stellwertin)
		#	listsepar[counter]=temprest
	if listsepar[counter] in operators:
		if operators[listsepar[counter]] == ",":
			tempdez[position+1]=counter
		else:
			#if the operators separate both numbers
			if counter!=0:
				position=4
		
			tempdez[position-1]=operators[listsepar[counter]]				
	else:
		tempdez[position]+=int(listsepar[counter]*(stellwertin**counter))
	#print(stellwertin**tempcl)

	if counter < len(listsepar)-1:
		print(str(listsepar[counter])+"*"+str(stellwertin)+"^"+str(counter), end="+")
	else:
		print(str(listsepar[counter])+"*"+str(stellwertin)+"^"+str(counter), end=")")
	
#ease calculations by taking the least after comma positions
#why calculating with 10: because the inputstellwersystem is the same
if tempdez[2]<=tempdez[5]:
	finalcounter=tempdez[5]-tempdez[2]
	tempdez[4]=tempdez[4]/(pow(10,finalcounter))
if tempdez[2]>tempdez[5]:
	finalcounter=tempdez[2]-tempdez[5]
	tempdez[1]=tempdez[1]/(pow(10,finalcounter))
print("/(10^"+str(finalcounter)+")")

#transform the comma position to the one of the target modulo system UNFINISHED
targetcountpre=math.log(pow(10,finalcounter))/math.log(stellwertout)
targetcount=math.trunc(targetcountpre)
print("Rounding error: "+str(targetcount-targetcountpre))
print(targetcountpre)

#if first number is negativ
if tempdez[0]=="-":
	tempdez[1]=tempdez[1]*-1

if tempdez[3]=="-":
	lowtohigh.append(calczahl(tempdez[1]-tempdez[4]))
if tempdez[3]=="+":
	lowtohigh.append(calczahl(tempdez[1]+tempdez[4]))
if tempdez[3]=="/":
	lowtohigh.append(calczahl(tempdez[1]/tempdez[4]))
if tempdez[3]=="*":
	lowtohigh.append(calczahl(tempdez[1]*tempdez[4]))


"""
if tempdez[3]=="-":
	tempdez[1]=tempdez[1]-tempdez[4]
	if tempdez[1]<0:
		
		tempdez[0]-tempdez[3]+tempdez[1]
	lowtohigh.append(calczahl(tempdez[0]-tempdez[3]))
else:
	lowtohigh=calczahl(tempdez[0])
"""

	
for counter in range(len(lowtohigh)-1,-1,-1):
	if counter==len(lowtohigh)-targetcount:
		print(",",end="")
	if stellwertout <= 36:
		print(""+ausgabe35[lowtohigh[counter]]+"",end="")
	else:
		print(str(lowtohigh[counter])+" ",end="")
print()
