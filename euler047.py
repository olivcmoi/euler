# -*- coding: utf-8 -*-
#Distinct primes factors
#The first two consecutive numbers to have two distinct prime factors are:
#14 = 2 × 7
#15 = 3 × 5
#The first three consecutive numbers to have three distinct prime factors are:
#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.
#Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

import math;

def sieve_eratosthenes(limit):
	list = [];
	multiple = 0;
	list = range(0, limit+1);
	for i in list:
		if i >= 2:
			multiple = 2;
			while (i * multiple) < limit:
				list[i * multiple] = 0;
				multiple += 1;
	result = [];
	for i in list:
		if i > 1:
			result.append(i);
	return result;

def primeFactor(n, listPrim):
	listFactor = [];
	index = 0;
	while n > 1:
		while n % listPrim[index] == 0:
			if listPrim[index] not in listFactor:
				listFactor.append(listPrim[index]);
			n /= listPrim[index];
		index += 1;
	return listFactor;

limit = 4;
listPrime = sieve_eratosthenes(1000000);
value = 1;
factorN = [];
factorNm1 = [];
factorNm2 = [];
factorNm3 = [];
while len(factorNm3) <> len(factorNm2) or len(factorNm2) <> len(factorNm1) or len(factorN) <> len(factorNm1) or len(factorN) <> limit or factorN in factorNm1 or factorN in factorNm2 or factorNm1 in factorNm2 or factorN in factorNm3 or factorNm1 in factorNm3 or factorNm2 in factorNm3:
	value += 1;
	factorNm3 = factorNm2;
	factorNm2 = factorNm1;
	factorNm1 = factorN;
	factorN = primeFactor(value, listPrime);
print "Fin", value, factorN, value - 1, factorNm1, value - 2, factorNm2, value - 3, factorNm3;