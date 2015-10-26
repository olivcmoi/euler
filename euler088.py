# -*- coding: utf-8 -*-
#Product-sum numbers
#Problem 88
#A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

#For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

#For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

#k=2: 4 = 2 × 2 = 2 + 2
#k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
#k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
#k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
#k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

#Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

#In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

#What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

def SumProd(list):
	sum = 0;
	prod = 1;
	for i in list:
		sum += i;
		prod *= i;
	#print list, sum,prod;
	return sum,prod;

limit = 12000;
cpt=0;
l = 2;
import sys;
listMin = [sys.maxint] * (limit-2);

for k in range(13):
	list = [2] * l;
	bOverflow = False;
	while not bOverflow:
		sum, prod = SumProd(list);
		if len(list)+ prod - sum - 2 < len(listMin):
			if listMin[len(list)+ prod - sum - 2] > prod:
				listMin[len(list)+ prod - sum - 2] = prod;
				#print len(list)+ prod - sum - 2, prod, list;
		else:
			if list[l-1] == list[0]:
				bOverflow = True;
			elif list[l-1] == list[l-2]:
				for k in range(l-1, -1, -1):
					if list[k] <> list[l-1]:
						#print k;
						break;
				list[k] += 1;
				for m in range(k+1, l):
					list[m] = list[k];
				list[l-1] = list[l-2]-1;
			else:
				list[l-2] += 1;
				list[l-1] = list[l-2]-1;
		list[l-1] += 1;
	l += 1;

setMin = set(listMin);
#print list;
#print listMin;
#print setMin;
for i in setMin:
	cpt += i;

print 'Fin', cpt;
