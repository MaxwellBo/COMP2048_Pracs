import string
from test_caesar_break import deshift_message
from collections import Counter
#      a   t   t   a   c   k                                                   c 
xs = [ 19, 17, 17, 19, 14, 20, 23, 18, 19, 8, 12, 16, 19, 8, 3, 21, 8, 25, 18, 14, 18, 6, 3, 18, 8, 15, 18, 22, 18, 11 ] 

# frequency of each letter, bar spaces
letter_counts = Counter([ i for i in xs ])


lowercase = 'abcdefghijklmnopqrstuvwxyz'



# find max letter
#                                                 v sort by frequency
sorted_counts = sorted(letter_counts.items(), key=lambda tup: tup[1], reverse=True)

print(sorted_counts)

lookup = {
    19: 'a',
    17: 't',
    14: 'c',
    20: 'k',

    18: 'u', # vowel candidates
    8: 'i',
    3: 'u'
}

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def lookup_fallback(i):
    maybeChr = lookup.get(i)

    if maybeChr is None:
        return letters[i]
    else:
        return maybeChr
    
message = "".join([ lookup_fallback(i) for i in xs ])

print(message)