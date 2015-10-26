# -*- coding: utf-8 -*-
#Cuboid route
#Problem 86
#A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


#However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

#It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

#Find the least value of M such that the number of solutions first exceeds one million.
import math;

def shortest_path(a, b, c):
	return math.sqrt(pow(a,2) + pow(b+c,2));

def shortest_path(a, b):
	return math.sqrt(pow(a,2) + pow(b,2));

limit = 1000000;
cpt = 0;
a = 2;
while cpt < limit:
	for b in range(1, 2*(a+1)):
		temp = shortest_path(a,b);
		if temp == int(temp):
			if b <= a:
				cpt += b/2;
			else:
				cpt += 1 + (a - (b+1)/2);
	a += 1;

print "Fin",a-1, cpt;
