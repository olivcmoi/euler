# -*- coding: utf-8 -*-
#Diophantine equation
#Consider quadratic Diophantine equations of the form:
#x2 – Dy2 = 1
#For example, when D=13, the minimal solution in x is 649² – 13×180² = 1.
#It can be assumed that there are no solutions in positive integers when D is square.
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#32 – 2×22 = 1
#22 – 3×12 = 1
#92 – 5×42 = 1
#52 – 6×22 = 1
#82 – 7×32 = 1
#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

import math;

#Continued fraction expansion
def diophantine(d):
	found = False;
	x = int(math.sqrt(d));
	if x < 2:
		x = 2;
	while not found and x < 1000000000:
		temp = pow(x,2) - 1;
		if temp % d == 0:
			temp /= d;
			if math.sqrt(temp) == int(math.sqrt(temp)):
				found = True;
				return x;
		x += 1;
	return x;

#Continued fraction expansion
def fraction_expansion(n):
	a0 = int(math.sqrt(n));
	m = 0;
	d = 1;
	a = a0;
	period = 0;
	list = [a0];
	while a != 2 * a0:
		m = d * a - m;
		d = (n - pow(m,2)) / d;
		a = int((math.sqrt(n) + m) / d);
		period += 1;
		list.append(a);
	return list;

def convergence(list):
	output = [];
	for i in range(1, len(list) + 1):
		nm1 = 1;
		dm1 = 0;
		for e in reversed(list[0:i]):
			d = nm1;
			n = e * nm1 + dm1;
			dm1 = d;
			nm1 = n;
		output.append((nm1, dm1));
	return output;

max = 0;
index = 0;
limit = 1000;
for i in range(2, limit+1):
	sqrt = math.sqrt(i);
	if sqrt != int(math.sqrt(i)):
		found = False;
		period = 0;
		list = [];
		while not found:
			#res = diophantine(i);
			#print "input, diophantine",i, res;
			if not list:
				list = fraction_expansion(i);
				#print list;
			else:
				if period == 0:
					period = len(list) - 1;
				for j in range(0, period):
					list.append(list[j+1]);
			output = convergence(list);
			#print output;
			for elt in output:
				if pow(elt[0],2) - i * pow(elt[1],2) == 1:
					res = elt[0];
					found = True;
					print i, res;
					break;
		if max < res:
			max = res;
			index = i;
print 'Fin',index,max;