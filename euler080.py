# -*- coding: utf-8 -*-
#Square root digital expansion
#Problem 80
#It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

#The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

import math;
import decimal;
decimal.getcontext().prec = 120;

def calc(n):
	temp = math.sqrt(n);
	strValue = str(temp - int(temp));
	sum = 0;
	print strValue;
	for c in strValue[2:]:
		sum += int(c);
	return sum;

def calc2(n):
	a0 = int(math.sqrt(n));
	if a0 - math.sqrt(n) == 0:
		return 0;
	result = (decimal.Decimal(a0) + decimal.Decimal(n) / decimal.Decimal(a0)) / decimal.Decimal(2);
	for i in range(0, 10):
		#print result;
		result = (result + n / decimal.Decimal(result))/2;
	strValue = str(result);
	sum = 0;
	#print strValue[0:101];
	for c in strValue[0:101]:
		if c is not '.':
			sum += int(c);
	return sum;

somme = 0;
for i in range(1, 101):
	somme += calc2(i);
print somme;
