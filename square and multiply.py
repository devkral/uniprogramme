#! /usr/bin/python3
import sys
import os


def squareandmultiply(a,potenz,mod):
	if potenz < 1: #wenn potenz = 0
		print("Ende erreicht. Potenz=0, return 1.")
		return 1
	#if potenz < 2:
	#	print("Ende erreicht.")
	#	return a%mod
	potalt=potenz
	potenz=potenz>>1
	print("Halbiere Potenz ("+str(potalt)+"), nehme "+str(a)+" ins Quadrat")
	if potalt&1==1:
		print("Ungerade, multipliziere mit "+str(a)+"¹")
		return (squareandmultiply((a*a)%mod,potenz,mod)*a)%mod
	else:
		print("Gerade, multipliziere mit "+str(a)+"⁰ (=1) fällt weg")
		return (squareandmultiply((a*a)%mod,potenz,mod))%mod
	
def usage():
	print("usage:")
	print("program <zahl> <potenz> <modulo>")

if len(sys.argv)!=4:
	usage()
	exit(1)

zahl=int(sys.argv[1])
hoch=int(sys.argv[2])
modulo=int(sys.argv[3])
t=squareandmultiply(zahl,hoch,modulo)
print("Das Ergebnis ist: "+str(t))


