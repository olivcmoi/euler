# -*- coding: utf-8 -*-
#Totient permutation
#Problem 70
#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

#Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

#Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

#Input: a, b positive integers
#Output: g and d such that g is odd and gcd(a, b) = g×2d
#    d := 0
#    while a and b are both even do
#        a := a/2
#        b := b/2
#        d := d + 1
#    while a ≠ b do
#        if a is even then a := a/2
#        else if b is even then b := b/2
#        else if a > b then a := (a – b)/2
#        else b := (b – a)/2
#    g := a
#    output g, d
def greatest_common_divisor(a, b):
	d = 0;
	while a % 2 == 0 and b % 2 == 0:
		a /= 2;
		b /= 2;
		d += 1;
	while a <> b:
		if a % 2 == 0:
			a /= 2;
		elif b % 2 == 0:
			b /= 2;
		elif a > b:
			a = (a - b) / 2;
		else:
			b = (b - a) / 2;
	g = a;
	return g, d;

def phy(n, cond):
	cpt = 0;
	for i in range(1, n + 1):
		g , d = greatest_common_divisor(n, i);
		if g == 1 and d == 0:
			cpt += 1;
			if cond <> 0 and cpt > cond:
				break;
	#print "phy", n, cpt;
	return cpt;

def isPermutation(a, b):
	if ''.join(sorted(str(a))) == ''.join(sorted(str(b))):
		return True;
	else:
		return False;

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

#max = 0.0;
#index = 0;
#limit = pow(10,4);
#cond = 0;
#for value in range(2, limit+1):
#	if max > 0:
#		cond = int(value / max) + 1;
#	temp = phy(value, cond);
#	res = value / float(temp);
#	if max < res and isPermutation(value, temp):
#		max = res;
#		index = value;
#print max, index;

best = 1;
phiBest = 1;
bestRatio = 100000.0;
 
limit = pow(10, 7);
lowerbound = 2;
upperbound = 5000;
primes = sieve_eratosthenes(lowerbound, upperbound);
 
for i in primes:
	for j in primes:
		temp = i * j;
		if temp > limit:
			break;
		phi = (i - 1) * (j - 1);
		ratio = temp / float(phi);
		if isPermutation(temp, phi) and bestRatio > ratio:
			best = temp;
			phiBest = phi;
			bestRatio = ratio;
			print i, j, best, phiBest, ratio;
print "Fin", best, phiBest, ratio;


