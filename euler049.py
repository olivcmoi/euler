# -*- coding: utf-8 -*-
#Prime permutations
#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#What 12-digit number do you form by concatenating the three terms in this sequence?

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

def isPermutation(a, b, c):
	list = [];
	temp = a;
	listPossible = [];
	isOk = 0;
	while temp > 0:
		list.append(temp % 10);
		temp /= 10;
	from itertools import permutations
	for subset in permutations(list, 4):
		listPossible.append(reduce(lambda rst, d: rst * 10 + d, subset));
	if b in listPossible and c in listPossible:
		isOk = 1;
	return isOk;

limit = 10000;
listPrime = sieve_eratosthenes(limit);

for i in range(1000,limit - 6660):
	if i in listPrime and i + 3330 in listPrime and i + 6660 in listPrime:
		if isPermutation(i, i+3330, i+6660):
			print "Yes", i, i+3330, i+6660;
print "Fin";