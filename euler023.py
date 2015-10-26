#Non-abundant sums
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math

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

def sumOfFactorsPrime(number, primelist):
	n = number;
	sum = 1;
	p = primelist[0];
	j = 0;
	i = 0;

	while p * p <= n and n > 1 and i < len(primelist):
		p = primelist[i];
		i += 1;
		if n % p == 0:
			j = p * p;
			n = n / p;
			while n % p == 0:
				j = j * p;
				n = n / p;
			sum = sum * (j - 1) / (p - 1);
	#A prime factor larger than the square root remains
	if n > 1:
		sum *= n + 1;
	return sum - number;

somme = 0;
limit = 28123;
listAbundant = [];
listPrime = sieve_eratosthenes(int(math.sqrt(limit)));
for value in range(1, limit+1):
	if sumOfFactorsPrime(value, listPrime) > value:
		listAbundant.append(value);

listSommeAbundant = range(0, limit);
for i in range(0, len(listAbundant)):
	for j in range(0, len(listAbundant)):
		if listAbundant[i] + listAbundant[j] < limit:
			listSommeAbundant[listAbundant[i] + listAbundant[j]] = 0;

for i in listSommeAbundant:
	somme += i;

print somme;
