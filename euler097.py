# -*- coding: utf-8 -*-
#Large non-Mersenne prime
#Problem 97
#The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form pow(2,6972593)−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

#However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×pow(2,7830457)+1.

#Find the last ten digits of this prime number.

sum = 2;
for i in range(1, 7830457):
	sum *= 2;
	if sum > 1000000000:
		sum = int(str(sum)[-10:]);
sum *= 28433;
sum += 1;
print sum;