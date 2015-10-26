# -*- coding: utf-8 -*-
#Counting rectangles
#Problem 85
#By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

# 1 x 1 = 6 ; 1 x 2 = 4; 1 x 3 = 2 ; 2 x 1 = 3 ; 2 x 2 = 2 ; 2 x 3 = 1 => 6 + 4 + 2 + 3 + 2 + 1 = 18

#Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

def nbMove(a,b,long,larg):
	cpt = 0;
	for c in range(0, larg):
		for d in range(0, long):
			if c+a <= larg and d+b <= long:
				cpt +=1;
	return cpt;

def nbArea(long, larg):
	cpt = 0;
	for a in range(0, larg):
		for b in range(0, long):
			cpt += (larg - a) * (long - b); #nbMove(a,b,long,larg);
			print a, larg, b, long, cpt;
	return cpt;

limit = 2000000;
larg=2;
cpt=0;

#print nbArea(52,53);

import math;

closestarearects = 0;
closestarea = 0;
target = 2000000;

def rectangles(x, y):
	rects = 0;
	for i in range(0, x):
		for j in range(0, y):
			rects += (x - i) * (y - j);
	return rects;

#for x in range(1, 2000):
#	for y in range(x, 2000):
#		rects = rectangles(x,y);
#		if math.fabs(closestarearects - target) > math.fabs(rects - target):
#			closestarea = x * y;
#			closestarearects = rects;
#			print x, y, rects, closestarea, closestarearects
#		if rects > target:
#			break;

error = 9999999999;
closestarea = 0;
target = 2000000;
 
x = 2000;
y = 1;
 
while x >= y:
	rects = x * (x + 1) * y * (y + 1) / 4;
	if error > math.fabs(rects - target):
		closestarea = x * y;
		error = math.fabs(rects - target);
		print x, y, rects, closestarea, closestarearects
	if rects > target:
		x -= 1;
	else:
		y += 1;
