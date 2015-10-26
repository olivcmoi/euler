# -*- coding: utf-8 -*-
#Roman numerals
#Problem 89
#For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

#For example, it would appear that there are at least six ways of writing the number sixteen:

#IIIIIIIIIIIIIIII
#VIIIIIIIIIII
#VVIIIIII
#XIIIIII
#VVVI
#XVI

#However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

#The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

#Find the number of characters saved by writing each of these in their minimal form.

#Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

def value(c):
	if c == 'I':
		return 1;
	elif c == 'V':
		return 5;
	elif c == 'X':
		return 10;
	elif c == 'L':
		return 50;
	elif c == 'C':
		return 100;
	elif c == 'D':
		return 500;
	elif c == 'M':
		return 1000;
	else:
		print c;

def decrypt(number):
	cpt = 0;
	lastNumber = 0;
	for i in number:
		temp = value(i);
		if lastNumber > 0 and temp > lastNumber:
			cpt += temp - 2 * lastNumber;
		else:
			cpt += temp;
		lastNumber = temp;
	return cpt;

def encrypt(number):
	str = '';
	while number <> 0:
		#print number, str;
		if number >= 1000:
			str += 'M';
			number -= 1000;
		elif number >= 900:
			str += 'CM';
			number -= 900;
		elif number >= 500:
			str += 'D';
			number -= 500;
		elif number >= 400:
			str += 'CD';
			number -= 400;
		elif number >= 100:
			str += 'C';
			number -= 100;
		elif number >= 90:
			str += 'XC';
			number -= 90;
		elif number >= 50:
			str += 'L';
			number -= 50;
		elif number >= 40:
			str += 'XL';
			number -= 40;
		elif number >= 10:
			str += 'X';
			number -= 10;
		elif number >= 9:
			str += 'IX';
			number -= 9;
		elif number >= 5:
			str += 'V';
			number -= 5;
		elif number == 4:
			str += 'IV';
			number -= 4;
		elif number >= 1:
			str += 'I';
			number -= 1;
	return str;

with open('p089_roman.txt') as f:
	data = f.read();
Nb = len(data);

cpt = 0;
for line in data.splitlines():
	tempNb = decrypt(line);
	tempStr = encrypt(tempNb);
	cpt += len(line) - len(tempStr);
	if len(line) < len(tempStr):
		print 'error', line, tempNb, tempStr;
print 'Fin', cpt;

