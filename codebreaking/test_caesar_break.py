# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 

# frequency of each letter
letter_counts = Counter(message)
print(letter_counts)

# find max letter
#                                                 v sort by frequency
sorted_counts = sorted(letter_counts.items(), key=lambda tup: tup[0], reverse=True)
max_letter, max_freq = sorted_counts[0] # get the highest freq-letter pair
print("Max Ocurring Letter:", max_letter)

# predict shift
# assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

e_index          = letters.find('e')
max_letter_index = letters.find(max_letter)

shift = max_letter_index - e_index
print("Predicted Shift:", shift)

def deshift(x):
    index = (letters.find(x) - shift) % len(letters)
    #                                 ^ wrap around
    return letters[index]

deshifted_message = "".join([deshift(i) for i in message])
print("The deshifted message is:", deshifted_message)