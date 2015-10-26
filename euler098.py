# -*- coding: utf-8 -*-
#Anagramic squares
#Problem 98
#By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36². What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96². We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

#What is the largest square number formed by any member of such a pair?

#NOTE: All anagrams formed must be contained in the given text file.

def isAnagram(list):
	for i in range(0, len(list)):
		ref = list[i];
		ref.sort();
		for j in range(i+1, len(list)):
			current = list[j];
			current.sort();
			if ref == current:
				print 'Anagram', list[i], list[j];

with open('p098_words.txt') as f:
	list = f.read().replace('"','').split(',');
list.sort();
d = dict();
maxlength = 0;
for index, name in enumerate(list):
	if maxlength < len(name):
		maxlength = len(name);
	d[name] = len(name);
	print name, len(name);
#print maxlength;
for size in range(1, maxlength + 1):
	listLen = [];
	for len, word in enumerate(d):
		if len == size:
			print len, word;
			listLen.append(word);
	print size, listLen;
	isAnagram(listLen);
