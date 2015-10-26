#Truncatable primes
#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

def truncatable_prime(value, listPrime):
	strValue = str(value);
	for e in ['2','5','0','6','8']:
		if e in strValue[1:-1]:
			return 0;
	if len(strValue) == 1:
		return 0;
	while len(strValue) > 1:
		strValue = strValue[1:];
		if int(strValue) not in listPrime:
			return 0;
	strValue = str(value);
	while len(strValue) > 1:
		strValue = strValue[:-1];
		if int(strValue) not in listPrime:
			return 0;
	return 1;

limitPrime = 1000000;
listPrime = sieve_eratosthenes(limitPrime);
listResult = [];
somme = 0;
for prime in listPrime:
	if truncatable_prime(prime, listPrime) > 0 and len(listResult) < 11:
		listResult.append(prime);
		somme += prime;
print listResult, somme;
