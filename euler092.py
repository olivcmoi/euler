# -*- coding: utf-8 -*-
#Square digit chains
#Problem 92
#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

#For example,

#44 → 32 → 13 → 10 → 1 → 1
#85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

#How many starting numbers below ten million will arrive at 89?

import math;

def next(n):
	result = 0;
	while n > 0:
		result += pow(n % 10,2);
		n /= 10;
	return result;

list89 = set();
list1 = set();
list1.add(1);
list89.add(89);

cpt = 0;
for n in range(2, 10000000):
	bLoop = True;
	temp = n;
	while bLoop:
		if temp in list1:
			list1.add(n);
			bLoop = False;
		elif temp in list89:
			list89.add(n);
			bLoop = False;
			cpt += 1;
		temp = next(temp);

print "Fin",cpt;