#! /usr/bin/python3

import sys
import os
import math

countmax=10000000000000





scounter=0

def teilerfinder(zahl):
	global scounter
	limit=math.ceil(math.sqrt(zahl))
	teiler=2
	if (zahl&1):
		teiler=3	
	
	while teiler<=limit and (zahl%teiler)!=0 and scounter<countmax:
		teiler+=2
		scounter+=1
	
	if teiler<=limit and scounter<countmax:
		print(teiler,end="*")
		teilerfinder(zahl//teiler)
	
	if teiler>limit:
		print(zahl,end="*1\n")	
	
	if scounter>=countmax:
		print("\nError: calculation failed")


if len(sys.argv)!=2 or sys.argv[1].isdecimal()==False:
	print("Error: invalid parameters\nusage: "+sys.argv[0]+" <zahl>")
	exit(1) 

teilerfinder(int(sys.argv[1]))
