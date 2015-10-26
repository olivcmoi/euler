# -*- coding: utf-8 -*-
#Sub-string divisibility
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.

def isPandigital(n):
	digits = 0;
	count = 0;
	tmp = 0;
	zero = 0;
	while n > 0:
		tmp = digits;
		if n % 10 == 0:
			zero += 1;
		digits = digits | 1 << int((n % 10) - 1);
		if tmp == digits:
			return 0;
		count += 1;
		n /= 10;
	return digits == (1 << count) - 1 and zero == 1;

def isDivisibility(n):
	strValue = str(n);
	offset = 0;
	if (len(strValue) < 10):
		offset = -1;
	if int(strValue[1+offset:4+offset]) % 2 == 0 and int(strValue[2+offset:5+offset]) % 3 == 0 and int(strValue[3+offset:6+offset]) % 5 == 0 and int(strValue[4+offset:7+offset]) % 7 == 0 and int(strValue[5+offset:8+offset]) % 11 == 0 and int(strValue[6+offset:9+offset]) % 13 == 0 and int(strValue[7+offset:10+offset]) % 17 == 0:
		return 1;
	return 0;

result = 0;
from itertools import permutations
possible = range(0, 10);
for subset in permutations(possible, 10):
	temp = reduce(lambda rst, d: rst * 10 + d, subset);
	if (isDivisibility(temp)):
		print temp;
		result += temp;
print 'Result',result;