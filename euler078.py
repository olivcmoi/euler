# -*- coding: utf-8 -*-
#Coin partitions
#Problem 78
#Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

#OOOOO
#OOOO   O
#OOO   OO
#OOO   O   O
#OO   OO   O
#OO   O   O   O
#O   O   O   O   O
#Find the least value of n for which p(n) is divisible by one million.

#import math;

def calcul(l, max):
	if max <= 1 or l <= 1:
		return 0;
	cpt = 0;
	for i in range(2, max+1):
		if l-i >= 0:
			cpt += (1 + calcul(l-i, i));
	return cpt;

def ecriture(n):
	cpt = 0;
	for i in range(1, n+1):
		cpt += (1 + calcul(n-i, i));
	return cpt;

print ecriture(5);

def fct(target):
	ways =  [0] * (target + 1);
	ways[0] = 1;
	for i in range(1, target):
		for j in range(i, target+1):
			ways[j] += ways[j - i];
	return ways[target]+1;

factor = 1000000;
factor2 = 100;
index = 0; #4800;
bFound = False;
while not bFound:
	temp = fct(index);
	if temp % factor == 0:
		bFound = True;
		print 'Ok', index, temp;
	if index % factor2 == 0:
		print index, temp;
	index += 1;

12400