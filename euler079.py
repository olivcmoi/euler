# -*- coding: utf-8 -*-
#Passcode derivation
#Problem 79
#A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

#The text file, keylog.txt, contains fifty successful login attempts.

#Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

keylogs = list(map(lambda x: list(map(int, x.strip())), open('p079_keylog.txt').readlines()))
#print keylogs

all_digits = list({j for i in keylogs for j in i})
#print all_digits

for key in keylogs:
    #print key;
    digit_pos = [0,0,0]
    while not (digit_pos[0] < digit_pos[1] < digit_pos[2]):
        digit_pos = [all_digits.index(key[0])]
        #print digit_pos;
        for i in range(1, 3):
            index = all_digits.index(key[i])
            digit_pos.append(index)
            if index < digit_pos[i-1]:
                all_digits[index], all_digits[digit_pos[i-1]] = all_digits[digit_pos[i-1]], all_digits[index]
                digit_pos[i], digit_pos[i-1] == digit_pos[i-1], digit_pos[i]
                #print all_digits;

print(all_digits)