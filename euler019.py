#Counting Sundays
#You are given the following information, but you may prefer to do some research for yourself.
#
#1 Jan 1900 was a Monday.
#Thirty days has September,April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def dayPerMonth(year, month):
	result = 0;
	if month == 4 or month == 6 or month == 9 or month == 11:
		result = 30;
	elif month == 2:
		if leapYear(year):
			result = 29;
		else:
			result = 28;
	else:
		result = 31;
	return result;

def leapYear(year):
	result = 0;
	if year % 4 == 0:
		if year % 100 != 0 or year % 400 == 0:
			#leap year
			result = 1;
	return result;

totalJours = 0;
day = 365; #monday + 365j
dayPerWeek = 7;
if day % dayPerWeek == 6:
	totalJours -= 1;
for y in range(1901, 2001):
	for m in range(1, 13):
		day += dayPerMonth(y,m);
		if day % dayPerWeek == 6:
			totalJours += 1;

if day % dayPerWeek == 6:
	totalJours -= 1;

print totalJours
