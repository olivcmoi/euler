# -*- coding: utf-8 -*-
#Large non-Mersenne prime
#Problem 97
#The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

#However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

#Find the last ten digits of this prime number.

# Est-ce que c'est résolu ?
def isSolved(data):
	for i in range(0, len(data)):
		if 0 in data[i]:
			return False;
	return True;

def isErreur(data):
	error = False;
	for cube in range(0, 9):
		l = listCube(data, cube);
		nb0 = l.count(0);
		for index in range(0, nb0):
			l.remove(0);
		setL = set(l);
		if len(setL) != len(l):
			#print 'Error: Cube', cube;
			error = True;
	for i in range(0, len(data)):
		column = [];
		line = [];
		for j in range(0, len(data)):
			if data[i][j] > 0:
				column.append(data[i][j]);
		setL = set(column);
		if len(setL) != len(column):
			#print 'Error: Column', i;
			error = True;
		for j in range(0, len(data)):
			if data[j][i] > 0:
				line.append(data[j][i]);
		setL = set(line);
		if len(setL) != len(line):
			#print 'Error: Line', i;
			error = True;
	return error;

# Liste des numéros existant pour un cube
# Cube listé de la façon suivante
#  0  3  6
#  1  4  7
#  2  5  8
def listCube(data, cube):
	list = [];
	a = cube%3;
	b = cube/3;
	for i in range(a * 3, a * 3 + 3):
		for j in range(b * 3, b * 3 + 3):
			list.append(data[i][j]);
	return list;

# Liste des numéros existant dans la ligne et la colonne
def listVertHori(data, i, j):
	list = [];
	for k in range(0, 9):
		list.append(data[i][k]);
		list.append(data[k][j]);
	return list;

# Liste les positions possibles d'un numéro donné dans un cube
def possibleNumCube(data, num, cube):
	list = [];
	a = cube%3;
	b = cube/3;
	for i in range(a * 3, a * 3 + 3):
		for j in range(b * 3, b * 3 + 3):
			if data[i][j] == 0 and num not in listVertHori(data,i,j):
				list.append((i, j));
	return list;

# Ajout 
def ajout(data, pile, i, j, val):
	data[i][j] = val;
	if len(pile) > 0:
		pile.append((i, j, val));

# Pour chaque numéro, 
#	on vérifie s'il appartient à un cube,
#		sinon on liste les positions possibles dans ce cube
#			si cette liste ne contient qu'un élément -> c'est la solution
def complicateSolve(data, pile):
	bIsModified = False;
	for num in range(1, 10):
		for cube in range(0, 9):
			if num not in listCube(data, cube):
				possible = possibleNumCube(data, num, cube);
				if len(possible) == 1:
					#print 'Num', num, 'Cube', cube, possible;
					ajout(data, pile, possible[0][0], possible[0][1], num);
					bIsModified = True;
	return bIsModified;

# Pour chaque case non résolue,
#	on passe en revue les différents numéros,
#		pour ceux qui ne sont pas dans le cube, ni dans la ligne ou la colonne,
#			on vérifie qu'il existe d'autre possibilité sur la ligne et la colonne
#				sinon -> c'est la solution
def moreComplicateSolve(data, pile):
	bIsModified = False;
	for i in range(0, len(data)):
		for j in range(0, len(data)):
			if data[i][j] == 0:
				for num in range(1, 10):
					if num not in listCube(data, j/3*3+i/3) and num not in listVertHori(data, i, j):
						#print i, j, num;
						hauteur = 0;
						horizontal = 0;
						for k in range(0, 9):
							if k != j and data[i][k] == 0 and num not in listCube(data, k/3*3+i/3):
								hauteur += 1;
								for l in range(0, 9):
									if data[l][k] == num:
										hauteur -= 1;
										#print 'Hauteur', i, j, num, 'Couple', i, k, 'Trouvé', l, k;
							if k != i and data[k][j] == 0 and num not in listCube(data, j/3*3+k/3):
								horizontal += 1;
								for l in range(0, 9):
									if data[k][l] == num:
										horizontal -= 1;
										#print 'Horizontal', i, j, 'Couple', k, j, 'Trouvé', k, l;
						if hauteur == 0 or horizontal == 0:
							ajout(data, pile, i, j, num);
							bIsModified = True;
							#print 'Modified', i, j, num;
	return bIsModified;

def listRejet(rejet, i, j):
	list = [];
	for elt in rejet:
		if elt[0] == i and elt[1] == j:
			list.append(elt[2]);
	return list;

