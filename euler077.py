# -*- coding: utf-8 -*-
#Prime summations
#Problem 77
#It is possible to write ten as the sum of primes in exactly five different ways:

#7 + 3
#5 + 5
#5 + 3 + 2
#3 + 3 + 2 + 2
#2 + 2 + 2 + 2 + 2

#What is the first value which can be written as the sum of primes in over five thousand different ways?

#import math;

def calcul(l, max, primes):
	if l < 0:
		return 0;
	if l == 0:
		return 1;
	cpt = 0;
	for i in primes:
		if max >= i:
			cpt += calcul(l-i, i, primes);
		else:
			break;
	return cpt;

def ecriture(n, primes):
	cpt = 0;
	for i in primes:
		if n > i:
			cpt += calcul(n-i, i, primes);
		else:
			break;
	return cpt;

def sieve_eratosthenes(limitb, limith):
	list = [];
	multiple = 0;
	list = range(0, limith+1);
	for i in list:
		if i >= 2:
			multiple = 2;
			while (i * multiple) < limith:
				list[i * multiple] = 0;
				multiple += 1;
	result = [];
	for i in list:
		if i > limitb:
			result.append(i);
	return result;

primes = sieve_eratosthenes(1, 71);

target = 5000;
max = 0;
index = 10;
while max < target:
	temp = ecriture(index, primes);
	if temp > max:
		max = temp;
		print index, max;
	index += 1;