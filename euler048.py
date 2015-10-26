# -*- coding: utf-8 -*-
#Self powers
#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

import math;

def power(n):
	return pow(n,n);

result = 0;
for i in range(1,1000+1):
	result += power(i);
print "Fin", result % 10000000000;