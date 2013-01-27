#! /usr/bin/python3
import os
import sys

print("Not ready yet")
exit(1)

hightolow=[]
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

positioncounter=argslen
anzahlkomma=0
for counter in range(3,argslen):
	if sys.argv[counter] == ".":
		positioncounter=counter-1
		anzahlkomma+=1

if anzahlkomma>1:
	print("Too many points")

ubertrag=0
for counter in range(3, positioncounter,1):
	tempcl=positioncounter-counter
	if int(sys.argv[counter])>=int(stellwertin):
		toohighdigit(sys.argv[counter])
	temp=(int(sys.argv[counter])+ubertrag)*(stellwertin**tempcl)
	temp2=temp%stellwertout
	ubertrag=(temp-temp2)//stellwertout
	hightolow.append(temp2)

if  anzahlkomma==1:
	hightolow.append(".")
	
for counter in range(positioncounter+2,argslen):
	tempcl=0

print(len(hightolow))
for counter3 in range(0,len(hightolow)-1):
	print("j")
	print(hightolow[counter3],end=" ")
print()
