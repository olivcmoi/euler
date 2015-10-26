# -*- coding: utf-8 -*-
#Prime digit replacements
#By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import math;

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

def isPossible(n):
	ret = 0;
	if n % 10 == 3:
		if '0' in str(n):
			ret = 1;
		if '1' in str(n):
			ret = 1;
		if '2' in str(n):
			ret = 1;
	return ret;

def subNbPrime(strTemp, c, listPrim):
	result = 0;
	min = 1000000000000;
	for i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
		if len(strTemp) == len(str(int(strTemp.replace(c,i)))) and int(strTemp.replace(c,i)) <> 0:
			temp = int(strTemp.replace(c,i)) * 10 + 3;
			if temp in listPrim:
				result += 1;
				if min > temp:
					min = temp;
	return result, min;

def nbPrime(n, listPrim):
	listElt = [];
	strTemp = str(n / 10);
	result = 0;
	min = n;
	if '0' in str(n):
		result, min = subNbPrime(strTemp, '0', listPrim);
	if '1' in str(n):
		result1, min1 = subNbPrime(strTemp, '1', listPrim);
		if result < result1:
			result = result1;
			min = min1;
	if '2' in str(n):
		result1, min1 = subNbPrime(strTemp, '2', listPrim);
		if result < result1:
			result = result1;
			min = min1;
	return result, min;

nb = 8;
limit = 1000000;
listPrim = sieve_eratosthenes(limit);
print "Fin list Prime";

for index in range(0, len(listPrim)):
	if isPossible(listPrim[index]) > 0:
		#print "isPossible", listPrim[index];
		result, min = nbPrime(listPrim[index], listPrim);
		if result == nb:
			print result, min;
			break;

print "Fin";