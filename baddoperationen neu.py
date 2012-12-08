#! /usr/bin/python3
import os
import sys
import math



argslen=len(sys.argv)-1 #program arg1 arg2 args

def myhelp():
	print("usage:")
	print(sys.argv[0]+" <stellwertinput> <stellwertoutput> <…Ziffern des Zahlensystems>")



operators={
 "*" : "*", # part of sonder elements
 "/" : "/",
 "+" : "+",
 "-" : "-"
}

if argslen < 3:
	print("error: too less arguments")
	myhelp()
	exit(1)
else:
	stellwertin=int(sys.argv[1])
	stellwertout=int(sys.argv[2])

listsepar=[] #low to high

poscomma=0
for counter in range(argslen, 2, -1):
	if sys.argv[counter] == "," or sys.argv[counter] == ".":
		poscomma=counter

ubertrag=0
ubertrag2=0
counter=argslen+1 #get the first element
zahl=0;
init=1
while ubertrag != 0 or counter>2:
	counter=counter-1
	if counter >2:
		if sys.argv[counter] == "," or sys.argv[counter] == ".":
			listsepar.append(".")
			continue
		else:
			zahl=int(sys.argv[counter])  #must be last argument of if
	else:
		zahl=0
	"""zahlmod=(zahl+ubertrag)%stellwertin
	#print(zahlmod)
	ubertrag=int((zahl+ubertrag-zahlmod)/stellwertin)
	zahlmodout=((zahlmod+ubertrag2)*stellwertin)%stellwertout
	ubertrag2=int((((zahlmod+ubertrag2)*stellwertin)-zahlmodout)/stellwertout)
	listsepar.append(zahlmodout)"""
	zahlneu=int((zahl+ubertrag)*pow(stellwertin, (argslen-counter-poscomma)))
	print(zahlneu)
	zahlmod=zahlneu%stellwertout
	ubertrag=(zahlneu-zahlmod) #tellwertout
	listsepar.append(zahlmod)
	
		
for counter in range(len(listsepar)-1, -1, -1):
	print(str(listsepar[counter]),end=" ")
print()

