# -*- coding: utf-8 -*-
#Digit fifth powers
#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#As 1 = 14 is not a sum it is not included.
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
somme = 0;

def fifthPowerSumme(value):
	result = 0;
	factor = 100000;
	while factor >= 1:
		result += pow(int(value / factor),5);
		value = value - int(value / factor) * factor;
		factor /= 10;
	return result;

for value in range(1, 6*pow(9,5)):
	if value == fifthPowerSumme(value):
		print "toto",value;
		somme += value;
print somme - 1;