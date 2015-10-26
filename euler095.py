# -*- coding: utf-8 -*-
#Amicable chains
#Problem 95
#The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

#Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

#Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

#12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

#Since this chain returns to its starting point, it is called an amicable chain.

#Find the smallest member of the longest amicable chain with no element exceeding one million.

import math

def sieve_eratosthenes(limit):
	list = [];
	multiple = 0;
	list = range(0, limit);
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

def sumOfFactorsPrime(number, primelist):
	n = number;
	sum = 1;
	p = primelist[0];
	j = 0;
	i = 0;

	while p * p <= n and n > 1 and i < len(primelist):
		p = primelist[i];
		i += 1;
		if n % p == 0:
			j = p * p;
			n = n / p;
			while n % p == 0:
				j = j * p;
				n = n / p;
			sum = sum * (j - 1) / (p - 1);
	#A prime factor larger than the square root remains
	if n > 1:
		sum *= n + 1;
	return sum - number;

limit = 1000000;
somme = 0;
list = [];
result = 0;
listPrime = sieve_eratosthenes(int(math.sqrt(limit)));
maxLenAmicableChain = 0;

for value in range(0, limit+1):
	somme = sumOfFactorsPrime(value, listPrime);
	list.append(somme);
	listChain = [value];
	while somme > 1 and somme < value and somme not in listChain:
		listChain.append(somme);
		somme = list[somme];
	if somme in listChain:
		#print listChain, somme;
		listChain = listChain[listChain.index(somme):];
		if len(listChain) > maxLenAmicableChain:
			print listChain, somme;
			maxLenAmicableChain = len(listChain);
			listChain.sort();
			result = listChain[0];
#print list;
print result;