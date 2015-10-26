# -*- coding: utf-8 -*-
#Path sum: three ways
#Problem 82
#NOTE: This problem is a more challenging version of Problem 81.

#The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

# 131 673 234 103  18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331

#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

def sommeproche(data):
	import copy
	temp = copy.deepcopy(data);
	for i in range(1,len(data)):
		for j in range(0,len(data)):
			if j == 0:
				temp[j][i] = min(temp[j][i-1] + data[j][i], temp[j+1][i-1] + data[j+1][i] + data[j][i]);
			elif j == len(data)-1:
				temp[j][i] = min(temp[j][i-1] + data[j][i], temp[j-1][i-1] + data[j-1][i] + data[j][i]);
			else:
				temp[j][i] = min( min(temp[j][i-1] + data[j][i], temp[j-1][i-1] + data[j-1][i] + data[j][i]), temp[j+1][i-1] + data[j+1][i] + data[j][i]);
		for j in range(1,len(data)):
			temp[j][i] = min(temp[j][i], temp[j-1][i] + data[j][i]);
		for j in range(len(data)-2,0,-1):
			temp[j][i] = min(temp[j][i], temp[j+1][i] + data[j][i]);
	result = temp[0][len(data)-1];
	for i in range(1,len(data)):
		if result > temp[i][len(data)-1]:
			result = temp[i][len(data)-1];
	return result;

data = """131 673 234 103  18 
          201  96 342 965 150 
          630 803 746 422 111 
          537 699 497 121 956 
          805 732 524  37 331 """

with open('p082_matrix.txt') as f:
	data = f.read();

#ldata = [map(int, row.split()) for row in data.splitlines()];
ldata = [map(int, row.split(',')) for row in data.splitlines()];
print sommeproche(ldata);
