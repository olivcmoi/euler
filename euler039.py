# -*- coding: utf-8 -*-
#Integer right triangles
#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#{20,48,52}, {24,45,51}, {30,40,50}
#For which value of p ≤ 1000, is the number of solutions maximised?

def listLengthPerimeter(value):
	count = 0;
	for i in range(1, value - 2):
		for j in range (i, value -i -1):
			k = value - i - j;
			if pow(i,2) + pow(j,2) == pow(k,2):
				#print "found",i,j,k;
				count += 1;
	return count;

max = 0;
maxindex = 0;
for i in range(3,1000+1):
	temp = listLengthPerimeter(i);
	if max < temp:
		max = temp;
		maxindex = i;
print "Max",max, maxindex;