# -*- coding: utf-8 -*-
#Cubic permutations
#The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.

import math;


limit = 100000;
i0 = 1;
list = [];
for i in range(i0, limit):
	cube = ''.join(sorted(str(pow(i, 3))));
	if list.count(cube) > 3:
		print pow(list.index(cube)+1,3);
		break;
	list.append(cube);
print 'Fin';