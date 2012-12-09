#! /usr/bin/python3
import sys
import os


def squareandmultiply(a,potenz,mod):
	if potenz == 0: #case potenz = 0
		return 1
	if potenz < 2:
		return a%mod
	status=1&potenz
	potenz=potenz>>1
	
	if status==1:
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


