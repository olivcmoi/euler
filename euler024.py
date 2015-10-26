#Lexicographic permutations
#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def fact(n):
	result = 1;
	while n > 1:
		result *= n;
		n -= 1;
	return result;

position = 1000000 - 1;
limit = 10;
result = 0;
list = range(0,limit);
while limit > 0:
	limit -= 1;
	temp = fact(limit);
	print limit,temp;
	result = result * 10 + list[int(position / temp)];
	list.remove(list[int(position / temp)]);
	position -= int(position / temp) * temp;
	print position
print result;

