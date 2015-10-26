# -*- coding: utf-8 -*-
#Powerful digit counts
#The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
#How many n-digit positive integers exist which are also an nth power?

import math;

list = [];
limit = 100;
for a in range(1, limit):
	for b in range(1, limit):
		result = pow(a, b);
		if len(str(result)) == b:
			print a, b;
			if result not in list:
				list.append(result);
print 'Fin',len(list);