def solve(data):
	pile = [];
	hypothese = [];
	rejet = [];
	nCannotSolve = 0;
	while not isSolved(data):
		bIsModified = False;
		maxLen = maxI = maxJ = 0;
		for i in range(0, len(data)):
			for j in range(0, len(data)):
				if data[i][j] == 0:
					setVal = set(listVertHori(data, i, j)) | set(listCube(data, j/3*3+i/3));
					if len(setVal) == 9:
						maxLen = len(setVal);
						for val in range(1, 10):
							if val not in setVal:
								ajout(data, pile, i, j, val);
						bIsModified = True;
					elif maxLen < len(setVal):
						maxLen = len(setVal);
						maxI = i;
						maxJ = j;
						maxSetVal = setVal;
						#print maxLen, maxI, maxJ, maxSetVal;
		if not bIsModified and not complicateSolve(data, pile) and not moreComplicateSolve(data, pile):
			nCannotSolve += 1;
			#print 'CANNOT SOLVE';
			#for i in range(0, len(data)):
			#	print i, data[i];
			if isErreur(data) or maxLen > 9:
				#print 'ERROR';
				#print 'Liste pile:' 
				#for elt in pile:
				#	print elt[0], elt[1], elt[2];
				#print 'Liste hypothese:' 
				#for elt in hypothese:
				#	print elt[0], elt[1], elt[2];
				#print 'Liste rejet:' 
				#for elt in rejet:
				#	print elt[0], elt[1], elt[2];
				# Récupère dernière hypothèse
				bIsLastHypoHasOtherSol = False;
				while not bIsLastHypoHasOtherSol:
					lastHypo = hypothese.pop();
					rejet.append(lastHypo);
					# Vide pile des elts avant hypothèse
					bIsLastHypo = False;
					while not bIsLastHypo:
						lastEltPile = pile.pop();
						# Remet à zéro 
						data[lastEltPile[0]][lastEltPile[1]] = 0;
						if lastEltPile == lastHypo:
							bIsLastHypo = True;
					maxI = lastEltPile[0];
					maxJ = lastEltPile[1];
					maxSetVal = set(listVertHori(data, maxI, maxJ)) | set(listCube(data, maxJ/3*3+maxI/3)) | set(listRejet(rejet,maxI,maxJ));
					if len(maxSetVal) <= 9:
						bIsLastHypoHasOtherSol = True;
					else:
						# Enlever les éléments (maxI, maxJ) dans rejet
						for i in range(len(rejet) - 1, -1, -1):
							elt = rejet[i];
							if elt[0] == maxI and elt[1] == maxJ:
								rejet.remove(elt);
			#print maxLen, maxI, maxJ, maxSetVal;
			listHyp = [];
			for num in range(1, 10):
				if num not in maxSetVal:
					listHyp.append(num);
			hypothese.append((maxI, maxJ, listHyp[0]));
			data[maxI][maxJ] = listHyp[0];
			pile.append((maxI, maxJ, listHyp[0]));
			#print 'hypothese', maxI, maxJ, listHyp[0];

#data = """0 0 3  0 2 0  6 0 0
#9 0 0  3 0 5  0 0 1
#0 0 1  8 0 6  4 0 0
#0 0 8  1 0 2  9 0 0
#7 0 0  0 0 0  0 0 8
#0 0 6  7 0 8  2 0 0
#0 0 2  6 0 9  5 0 0
#8 0 0  2 0 3  0 0 9
#0 0 5  0 1 0  3 0 0"""
data = """1 0 0 9 2 0 0 0 0
5 2 4 0 1 0 0 0 0
0 0 0 0 0 0 0 7 0
0 5 0 0 0 8 1 0 2
0 0 0 0 0 0 0 0 0 
4 0 2 7 0 0 0 9 0
0 6 0 0 0 0 0 0 0
0 0 0 0 3 0 9 4 5
0 0 0 0 7 1 0 0 6"""

#ldata = [map(int, row.split()) for row in data.splitlines()];
#print ldata;
#solve(ldata);
#for i in range(0, len(ldata)):
#	print ldata[i];

with open('p096_sudoku.txt') as f:
	data = f.read();

sum = 0;
index = 0;
ldata = [];
for row in data.splitlines():
	if index == 0:
		print row;
	else:
		l = [];
		for c in row:
			l.append(int(c));
		ldata.append(l);
	index += 1;
	index %= 10;
	if index == 0:
		solve(ldata);
		sum += ldata[0][0] * 100 + ldata[0][1] * 10 + ldata[0][2];
		for i in range(0, len(ldata)):
			print ldata[i];
		ldata = [];
print sum;
