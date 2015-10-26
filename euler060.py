# -*- coding: utf-8 -*-
#Prime pair sets
#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

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

#Miller-Rabin primality test
def isPrime(n):
	k = 5;
	assert n >= 2;
	if n % 2 == 0:
		return 0;

	d = n - 1;
	s = 0;
	while d % 2 == 0:
		d /= 2;
		s += 1;

	# test the base a to see whether it is a witness for the compositeness of n
	def try_composite(a):
		if pow(a, d, n) == 1:
			return False;
		for i in range(s):
			if pow(a, 2**i * d, n) == n-1:
				return False;
		return True # n is definitely composite

	while k > 0:
		from random import randint
		a = randint(2,n-1);
		if try_composite(a):
			return 0;
		k -= 1;
	return 1;

def testIsPrime(prime1, prime2):
	if isPrime(int(str(prime1) + str(prime2))) and isPrime(int(str(prime2) + str(prime1))) == 1:
		return True;
	return False;

def find():
	for a in range(0, len(listPrime) - 4):
		for b in range(a + 1, len(listPrime) - 3):
			if testIsPrime(listPrime[a], listPrime[b]):
				for c in range(b + 1, len(listPrime) - 2):
					if testIsPrime(listPrime[a], listPrime[c]) and testIsPrime(listPrime[b], listPrime[c]):
						for d in range(c + 1, len(listPrime) - 1):
							if testIsPrime(listPrime[a], listPrime[d]) and testIsPrime(listPrime[b], listPrime[d]) and testIsPrime(listPrime[c], listPrime[d]):
								for e in range(d + 1, len(listPrime)):
									if testIsPrime(listPrime[a], listPrime[e]) and testIsPrime(listPrime[b], listPrime[e]) and testIsPrime(listPrime[c], listPrime[e]) and testIsPrime(listPrime[d], listPrime[e]):
										somme = listPrime[a] + listPrime[b] + listPrime[c] + listPrime[d] + listPrime[e];
										print listPrime[a], listPrime[b], listPrime[c], listPrime[d], listPrime[e], somme;
										return;

limit = 10000;
listPrime = sieve_eratosthenes(limit);
find();

