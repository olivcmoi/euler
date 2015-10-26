# -*- coding: utf-8 -*-
#Spiral primes
#Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

#Miller-Rabin primality test
def isPrime(n):
	k = 11;
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

length = 1;
nbEltDiag = 1;
nbEltPrime = 0;
total = 1;

while total > 0:
	length += 2;
	nbEltDiag += 4;
	total += length - 1;
	if isPrime(total):
		nbEltPrime += 1;
	total += length - 1;
	if isPrime(total):
		nbEltPrime += 1;
	total += length - 1;
	if isPrime(total):
		nbEltPrime += 1;
	total += length - 1;
	if isPrime(total):
		nbEltPrime += 1;
	print length, nbEltPrime, nbEltDiag, total, nbEltPrime / float(nbEltDiag);
	if nbEltPrime / float(nbEltDiag) < 0.1:
		break;

print "Fin",length;