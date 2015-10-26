# -*- coding: utf-8 -*-
#Combinatoric selections
#There are exactly ten ways of selecting three from five, 12345:
#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#In combinatorics, we use the notation, 5C3 = 10.
#In general,
#nCr =	
#n!
#r!(n−r)!
#,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
#It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

def fact(n):
	result = 1;
	while n > 1:
		result *= n;
		n -= 1;
	return result;

def combi(n,r):
	return fact(n)/(fact(r) * fact(n-r));

cpt = 0;

for n in range (1, 100 + 1):
	for r in range (1, n):
		if combi(n,r) > 1000000:
			cpt += 1;

print "Fin", cpt;