#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
#Sieve of Eratosthenes
list = [];
limit = 2000000;
multiple = 0;
list = range(0, limit);
for i in list:
	if i >= 2:
		multiple = 2;
		while (i * multiple) < limit:
			list[i * multiple] = 0;
			multiple += 1;
result = 0;
for i in list:
	result += i;
print result - 1;
