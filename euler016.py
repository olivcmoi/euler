#Power digit sum
#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 21000?
power = 1000;
strResult = str(pow(2,power));
result = 0;
for i in range(0, len(strResult)):
	result += int(strResult[i]);
print result;
