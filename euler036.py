#Double-base palindromes
#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

def palindrome(value):
	strValue = str(value);
	for i in range(len(strValue)/2):
		if strValue[i] <> strValue[len(strValue) - 1 - i]:
			return 0;
	strValue = "{0:b}".format(value);
	for i in range(len(strValue)/2):
		if strValue[i] <> strValue[len(strValue) - 1 - i]:
			return 0;
	return 1;

limit = 1000000;
listPalindrome = [];
result = 0;
for value in range(0, limit):
	if palindrome(value) > 0:
		listPalindrome.append(value);
		result += value;
print listPalindrome, result;
