#Lattice paths
#Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20x20 grid?

def fact(n):
	result = 1;
	while n > 1:
		result *= n;
		n -= 1;
	return result;

def binominial(n ,k):
	return (fact(n)/(fact(n-k)* fact(k)));

grid = 20;
print binominial(grid+grid,grid);
