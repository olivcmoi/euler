#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#2, 3, 2^2, 5, 2*3, 7, 2^3, 3^2, 2*5
# 2^3 * 3^2 * 5 * 7
# 11, 2^2 * 3, 13, 7*2, 3*5, 2^4, 17, 2*3^2, 19, 2^2*5
# 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19

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

listPrim = sieve_eratosthenes(20);
listExposant = [];
for i in listPrim:
	listExposant.append(0);

list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
rest = 0;
exposant = 0;
for value in list:
	exposant = 0;
	for index in range(0, len(listPrim)):
		while value % listPrim[index] == 0:
			exposant +=1;
			value = value / listPrim[index];
		if exposant > listExposant[index]:
			listExposant[index] = exposant;
		exposant = 0;
result = 1;
for index in range(0, len(listPrim)):
	result *= pow(listPrim[index], listExposant[index]);
print result;
