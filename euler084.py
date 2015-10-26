# -*- coding: utf-8 -*-
#Monopoly odds
#Problem 84
#In the game, Monopoly, the standard board is set up in the following way:

#GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
#H2										C1
#T2										U1
#H1										C2
#CH3	 								C3
#R4	 									R2
#G3	 									D1
#CC3									CC2
#G2										D2
#G1										D3
#G2J F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP

#A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest) * 3, and CH (chance) * 3 changes this distribution.

#In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

#At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

#Community Chest (2/16 cards):
#Advance to GO
#Go to JAIL
#Chance (10/16 cards):
#Advance to GO
#Go to JAIL
#Go to C1
#Go to E3
#Go to H2
#Go to R1
#Go to next R (railway company)
#Go to next R
#Go to next U (utility company)
#Go back 3 squares.
#The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

#By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

#Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

#If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

def roll_dice():
	from random import randint
	return randint(1,4);

def play(listcard,limit):
	cpt = [0] * 40;
	index = 0;
	nbDouble = 0;
	ccpos=0;
	chpos=0;

	for i in range(0, limit):
		dice1 = roll_dice();
		dice2 = roll_dice();
		if dice1 == dice2:
			nbDouble += 1;
		else:
			nbDouble = 0;
		if nbDouble == 3:
			index = listcard.index('JAIL');
			nbDouble = 0;
		else:
			index = (index + dice1 + dice2) % 40;

			if listcard[index][0:2] == 'CH':
				chpos = (chpos + 1) % 16;
				if chpos == 0: # Advance to GO
					index = listcard.index('GO');
				elif chpos == 1: #Go to JAIL
					index = listcard.index('JAIL');
				elif chpos == 2: #Go to C1
					index = listcard.index('C1');
				elif chpos == 3: #Go to E3
					index = listcard.index('E3');
				elif chpos == 4: #Go to H2
					index = listcard.index('H2');
				elif chpos == 5: #Go to R1
					index = listcard.index('R1');
				elif chpos == 6 or chpos == 7: #Go to next R
					if listcard[index] == 'CH1':
						index = listcard.index('R2');
					elif listcard[index] == 'CH2':
						index = listcard.index('R3');
					elif listcard[index] == 'CH3':
						index = listcard.index('R1');
				elif chpos == 8: #Go to next U
					if listcard[index] == 'CH2':
						index = listcard.index('U2');
					else:
						index = listcard.index('U1');
				elif chpos == 9:
					index -= 3;
			if listcard[index][0:2] == 'CC':
				ccpos = (ccpos + 1) % 16;
				if ccpos == 0: #Advance to GO
					index = listcard.index('GO');
				elif ccpos == 1: #Go to JAIL
					index = listcard.index('JAIL');
			if listcard[index] == 'G2J':
				index = listcard.index('JAIL');
		cpt[index] += 1;
	cpt_order = sorted(cpt, reverse=True);
	strRes = "      ";
	total = 0;
	for i in range(0, 40):
		if cpt_order.index(cpt[i]) < 3:
			print cpt_order.index(cpt[i]),i;
	print strRes;

list = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 
		'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 
		'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J',
		'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2'];

limit = 1000000;
play(list,limit);

