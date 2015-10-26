# -*- coding: utf-8 -*-
#Counting fractions
#Problem 72
#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

#If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

#It can be seen that there are 21 elements in this set.

#How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

def sieve_eratosthenes(limitb, limith):
	list = [];
	multiple = 0;
	list = range(0, limith+1);
	for i in list:
		if i >= 2:
			multiple = 2;
			while (i * multiple) < limith:
				list[i * multiple] = 0;
				multiple += 1;
	result = [];
	for i in list:
		if i >= limitb:
			result.append(i);
	return result;

def brute_force(l):
	list = [];
	for d in range(1, l+1):
		for n in range(1, d):
			if n/float(d) not in list:
				list.append(n/float(d));
	return len(list);

def primeFactor(n, listPrim):
	listFactor = [];
	index = 0;
	while n > 1:
		while n % listPrim[index] == 0:
			if listPrim[index] not in listFactor:
				listFactor.append(listPrim[index]);
			n /= listPrim[index];
		index += 1;
	return listFactor;

def find_better(l):
	cpt = 0;
	phi = range(0, l+1);
	for d in range(2, l+1):
		if phi[d] == d:
			for j in range(d, l+1, d):
				phi[j] = phi[j] / d * (d - 1);
		cpt += phi[d];
	return cpt;

limit = pow(10, 6);
#print brute_force(limit);
print find_better(limit);
