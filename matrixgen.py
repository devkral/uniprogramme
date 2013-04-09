#! /usr/bin/python3

import os
import sys

if len(sys.argv)<2:
	print("Error: not format:\nprog <type>")
	print("Type can be:")
	print("e: einheitsmatrix")
	print("z: nullmatrix")
	print("m: matrix")
	print("g: 2 matrix and gauss")
	exit(1)

#zahlelem=[0,1]

einszahlelem=[1,1]
nullzahlelem=[0,1]
	
def einheitsmatrixgen(grosse):

	matrix=[]
	tmpzeile=[]
	
	for y in range(0,grosse):
		tmpzeile=[]
		for x in range(0,grosse):
			if x==y:
				tmpzeile.append(einszahlelem)
			else:
				tmpzeile.append(nullzahlelem)
		matrix.append(tmpzeile)
	return matrix

def zeromatrixgen(grosse):

	matrix=[]
	tmpzeile=[]
	
	for y in range(0,grosse):
		tmpzeile=[]
		for x in range(0,grosse):
			tmpzeile.append(nullzahlelem)
		matrix.append(tmpzeile)
	return matrix

def getgrosse():
	if len(sys.argv)>2:
		blub=int(sys.argv[2])
	else:
		blub=int(input("wie groß:\n"))
	return blub

def easebruch(bruch):
	
	try:
		tmpbruch=[int(bruch[0]),int(bruch[1])]
	except TypeError:
		print(str(bruch)+" Not valid")
		return bruch
	
	if tmpbruch[0]%tmpbruch[1]==0:
		tmpbruch[0]=tmpbruch[0]//tmpbruch[1]
		tmpbruch[1]=1
	if tmpbruch[1]<0:
		tmpbruch[0]=tmpbruch[0]*-1
		tmpbruch[1]=tmpbruch[1]*-1
		
	if tmpbruch[0]==0: #important for next line
		tmpbruch[1]=1
	while tmpbruch[0]%2==0 and tmpbruch[1]%2==0:
		tmpbruch[0]=tmpbruch[0]//2
		tmpbruch[1]=tmpbruch[1]//2
	return tmpbruch
	
def easematrix(matrix):
	for y in matrix:
		for x in y:
			x=easebruch(x)
	return matrix


def matrixausgabe(matrix):
	matrix=easematrix(matrix)
	for y in matrix:
		for elem in range(0,2):
			for x in y:
				if x[elem]!=1 or elem!=1:
					print (str(x[elem]),end="")
				elif elem==1:
					print (" ",end="")
				len0=len(str(x[0]))
				len1=len(str(x[1])) 
				if len0>len1 and elem==1:
					for leelem in range(len1,len0):
						print (" ",end="")
				else:
					for leelem in range(len0,len1):
						print (" ",end="")
				print(" ",end="")
			
			print()
			
		print()

def matrixfertig(matrix):
	matrix=easematrix(matrix)

	print("matrix{",end="")
	for y in range(0,len(matrix)):
		for x in range(0,len(matrix[0])):
			if matrix[y][x][1]==1:
				print ("{"+str(matrix[y][x][0])+"}",end="")
			else:
				print ("{"+str(matrix[y][x][0])+"} over {"+str(matrix[y][x][1])+"}",end="")
			if x<len(matrix[0])-1:
				print(" # ",end="")
		if y<len(matrix)-1:
			print(" ## ",end="")
	
	print("}")



	

def add(elem1, elem2):
	
	if int(elem1[1])==int(elem2[1]):
		elemtemp=[int(elem1[0])+int(elem2[0]),int(elem1[1])]
	else:
		elemtemp=[int(elem1[0])*int(elem2[1])+int(elem2[0])*int(elem1[1]),int(elem1[1])*int(elem2[1])]
	
	return easebruch(elemtemp)

def mult(elem, multi):
	if multi[0]==0:
		return nullzahlelem
	elemtemp=[int(elem[0])*int(multi[0]),int(elem[1])*int(multi[1])]
	return easebruch(elemtemp)

def div(elem, div):
	
	if int(div[0])==0:
		return nullzahlelem
	tmp=[int(elem[0])*int(div[1]),int(elem[1])*int(div[0])]
	return easebruch(tmp)

def negate(elem):
	if int(elem[0])==0:
		tmp=nullzahlelem	
	else:
		tmp=[int(elem[0])*-1,int(elem[1])]
	return tmp

def multzeile(zeile, multi):
	tempzeile=[]
	for ttt in zeile:
		tempzeile.append(mult(ttt,multi))
	return tempzeile

def inzeilenaddition(zeile1,zeiles, multi):
	zeiletemp=[]
	if len(zeile1)!=len(zeiles):
		print("Error: Zeilenlänge verschieden")
		exit(1)
	for element in range(0,len(zeile1)):
		zeiletemp.append(easebruch(add(zeile1[element],mult(zeiles[element],multi))))
	return zeiletemp



def zeilentausch(matrix,zeile1,zeile2):
	zeiletemp=matrix[zeile1]
	matrix[zeile1]=matrix[zeile2]
	matrix[zeile2]=zeiletemp
	return matrix

def convdigit(matrix):
	for y in matrix:
		for x in y:
			x[0]=int(x[0])
			x[1]=int(x[1])
	return matrix

