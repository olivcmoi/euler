# -*- coding: utf-8 -*-
#Powerful digit sum
#A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

limit = 100;
max = 0;
for a in range (1, limit):
	for b in range (1, limit):
		result = pow(a,b);
		somme = 0;
		while result > 0:
			somme += result % 10;
			result /= 10;
		if max < somme:
			print a, b;
			max = somme;

print "Fin", max;