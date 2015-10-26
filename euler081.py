# -*- coding: utf-8 -*-
#Path sum: two ways
#Problem 81
#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

# { 131 673 234 103  18 }
# { 201  96 342 965 150 } 
# { 630 803 746 422 111 }
# { 537 699 497 121 956 }
# { 805 732 524  37 331 }

#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

def sommeproche(data):
	temp = data;
	for i in range(0,len(data)):
		for j in range(0,len(data)):
			if i == 0 and j == 0:
				temp[i][j] = data[i][j];
			elif i == 0:
				temp[i][j] = temp[i][j-1] + data[i][j];
			elif j == 0:
				temp[i][j] = temp[i-1][j] + data[i][j];
			else:
				temp[i][j] = min(temp[i-1][j] + data[i][j], temp[i][j-1] + data[i][j]);
	return temp[len(data)-1][len(data)-1];

data = """131 673 234 103  18 
201  96 342 965 150 
630 803 746 422 111 
537 699 497 121 956 
805 732 524  37 331 """

with open('p081_matrix.txt') as f:
	data = f.read();

#ldata = [map(int, row.split()) for row in data.splitlines()];
ldata = [map(int, row.split(',')) for row in data.splitlines()];
print sommeproche(ldata);
