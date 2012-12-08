#! /usr/bin/python3
import sys
import os

def testgerade(u):
	if 1&u:
		return 0 #false
	else:
		return 1 #true


def squareandmultiply(a,potenz,mod):
	if potenz < 1:
		return a
	status=testgerade(potenz)
	potenz=potenz>>1
	
	if status==0:
		return (squareandmultiply((a*a)%mod,potenz,mod)*a)%mod
	else:
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
print("Das Resultat ist: "+str(squareandmultiply(zahl,hoch,modulo)))


