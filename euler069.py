# -*- coding: utf-8 -*-
#Totient maximum
#Problem 69
#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

#n	Relatively Prime	φ(n)	n/φ(n)
#2	1	1	2
#3	1,2	2	1.5
#4	1,3	2	2
#5	1,2,3,4	4	1.25
#6	1,5	2	3
#7	1,2,3,4,5,6	6	1.1666...
#8	1,3,5,7	4	2
#9	1,2,4,5,7,8	6	1.5
#10	1,3,7,9	4	2.5
#It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

#Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

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

def phy(n):
	cpt = 0;
	for i in range(1, n + 1):
		g , d = greatest_common_divisor(n, i);
		if g == 1 and d == 0:
			cpt += 1;
	#print "phy", n, cpt;
	return cpt;

#max = 0.0;
#index = 0;
#limit = 1000000;
#for value in range(2, limit+1):
#	res = float(value) / phy(value);
#	if max < res:
#		max = res;
#		index = value;
#print max, index;

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
list = sieve_eratosthenes(100);
result = 1;
index = 0;
while result * list[index] < limit:
	result *= list[index];
	index += 1;
print result;
