#Digit factorials
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def fact(n):
	result = 1;
	while n > 1:
		result *= n;
		n -= 1;
	return result;

limit = 100000
total = 0
for value in range(3, limit):
	temp = value;
	somme = 0;
	while temp > 0 and somme <= value:
		somme += fact(temp % 10);
		temp /= 10;
	if somme == value:
		print value;
		total += somme;
print total