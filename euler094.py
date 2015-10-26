# -*- coding: utf-8 -*-
#Almost equilateral triangles
#Problem 94
#It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

#Demonstration:

# a² = h² + (b/2)²

# cas b = a + 1
# a² = h² + ((a+1)/2)² = h² + (a² + 2a + 1) / 4
# 3a² - 2a -1 = 4h²
# 9a² - 6a -3 = 12h²
# 9a² - 6a +1 = 12h² + 4
# (3a - 1)² = 12h² + 4
# ((3a - 1)/2)² = 3h² + 1
# ((3a - 1)/2)² - 3h² = 1

# cas b = a - 1
# a² = h² + ((a-1)/2)² = h² + (a² - 2a + 1) / 4
# 3a² + 2a -1 = 4h²
# 9a² + 6a -3 = 12h²
# 9a² + 6a +1 = 12h² + 4
# (3a + 1)² = 12h² + 4
# ((3a + 1)/2)² = 3h² + 1
# ((3a + 1)/2)² - 3h² = 1

# x = (3a +- 1) / 2
# a = (2x +- 1) / 3

# Pell's equation (also called the Pell–Fermat equation) is any Diophantine equation of the form x²-ny²=1
#x_{k 1} = x_1x_k   ny_1y_k
#y_{k 1} = x_1y_k   y_1x_k

import math;

x1 = 2;
y1 = 1;
x = x1;
y = y1;

sumPerim = 0;
a3 = 0;
limit = 1000000000;

while True:
	# cas b = a + 1
	a3 = (2 * x + 1);
	if a3 > limit:
		break;
	if a3 % 3 == 0 and a3 > 0:
		sumPerim += a3 + 1;

	# cas b = a - 1
	a3 = (2 * x - 1);
	if a3 % 3 == 0 and (a3 / 3)-1 > 0:
		sumPerim += a3 - 1;

	nextx = x1 * x + 3 * y1 * y;
	nexty = x1 * y + y1 * x;
	x = nextx;
	y = nexty;

print sumPerim;
