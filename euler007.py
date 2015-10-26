#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?The prime factors of 13195 are 5, 7, 13 and 29.
list = [];
limit = 110000;
multiple = 0;
list = range(0, limit);
for i in list:
	if i >= 2:
		multiple = 2;
		while (i * multiple) < limit:
			list[i * multiple] = 0;
			multiple += 1;
result = 0;
index = 0;
for i in list:
	if i > 0:
		index += 1;
		if index == 10002:
			result = i;
print result;
