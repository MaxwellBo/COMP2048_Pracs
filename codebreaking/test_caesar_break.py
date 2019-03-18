# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def deshift_character(character, shift):
    if character == " ":
        return " "

    index = (letters.find(character) - shift) % len(letters)
    #                                         ^ wrap around
    return letters[index]

def deshift_message(message, most_common_letter='e'):
    # frequency of each letter, bar spaces
    letter_counts = Counter("".join([ i for i in message if i != ' ']))

    # find max letter
    #                                                 v sort by frequency
    sorted_counts = sorted(letter_counts.items(), key=lambda tup: tup[1], reverse=True)
    max_letter, max_freq = sorted_counts[0] # get the highest freq-letter pair
    print("Max Ocurring Letter:", max_letter)

    # predict shift
    # assume max letter is 'e'
    e_index          = letters.find(most_common_letter)
    max_letter_index = letters.find(max_letter)

    shift = max_letter_index - e_index
    print("Predicted Shift:", shift)

    return "".join([deshift_character(character=i, shift=shift) for i in message])

if __name__ == "__main__":
    deshifted_message = deshift_message(message)
    print("The deshifted message is:", deshifted_message)
