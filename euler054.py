# -*- coding: utf-8 -*-
#Poker hands
#In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

#High Card: Highest value card.
#One Pair: Two cards of the same value.
#Two Pairs: Two different pairs.
#Three of a Kind: Three cards of the same value.
#Straight: All cards are consecutive values.
#Flush: All cards of the same suit.
#Full House: Three of a kind and a pair.
#Four of a Kind: Four cards of the same value.
#Straight Flush: All cards are consecutive values of same suit.
#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#The cards are valued in the order:
#2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

#Consider the following five hands dealt to two players:

#Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD	2C 3S 8S 8D TD		Player 2
#		Pair of Fives	Pair of Eights
# 2	 	5D 8C 9S JS AC	2C 5C 7D 8S QH		Player 1
#	Highest card Ace	Highest card Queen
# 3	 	2D 9C AS AH AC	3D 6D 7D TD QD		Player 2
#		Three Aces		Flush with Diamonds
# 4	 	4D 6S 9H QH QC	3D 6D 7H QD QS		Player 1
#		Pair of Queens 	Pair of Queens
#		Highest card Nine Highest card Seven
# 5	 	2H 2D 4C 4D 4S	3C 3D 3S 9S 9D		Player 1
#		Full House		Full House
#		With Three Fours with Three Threes
#The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

#How many hands does Player 1 win?

def isFlush(list):
	if list[0][1] == list[1][1] and list[0][1] == list[2][1] and list[0][1] == list[3][1] and list[0][1] == list[4][1]:
		return 1;
	return 0;

def isRoyal(list):
	listOrder = [list[0][0], list[1][0], list[2][0], list[3][0], list[4][0]];
	listOrder.sort();
	if listOrder == ['A', 'J', 'K', 'Q', 'T']:
		return 1;
	return 0;

def value(c):
	if c == 'A':
		return 14;
	elif c == 'K':
		return 13;
	elif c == 'Q':
		return 12;
	elif c == 'J':
		return 11;
	elif c == 'T':
		return 10;
	else:
		return int(c);

def highest(list):
	max = 0;
	for card in list:
		temp = value(card[0]);
		if max < temp:
			max = temp;
	return max;

def isStraight(list):
	listValue = [];
	for card in list:
		listValue.append(value(card[0]));
	listValue.sort();
	setValue = set(listValue);
	if len(listValue) == len(setValue) and listValue[4] - listValue[0] == 4:
		return 1;
	return 0;

import collections

def consecutive(list):
	four = 0;
	three = 0;
	two1 = 0;
	two2 = 0;
	one = 0;
	listValue = [];
	for card in list:
		listValue.append(value(card[0]));
	counter=collections.Counter(listValue);
	for key, val in counter.iteritems():
		if val == 4:
			four = key;
		elif val == 3:
			three = key;
		elif val == 2:
			if two1 == 0:
				two1 = key;
			elif two1 < key:
				two2 = two1;
				two1 = key;
			else:
				two2 = key;
		elif val == 1 and one < key:
			one = key;
	if four > 0:
		return ['4', four];
	result = [];
	if three > 0:
		result.append('3');
		result.append(three);
	if two1 > 0:
		result.append('2');
		result.append(two1);
	if two2 > 0:
		result.append('2');
		result.append(two2);
	if one > 0:
		result.append('1');
		result.append(one);
	return result;

def analyse(list):
	result = [];
	if isFlush(list):
		if isRoyal(list):
			result = ['FR',13];
		elif isStraight(list):
			result = ['FS',highest(list)];
		else:
			result = ['F',highest(list)];
	elif isStraight(list):
		result = ['S',highest(list)];
	else:
		result = consecutive(list);
	return result;

def rate(list):
	result = 0;
	listValue = [];
	for value in list:
		if isinstance(value, basestring):
			if value == 'FR':
				result = 20; 
			elif value == 'FS':
				result = 18; 
			elif value == 'F':
				result = 10; 
			elif value == 'S':
				result = 8; 
			elif int(value) > 0:
				if int(value) == 1:
					result += 1;
				elif int(value) == 4:
					result += 16;
				elif int(value) == 3:
					result += 6;
				elif result == 0:
					result += 2;
				else:
					result *= 2;
			else:
				print value;
		else:
			listValue.append(value);
	listValue.insert(0,result);
	return listValue;

def compare(list1, list2):
	ratePlayer1 = rate(list1);
	ratePlayer2 = rate(list2);
	index = 0;
	while index < len(ratePlayer1) and index < len(ratePlayer2):
		if ratePlayer1[index] < ratePlayer2[index]:
			return 2;
		elif ratePlayer1[index] > ratePlayer2[index]:
			return 1;
		else:
			index += 1;
	return 0;

cpt = 0;
nbcards = 5;
with open('p054_poker.txt') as f:
	list = f.read().splitlines();
for line in list:
	cards = line.split();
	indexcard = 0;
	player1 = [];
	player2 = [];
	for card in line.split():
		if indexcard < nbcards:
			player1.append(card);
		else:
			player2.append(card);
		indexcard += 1;
	print "Player 1",player1,analyse(player1),"Player 2",player2,analyse(player2),compare(analyse(player1),analyse(player2));
	if compare(analyse(player1),analyse(player2)) == 1:
		cpt += 1;

print "Fin", cpt;