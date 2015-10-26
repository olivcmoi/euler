# -*- coding: utf-8 -*-
#Digit cancelling fractions
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

for numerator in range (10, 100):
	for denominator in range (numerator + 1, 100):
		if numerator / 10 == denominator % 10 and numerator / float(denominator) == (numerator % 10) / float(denominator / 10):
			print numerator, denominator, numerator / float(denominator), (numerator % 10) / float(denominator / 10);
		if denominator / 10 == numerator % 10 and denominator % 10 > 0 and  numerator / float(denominator) == (numerator / 10) / float(denominator % 10):
			print numerator, denominator, numerator / float(denominator), (numerator / 10) / float(denominator % 10);