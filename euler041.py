# -*- coding: utf-8 -*-
#Pandigital prime
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#What is the largest n-digit pandigital prime that exists?

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

listPrime = sieve_eratosthenes(987654321);
print "end list Prime"
result = 0;
for i in listPrime:
	if isPandigital(i):
		print i;
		result = i;


print result;