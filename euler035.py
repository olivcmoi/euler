#Circular primes
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?
import itertools;

def sieve_eratosthenes(limit):
	list = [];
	multiple = 0;
	list = range(0, limit);
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

def listFromPrime(value):
	output = [];
	while value not in output:
		output.append(value);
		if ((value % 10) % 2 == 0) or ((value % 10) % 5 == 0):
			return [];
		temp = (value % 10) * pow(10,len(str(value))-1) + value / 10;
		value = temp;
	return output;

limitPrime = 1000000;
listPrime = sieve_eratosthenes(limitPrime);
listElement = [];

primeIsOk = 0;
listResult = [2,5];
for prime in listPrime:
	if prime not in listResult:
		listElement = listFromPrime(prime);
		primeIsOk = 1;
		for i in listElement:
			if i not in listPrime:
				primeIsOk = 0;
		if primeIsOk > 0:
			for i in listElement:
				if i not in listResult:
					listResult.append(i);
print listResult, len(listResult);
