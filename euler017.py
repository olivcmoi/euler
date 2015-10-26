#Number letter counts
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def decimal(x):
	return {
		0: 0,
		1: len("teen"),
		2: len("twenty"),
		3: len("thirty"),
		4: len("forty"),
		5: len("fifty"),
		6: len("sixty"),
		7: len("seventy"),
		8: len("eighty"),
		9: len("ninety")
	}[x]

def basic(x):
	return {
		0: 0,
		1: len("one"),
		2: len("two"),
		3: len("three"),
		4: len("four"),
		5: len("five"),
		6: len("six"),
		7: len("seven"),
		8: len("eight"),
		9: len("nine"),
		10: len("ten"),
		11: len("eleven"),
		12: len("twelve"),
		13: len("thirteen"),
		14: len("fourteen"),
		15: len("fifteen"),
		18: len("eighteen")
	}[x]

def length(i):
	result = 0;
	if i <= 15 or i == 18:
		result += basic(i);
	elif i < 100:
		result += decimal(i/10);
		result += basic(i - int(i/10) * 10);
	elif i < 1000:
		result += length(i/100);
		result += hundred;
		if i % 100 > 0:
			i = i - int(i / 100) * 100;
			result += lenAnd;
			result += length(i);
	elif i == 1000:
		result += len("onethousand");
	else:
		print i;
	return result;

hundred = len("hundred");
lenAnd = len("and");
result = 0;
for i in range(1,1001):
	result += length(i);
print result;
