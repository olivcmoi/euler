# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#import math
strResult = '';
max = 0;
for i in range(500,1000):
	for j in range(500,1000):
		strResult = str(i * j);
		if strResult == strResult[::-1] and max < int(strResult):
			print "%s %d %d" % (strResult, i, j);
			max = int(strResult);
