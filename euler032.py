# -*- coding: utf-8 -*-
#Pandigital products
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

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

def calcul(list):
	listRest = list;
	#print list[0] * 10 + list[1],list[2] * 100 + list[3] * 10 + list[4];
	res = (list[0] * 10 + list[1]) * (list[2] * 100 + list[3] * 10 + list[4]);
	if res >= 10000 and res < 1000000:
		res = 0;
	return list[0] * 100000000 + list[1] * 10000000 + list[2] * 1000000 + list[3] * 100000 + list[4] * 10000 + res;

def calcul2(list):
	listRest = list;
	#print list[0] * 10 + list[1],list[2] * 100 + list[3] * 10 + list[4];
	res = list[0] * (list[1] * 1000 + list[2] * 100 + list[3] * 10 + list[4]);
	if res >= 10000 and res < 1000000:
		res = 0;
	return list[0] * 100000000 + list[1] * 10000000 + list[2] * 1000000 + list[3] * 100000 + list[4] * 10000 + res;

list = [0,0,0,0,0]
listProd = [];
for a in range(1, 10):
	for b in range(1, 10):
		if b != a:
			for c in range(1, 10):
				if c != a and c != b:
					for d in range(1, 10):
						if d != c and d != b and d != a:
							for e in range(1, 10):
								if e != d and e != c and e != b and e != a:
									list[0] = a;
									list[1] = b;
									list[2] = c;
									list[3] = d;
									list[4] = e;
									result = calcul(list);
									if isPandigital(result) > 0:
										if result % 10000 not in listProd:
											print result;
											listProd.append(result % 10000);
										else:
											print 'Not included',result;
									result = calcul2(list);
									if isPandigital(result) > 0:
										if result % 10000 not in listProd:
											print result;
											listProd.append(result % 10000);
										else:
											print 'Not included',result;
somme = 0;
for i in listProd:
	somme += i;
print somme;