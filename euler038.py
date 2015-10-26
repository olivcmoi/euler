# -*- coding: utf-8 -*-
#Pandigital multiples
#Take the number 192 and multiply it by each of 1, 2, and 3:
#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 #and (1,2,3,4,5).
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def isPandigital(n):
	digits = 0;
	count = 0;
	tmp = 0;
	while n > 0:
		tmp = digits;
		if n % 10 == 0:
			return 0;
		digits = digits | 1 << int((n % 10) - 1);
		if tmp == digits:
			return 0;
		count += 1;
		n /= 10;
	return digits == (1 << count) - 1;


for i in range(1,10000):
	multiplier = 1;
	result = 0;
	while result / pow(10,8) == 0:
		result = int(str(result) + str(i * multiplier));
		multiplier += 1;
	if result / pow(10,9) == 0 and isPandigital(result):
		print i, result;
