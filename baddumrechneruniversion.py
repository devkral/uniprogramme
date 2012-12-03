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

#ubertrag=0
ausgabehex={0 : "0",
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
                15 : "F"
}


u=""
for counter in range(3,len(sys.argv)):
	if int(sys.argv[counter]) in ausgabehex:
		u+=ausgabehex[int(sys.argv[counter])]
	else:
		u+=" "+sys.argv[counter]+" "
if stellwertin != 10:
	print("Wandle ("+u+")"+str(stellwertin)+" in eine temporäre Dezimalzahl x um")
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
	if stellwertin != 10:
		if 3 < counter:
			print(sys.argv[counter]+"*"+str(stellwertin)+"^"+str(tempcl), end="+")
		else:
			print(sys.argv[counter]+"*"+str(stellwertin)+"^"+str(tempcl), end="\n")
	
zahlcalc=tempdez

counter2=-1
while zahlcalc!=0:
	counter2+=1
	print(str(zahlcalc)+" mod "+str(stellwertout))
	print("Füge "+str(zahlcalc%stellwertout)+" zu z, an Position:"+str(counter2))
	lowtohigh.append(zahlcalc%stellwertout)
	zahlcalc=int((zahlcalc-lowtohigh[counter2])/stellwertout)
	if zahlcalc > 0:
		print("Rechne weiter mit: "+str(zahlcalc))
	else:
		print("x="+str(zahlcalc)+" Höre auf")
	
	
for counter4 in range(0,len(lowtohigh)):
	print("z"+str(counter4)+":"+str(lowtohigh[counter4]),end=" ")
print("Oder:\n(",end="")

for counter3 in range(len(lowtohigh)-1,-1,-1):
	print(str(lowtohigh[counter3]),end="")
print(")"+str(stellwertout))
