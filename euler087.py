# -*- coding: utf-8 -*-
#Prime power triples
#Problem 87
#The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

#28 = 22 + 23 + 24
#33 = 32 + 23 + 24
#49 = 52 + 23 + 24
#47 = 22 + 33 + 24

#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
import math;

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

limit = 50000000;
print int(math.sqrt(limit));
primes = sieve_eratosthenes(1, int(math.sqrt(limit))+1);
list = set();

for a in primes:
	tempa = pow(a,4);
	if tempa > limit:
		break;
	for b in primes:
		tempb = pow(b,3);
		if tempa + tempb > limit:
			break;
		for c in primes:
			temp = tempa + tempb + pow(c,2);
			if temp > limit:
				break;
			list.add(temp);
print "Fin",len(list);