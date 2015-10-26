# -*- coding: utf-8 -*-
#Arithmetic expressions
#Problem 93
#By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

#For example,

#8 = (4 * (1 + 3)) / 2
#14 = 4 * (3 + 1 / 2)
#19 = 4 * (2 + 3) − 1
#36 = 3 * 4 * (2 + 1)

#Note that concatenations of the digits, like 12 + 34, are not allowed.

#Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

#Find the set of four distinct digits, a < b &lt c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

import math;

def ope(e,f,o):
	temp = 0.;
	if o == '+':
		temp = float(e) + float(f);
	elif o == '-':
		temp = float(e) - float(f);
	elif o == '*':
		temp = float(e) * float(f);
	elif o == '/':
		if f == 0.0:
			return -10000000;
		else:
			temp = float(e) / float(f);
	else:
		print o;
	#print temp;
	return temp;

def ajoute(value, setCol):
	if value == int(value) and value > 0:
		setCol.add(int(value));

def subPossible(a,b,c,d,list,result):
	for op in list:
		ajoute(ope(ope(ope(a,b,op[0]),c,op[1]),d,op[2]),result);
		#print '(', a, op[0], b, op[1], c, ')', op[2], d, '=', temp; 
		ajoute(ope(ope(a,ope(b,c,op[1]),op[0]),d,op[2]),result);
		#print a, op[0], '(', b, op[1], c, ')', op[2], d, '=', temp; 
		ajoute(ope(ope(a,b,op[0]),ope(c,d,op[2]),op[1]),result);
		#print a, op[0], b, op[1], '(', c, op[2], d, ')', '=', temp; 
		ajoute(ope(a,ope(ope(b,c,op[1]),d,op[2]),op[0]),result);
		#print a, op[0], '(', b, op[1], c, op[2], d, ')', '=', temp; 
		ajoute(ope(ope(a,b,op[0]),ope(c,d,op[2]),op[1]),result);
		#print '(', a, op[0], b, ')', op[1], '(', c, op[2], d, ')', '=', temp; 

def possible(a,b,c,d,list):
	result = set();
	subPossible(a,b,c,d,list,result);
	subPossible(a,b,d,c,list,result);
	subPossible(a,c,b,d,list,result);
	subPossible(a,c,d,b,list,result);
	subPossible(a,d,b,c,list,result);
	subPossible(a,d,c,b,list,result);
	subPossible(b,a,c,d,list,result);
	subPossible(b,a,d,c,list,result);
	subPossible(b,c,a,d,list,result);
	subPossible(b,c,d,a,list,result);
	subPossible(b,d,a,c,list,result);
	subPossible(b,d,c,a,list,result);
	subPossible(c,a,b,d,list,result);
	subPossible(c,a,d,b,list,result);
	subPossible(c,b,a,d,list,result);
	subPossible(c,b,d,a,list,result);
	subPossible(c,d,a,b,list,result);
	subPossible(c,d,b,a,list,result);
	subPossible(d,a,b,c,list,result);
	subPossible(d,a,c,b,list,result);
	subPossible(d,b,a,c,list,result);
	subPossible(d,b,c,a,list,result);
	subPossible(d,c,a,b,list,result);
	subPossible(d,c,b,a,list,result);
	return result;

listOp = ['+', '-', '*', '/'];
list = [];
from itertools import product
for subset in product(listOp, repeat=3):
	list.append(subset[0]+subset[1]+subset[2]);

def find(list):
	maxRow = 0;
	from itertools import combinations
	for subset in combinations(range(1,10), 4):
		#print subset;
		setResult = possible(subset[0],subset[1],subset[2],subset[3], list);
		listResult = [];
		for res in setResult:
			listResult.append(res);
		listResult.sort();
		tempRow = 0;
		tempLastVal = 0;
		for res in listResult:
			if res == tempLastVal + 1:
				tempRow += 1;
				if tempRow > maxRow:
					maxRow = tempRow;
					maxSubset = subset;
			else:
				tempRow = 0;
			tempLastVal = res;
	print maxRow, maxSubset;

#print possible(1,2,3,4,list);
find(list);