# -*- coding: utf-8 -*-
#Cyclical figurate numbers
#Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

#Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
#Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
#Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
#Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
#Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
#The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

#The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
#Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
#This is the only set of 4-digit numbers with this property.
#Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.

import math;

def triangle(n):
	return n * (n + 1) / 2;

def isTriangle(n):
	triTest = (math.sqrt(1 + 8 * n) - 1.0) / 2.0;
	return triTest == int(triTest);

def square(n):
	return pow(n,2);

def isSquare(n):
	squareTest = math.sqrt(n);
	return squareTest == int(squareTest);

def pentagonal(n):
	return n * (3 * n - 1) / 2;

def isPentagonal(n):
	penTest = (math.sqrt(1 + 24 * n) + 1.0) / 6.0;
	return penTest == int(penTest);

def hexagonal(n):
	return n * (2 * n - 1);

def isHexagonal(n):
	hexaTest = (math.sqrt(1 + 8 * n) + 1.0) / 4.0;
	return hexaTest == int(hexaTest);

def heptagonal(n):
	return n * (5 * n  - 3) / 2;

def isHeptagonal(n):
	heptTest = (math.sqrt(9 + 40 * n) + 3.0) / 10.0;
	return heptTest == int(heptTest);

def octogonal(n):
	return n * (3 * n - 2);

def isOctogonal(n):
	octoTest = (math.sqrt(4 + 12 * n) + 2.0) / 6.0;
	return octoTest == int(octoTest);

def calcul(i, n):
	if i == 0:
		return triangle(n);
	elif i == 1:
		return square(n);
	elif i == 2:
		return pentagonal(n);
	elif i == 3:
		return hexagonal(n);
	elif i == 4:
		return heptagonal(n);
	return octogonal(n);

def fillList(i):
	limitinf = 1000;
	limitsup = 10000;

	list = [];
	n = 1;
	result = calcul(i, n);
	while result < limitsup:
		if result > limitinf and result % 100 > 10:
			list.append(result);
		n += 1;
		result = calcul(i, n);
	return list;

def check(i, val, part1, part2):
	ret = False;
	print "Deb", i, val, part1, part2;
	for j in range(5, i - 1, -1):
		part1[j] = 0;
		part2[j] = 0;
	if val / 100 not in part1 and val % 100 not in part2 and val / 100 <> val % 100:
		part1[i] = val/100;
		part2[i] = val%100;
		ret = True;
		count = 0;
		for j in range(0, i+1):
			count += part1.count(part2[j]);
		if i == 5:
			ret = (count == 6);
		else:
			ret = (count == i);
		print count, i;
	print "Fin", i, val, part1, part2;
	return ret;

def find(list):
	for a in list[0]:
		check(0, a, part1, part2);
		for b in list[1]:
			if check(1, b, part1, part2):
				for c in list[2]:
					if check(2, c, part1, part2):
						for d in list[3]:
							if check(3, d, part1, part2):
								for e in list[4]:
									if check(4, e, part1, part2):
										for f in list[5]:
											if check(5, f, part1, part2):
												print a,b,c,d,e,f;
												return a + b + c + d + e + f;
	return 0;

part1 = [0,0,0,0,0,0];
part2 = [0,0,0,0,0,0];
list = [];
for i in range(0, 6):
	list.append([]);
	temp = fillList(i);
	for t in temp:
		list[i].append(t);
print find(list);
