#! /usr/bin/python3
import os
import sys


hightolow=[]
lowtohigh=[]
tempdez=0;
argslen=len(sys.argv)-1 #program arg1 arg2 args

def myhelp():
	print("usage:")
	print(sys.argv[0]+" <stellwertinput> <stellwertoutput> <…Ziffern des Zahlensystems>")

def toohighdigit(digit):
	print ("Error: Digit: "+str(digit)+" to high. Exit")
	exit(2)

if argslen < 3:
	print("error: too less arguments")
	myhelp()
	exit(1)
else:
	stellwertin=int(sys.argv[1])
	stellwertout=int(sys.argv[2])

ubertrag=0
for counter in range(argslen, 2, -1):
	tempcl=argslen-counter
	if int(sys.argv[counter])>=int(stellwertin):
		toohighdigit(sys.argv[counter])
	#lowtohigh.append((int(sys.argv[counter])*(stellwertin**counter2))+ubertrag)
	#if lowtohigh[counter] >= stellwertin:
	#	tempre=lowtohigh[counter] % stellwertin
	#	ubertrag=lowtohigh[counter]-tempre
	#	lowtohigh[counter]=tempre
	tempdez+=int(sys.argv[counter])*(stellwertin**tempcl)
	#print(stellwertin**tempcl)

	if 3 < counter:
		print(sys.argv[counter]+"*"+str(stellwertin)+"^"+str(tempcl), end="+")
	else:
		print(sys.argv[counter]+"*"+str(stellwertin)+"^"+str(tempcl), end="\n")
	
zahlcalc=tempdez

counter2=-1
while zahlcalc!=0:
	counter2+=1
	#print(str(zahlcalc)+" mod "+str(stellwertout))
	#print("Füge zu z, an Position:"+str(counter2))
	lowtohigh.append(zahlcalc%stellwertout)
	zahlcalc=int((zahlcalc-lowtohigh[counter2])/stellwertout)
	
for counter3 in range(len(lowtohigh)-1,-1,-1):
	print(lowtohigh[counter3],end=" ")
print()
