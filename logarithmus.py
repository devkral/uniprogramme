temzahl#! /usr/bin/python3
import os
import sys


def usage():
	print("usage:")
	print(sys.argv[0]+" <logbasis> <zahl>")
	exit(1)

if len(sys.argv)!=3:
	usage()
	
#counter=1 #use s
logbasis=int(sys.argv[1])
zahl=int(sys.argv[2])
#begzahl=0
tempzahl=1

"""while tempzahl < zahl and zahl!=tempzahl:
	tempzahl+=logbasis
	counter+=1"""
tempzahl=zahl/logbasis

if counter < mod:
	print(str(tempzahl)+" ist logarithmus zu "+str(zahl))
