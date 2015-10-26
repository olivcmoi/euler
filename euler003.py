#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

def factor(n):
	if n % 2 == 0:
		n = n/2;
		lastFactor = 2;
		while n % 2 == 0:
			n = n / 2;
	else:
		lastFactor=1;
	factor = 3;
	while n>1:
		if n % factor == 0:
			lastFactor = factor;
			n = n / factor;
			while n % factor == 0:
				n = n / factor;
		factor = factor+2;
	return lastFactor;
input = 600851475143;
print factor(input);