def gauss(matrix1,matrix2):
	pivo=0
	if len(matrix2)==0:
		matrix2=zeromatrixgen(len(matrix1))
	matrix1=convdigit(matrix1)
	matrix2=convdigit(matrix2)
	
	if len(matrix1)!=len(matrix2):
		print("Error: different length of matrix")
		exit(1)
	
	for spalte in range(0,len(matrix1[0])):
		print("Pivo counter: "+str(pivo))
		if pivo>=len(matrix1):
			print("Finished")
			break
		
		if matrix1[pivo][spalte][0]!=0:
			iszero=False
		else:
			iszero=True
			for zeile in range(pivo,len(matrix1)):
				if matrix1[zeile][spalte][0]!=0 and pivo!=zeile:
					print("Tausche Zeile: "+str(zeile)+" mit Zeile: "+str(pivo))
					matrix1=zeilentausch(matrix1,zeile,pivo)
					matrix2=zeilentausch(matrix2,zeile,pivo)
					iszero=False
					break
			
		if iszero==False:
			
			#simplify
			for zeile in range(pivo,len(matrix1)):
				if matrix1[zeile][spalte][0]==1 and matrix1[zeile][spalte][1]==1:
					print("Tausche Zeile: "+str(zeile)+" mit Zeile: "+str(pivo)+" da 1")
					matrix1=zeilentausch(matrix1,zeile,pivo)
					matrix2=zeilentausch(matrix2,zeile,pivo)
					break
			print("Pivotiere mit: "+str(matrix1[pivo][spalte][0])+"/"+str(matrix1[pivo][spalte][1]))
			
			for zeile in range(0,len(matrix1)):
				if zeile!=pivo:
					tozero=negate(div(matrix1[zeile][spalte],matrix1[pivo][spalte]))
					print("Addiere "+str(tozero[0])+"/"+str(tozero[1])+" des pivot elements zur Zeile: "+str(zeile))
					matrix1[zeile]=inzeilenaddition(matrix1[zeile],matrix1[pivo],tozero)
					if matrix1[zeile][spalte][0]!=0:
						print("Error: not zero, tozero is: "+str(tozero)+"zeile (number "+str(zeile)+") pivo: "+str(pivo))
					matrix2[zeile]=inzeilenaddition(matrix2[zeile],matrix2[pivo],tozero)

			if matrix1[pivo][spalte][0]!=1 or matrix1[pivo][spalte][1]!=1:
				toone=div(einszahlelem,matrix1[pivo][spalte])
				print("Multiply line to fit; Multiplier: "+str(toone))
				matrix1[pivo]=multzeile(matrix1[pivo],toone)
				matrix2[pivo]=multzeile(matrix2[pivo],toone)
			pivo+=1
			
		else:
			print("Do nothing because zero")
			
	return [matrix1,matrix2]


def matrixgen():
	matrix=[]
	lzeile=-1
	count=1
	errort=False
	tempzeile=[]
	eingabe='init'
	while eingabe!='' or lzeile==-1:
		if errort==False:
			print("Current matrix")
		else:
			print("Invalid input. Repeat input")
			errort=False
		
		matrixausgabe(matrix)
		tempzeile=[]
		eingabe=input("Enter row "+str(count)+":\n")
		if eingabe!='':
			for ttt in eingabe.split(" "):
				if ttt.count("/")==0:
					tempzeile.append([ttt,1])
				elif ttt.count("/")==1:
					temp2=ttt.split("/")
					if temp2[0]=='' or temp2[1]=='':
						errort=True
						break
					tempzeile.append([temp2[0],temp2[1]])
			if lzeile==-1:
				lzeile=len(tempzeile)
		elif lzeile==-1:
			print("Error: input too short")
			errort=True
				
		if eingabe=="e":
			return einheitsmatrixgen(getgrosse());
		if eingabe=="z":
			return zeromatrixgen(getgrosse())
		
		if len(tempzeile)==lzeile and errort==False:
			matrix.append(tempzeile)
			count+=1
		else:
			errort=True
			
	return matrix
	

	

if sys.argv[1]=="e":
	tempmatrix=einheitsmatrixgen(getgrosse())
	matrixausgabe(tempmatrix)
	print("Matrix ready for libreoffice:")
	matrixfertig(tempmatrix)
elif sys.argv[1]=="z":
	tempmatrix=zeromatrixgen(getgrosse())
	matrixausgabe(tempmatrix)
	print("Matrix ready for libreoffice:")
	matrixfertig(tempmatrix)
elif sys.argv[1]=="m":
	tempmat=matrixgen()
	print("Matrix ready for libreoffice:")
	matrixfertig(tempmat)
elif sys.argv[1]=="g":
	print("Enter Matrix 1:")
	mat1=matrixgen()
	print("Enter Matrix 2:")
	mat2=matrixgen()
	print("Now Gausselimination:")
	tempmat=gauss(mat1,mat2)
	print("Matrix1:")
	matrixausgabe(tempmat[0])
	print("Matrix2:")
	matrixausgabe(tempmat[1])
	print("libreoffice ready:")
	matrixfertig(tempmat[0])
	print("mline")
	matrixfertig(tempmat[1])
