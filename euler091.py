# -*- coding: utf-8 -*-
#Right triangles with integer coordinates
#Problem 91
#The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.


#There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
#0 ≤ x1, y1, x2, y2 ≤ 2.


#Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

def isSquare(x1, y1, x2, y2):
	c1 = pow((x1 - 0),2) + pow((y1 - 0),2);
	c2 = pow((x2 - 0),2) + pow((y2 - 0),2);
	c3 = pow((x2 - x1),2) + pow((y2 - y1),2);
	maxc = max(c1,c2,c3);
	return c1+c2+c3 == 2 * maxc;


limit = 6;
dim = range(0,limit + 1);

cpt = 0;
for x1 in dim:
	for y1 in dim:
		for x2 in dim:
			for y2 in dim:
				if not (x1 == x2 and y1 == y2) and not (x1 == 0 and y1 == 0) and not (x2 == 0 and y2 == 0):
					if isSquare(x1,y1,x2,y2):
						cpt += 1;
						#print x1, y1, x2, y2;
print 'Fin', cpt/2;