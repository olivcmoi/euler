# -*- coding: utf-8 -*-
#Coin sums
#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?
twopound = 1;
onepound = 1;
fiftyp = 1;
twentyp = 2;
fifep = 1;
twop = 1;
onep = 3;

mal = 0;
for a in range(0, 200/100):
	for b in range(0, 200 / 50):
		for c in range(0, 200 / 20):
			for d in range(0, 200 / 10):
				for e in range(0, 200 / 5):
					for f in range(0, 200 / 2):
						for g in range(0, 200 / 1):
							result = a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2 + g * 1;
							if result == 200:
								mal += 1;
								break;
							elif result > 200:
								break;
print mal+8;