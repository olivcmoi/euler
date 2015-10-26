# -*- coding: utf-8 -*-
#Goldbach's other conjecture
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#9 = 7 + 2×12
#15 = 7 + 2×22
#21 = 3 + 2×32
#25 = 7 + 2×32
#27 = 19 + 2×22
#33 = 31 + 2×12
#It turns out that the conjecture was false.
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

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

listPrime = sieve_eratosthenes(10000);
isGoldbach = 1;
value = 9;
while isGoldbach > 0:
	isGoldbach = 0;
	index = 0;
	while isGoldbach == 0 and listPrime[index] < value:
		j = 0;
		while value > listPrime[index] + 2 * pow(j,2):
			j += 1;
		if value == listPrime[index] + 2 * pow(j,2):
			print value, listPrime[index], j;
			isGoldbach = 1;
		index += 1;
	if isGoldbach > 0:
		value += 2;
		while value in listPrime:
			value += 2;
print "Fin", value