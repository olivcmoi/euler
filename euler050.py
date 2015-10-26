# -*- coding: utf-8 -*-
#Consecutive prime sum
#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

limit = 1000000;
listPrime = sieve_eratosthenes(limit);
listSum = [];
sum = 0;
for i in range(0, len(listPrime)):
	sum += listPrime[i];
	listSum.append(sum);

max = 0;
result = 0;
for startIndex in range(0, len(listPrime)):
	sum = 0;
	consecutive = max + 1;
	while consecutive + startIndex < len(listPrime) and sum < limit:
		sum = listSum[consecutive + startIndex] - listSum[startIndex];
		if sum < limit and sum in listPrime and max < consecutive:
			max = consecutive;
			result = sum;
			#print len(listPrime), startIndex, max, result;
		consecutive += 1;
print "Fin", max, result;