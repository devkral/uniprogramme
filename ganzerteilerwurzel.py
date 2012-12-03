#! /usr/bin/python3
import os
import sys
import math

argslen=len(sys.argv)-1
if len(sys.argv)<3 or len(sys.argv)>4 or not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
	print("usage:")
	print(sys.argv[0]+"<modulosystem> <rest> <wurzel>")
	exit(1)
else:
	modulo=int(sys.argv[1])
	rest=int(sys.argv[2])%modulo
	if len(sys.argv)==4 and sys.argv[3].isnumeric():
		wurzel=int(sys.argv[3])
	else:
		wurzel=2

 #seccounter=-1
maxcount=10000
zahl=0
counter=0
counter2=1
stopper=0

for counter in range(0,maxcount):
	zahl=(modulo*counter+rest)
	#print("Zahl: "+str(zahl)+" Zahl/2: "+str(math.ceil(zahl/2)))
	for counter2 in range(0, math.ceil(zahl/2)+1):
		#print("pot Wurzel: "+str(counter2)+" Ergebnis nach treatment:"+str(pow(counter2,wurzel)))
		if pow(counter2,wurzel) < zahl:
			continue
		if pow(counter2,wurzel) == zahl:
			#print("hurra")
			stopper=1
			break
		if pow(counter2,wurzel) > zahl:
			break
	if stopper==1:
		break
	
print("modulo:"+str(modulo)+" rest:"+str(rest)+ " zahl:"+str(zahl))
print("z="+str(wurzel)+"√(<modulo>*n+<rest>)(="+str(zahl)+") wobei n eine beliebige aber feste Zahl ist")	
if stopper == 1:
	if wurzel%2==0:
		print(str(wurzel)+". Wurzel von "+str(zahl)+" = ±"+str(counter2)+"   nach: "+str(counter)+" Iterationen")
	else:
		print(str(wurzel)+". Wurzel von "+str(zahl)+" = "+str(counter2)+"   nach: "+str(counter)+" Iterationen")
else:
	print("Kein Ergebnis")
