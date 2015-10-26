# -*- coding: utf-8 -*-
#Path sum: four ways
#Problem 83
#NOTE: This problem is a significantly more challenging version of Problem 81.

#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

# 131 673 234 103  18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331

#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.

# verifier si à l'index temp [a][b] est 
def checkValue(temp, data, a, b, max):
	bModify = False;
	if a+1 <= max and temp[a+1][b] + data[a][b] < temp[a][b]:
		temp[a][b] = temp[a+1][b] + data[a][b];
		bModify = True;
	if a-1 >= 0 and temp[a-1][b] + data[a][b] < temp[a][b]:
		temp[a][b] = temp[a-1][b] + data[a][b];
		bModify = True;
	if b+1 <= max and temp[a][b+1] + data[a][b] < temp[a][b]:
		temp[a][b] = temp[a][b+1] + data[a][b];
		bModify = True;
	if b-1 >= 0 and temp[a][b-1] + data[a][b] < temp[a][b]:
		temp[a][b] = temp[a][b-1] + data[a][b];
		bModify = True;
	if bModify:
		# Répercute les voisins
		if a+1 <= max:
			temp = checkValue(temp, data, a+1, b, max);
		if a-1 >= 0:
			temp = checkValue(temp, data, a-1, b, max);
		if b+1 <= max:
			temp = checkValue(temp, data, a, b+1, max);
		if b-1 >= 0:
			temp = checkValue(temp, data, a, b-1, max);
	return temp;

def sommeproche(data):
	import copy
	temp = copy.deepcopy(data);
	for i in range(1, len(data)):
		for j in range(0, i+1):
			if i != j:
				temp[j][i] = temp [j][i-1] + data[j][i];
				temp[i][j] = temp [i-1][j] + data[i][j];
			else:
				temp[i][i] = min(temp[i][i-1] + data[i][i], temp[i-1][i] + data[i][i]);
		for j in range(1,i+1):
			temp[i][j] = min(temp[i][j], temp[i][j-1] + data[i][j]);
			temp[j][i] = min(temp[j][i], temp[j-1][i] + data[j][i]);
		for j in range(i-1,-1,-1):
			temp[i][j] = min(temp[i][j], temp[i][j+1] + data[i][j]);
			temp[j][i] = min(temp[j][i], temp[j+1][i] + data[j][i]);
		for j in range(0, i+1):
			temp = checkValue(temp, data, i-1, j, i);
			temp = checkValue(temp, data, j, i-1, i);
	#print temp;
	return temp[len(data)-1][len(data)-1];

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
