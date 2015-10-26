# -*- coding: utf-8 -*-
#Digit factorial chains
#Problem 74
#The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

#1! + 4! + 5! = 1 + 24 + 120 = 145

#Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

#169 → 363601 → 1454 → 169
#871 → 45361 → 871
#872 → 45362 → 872

#It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

#69 → 363600 → 1454 → 169 → 363601 (→ 1454)
#78 → 45360 → 871 → 45361 (→ 871)
#540 → 145 (→ 145)

#Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

#How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

def fact(n):
	result = 1;
	while n > 1:
		result *= n;
		n -= 1;
	return result;

def sumfact(n):
	result = 0;
	while n > 0:
		result += fact(n%10);
		n /= 10;
	return result;

limit = pow(10,6);
cpt = 0;
for value in range(1, limit):
	currentList = [value];
	temp = sumfact(value);
	while temp not in currentList:
		currentList.append(temp);
		temp = sumfact(temp);
	if len(currentList) == 60:
		cpt += 1;
		print currentList;
print "Fin", cpt;
