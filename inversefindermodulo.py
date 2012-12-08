#! /usr/bin/python3
import os
import sys


def usage():
	print("usage:")
	print(sys.argv[0]+" <modulosystem> <zahl>")
	exit(1)

if len(sys.argv)!=3:
	usage()
	
counter=0 #use s
mod=int(sys.argv[1])
zahl=int(sys.argv[2])
#begzahl=0
tempzahl=0

while counter < mod and tempzahl%mod!=1:
	tempzahl+=zahl
	counter+=1

if counter < mod:
	print(str(counter)+" ist inverses zu "+str(zahl))
