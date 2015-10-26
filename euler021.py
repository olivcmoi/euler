#Amicable numbers
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.
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

limit = 10000;
somme = 0;
list = [];
total_somme = 0;
listPrime = sieve_eratosthenes(int(math.sqrt(limit)));
for value in range(0, limit+1):
	#somme = 0;
	#for factor in range (1, limit/2+1):
	#	if factor >= value:
	#		break;
	#	if value % factor == 0:
	#		somme += factor;
	somme = sumOfFactorsPrime(value, listPrime);
	list.append(somme);
	if somme < value and list[somme] == value:
		print somme,value;
		total_somme = total_somme + somme + value;
#print list;
print total_somme;