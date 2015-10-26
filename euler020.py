#Factorial digit sum
#n! means n x (n - 1) x ... x 3 x 2 x 1
#For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

def fact(n):
	result = 1;
	while n > 1:
		result *= n;
		n -= 1;
	return result;

strNumber = str(fact(100));
somme = 0;
for i in range(0, len(strNumber)):
	somme += int(strNumber[i]);

print somme;
