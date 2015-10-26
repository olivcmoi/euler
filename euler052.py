# -*- coding: utf-8 -*-
#Permuted multiples
#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def listFromNb(n):
	list = [];
	while n > 0:
		list.append(n % 10);
		n /= 10;
	list.sort();
	return list;

i = 1;
isOk = 0;
while isOk == 0:
	if len(str(i)) == len(str(i*6)):
		print "possible",i;
		listRef = listFromNb(i);
		if listFromNb(i*2) == listRef and listFromNb(i*3) == listRef and listFromNb(i*4) == listRef and listFromNb(i*5) == listRef and listFromNb(i*6) == listRef:
			isOk = 1;
			print "found";
			break;
	i += 1;

print "Fin", i;