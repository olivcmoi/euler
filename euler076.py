# -*- coding: utf-8 -*-
#Counting summations
#Problem 76
#It is possible to write five as a sum in exactly six different ways:

#2
#1 + 1
# ecriture 2 => 1

#3
#2 + 1
#1 + 1 + 1
# ecriture 3 => 1 + ecriture 2


#4
#3 + 1
#2 + 2
#2 + 1 + 1
#1 + 1 + 1 + 1
# ecriture 4 => 1 + ecriture 3 + ecriture 2

#5
#4 + 1
#3 + 2
#3 + 1 + 1
#2 + 2 + 1
#2 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1
# ecriture 5 => 1 + ecriture 3 + ecriture 3 + ecriture 2

#6
#5 + 1
#4 + 2
#4 + 1 + 1
#3 + 3
#3 + 2 + 1
#3 + 1 + 1 + 1
#2 + 2 + 2
#2 + 2 + 1 + 1
#2 + 1 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1 + 1
# ecriture 6 => 1 + ecriture 3 + 1 + ecriture 3 + 

#How many different ways can one hundred be written as a sum of at least two positive integers?

import math;

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
	for i in range(1, n):
		cpt += (1 + calcul(n-i, i));
	return cpt;

#print 100, ecriture(100);


target = 100;
ways =  [0] * (target + 1);
ways[0] = 1;
for i in range(1, target):
    for j in range(i, target+1):
        ways[j] += ways[j - i];
print ways[100];