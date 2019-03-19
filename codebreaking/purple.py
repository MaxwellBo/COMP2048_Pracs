import string
from test_caesar_break import deshift_message
from collections import Counter
from itertools import permutations

sequence = [ 19, 17, 17, 19, 14, 20, 23, 18, 19, 8, 12, 16, 19, 8, 3, 21, 8, 25, 18, 14, 18, 6, 3, 18, 8, 15, 18, 22, 18, 11 ] 

lowercase = 'abcdefghijklmnopqrstuvwxyz'
message = "".join([ lowercase[i] for i in sequence ])
print('message', message)
# trrtouxstimqtidvizsosgdsipswsl
# SHOULD MAP TO
# attack????????????????????????

domain = set(message)
print("Domain size", len(domain)) # 16

letter_frequency_in_order = 'etaoinshrdlcumwfgypbvkjxqz'
assert(len(letter_frequency_in_order) == 26)

attack_table = {
    't': 'a',
    'r': 't',
    'o': 'c',
    'u': 'k',
}

next_most_frequent_without_attack = "".join([ i for i in letter_frequency_in_order if i not in 'attack'])
remaining_12 = next_most_frequent_without_attack[:12]
print(remaining_12)
# we already know the mappings for 4 of the characters, and we know the domain is 16 characters

known_domain_mappings = set("trou")
unknown_domain_mappings = domain - known_domain_mappings

for permutation in permutations(remaining_12):
    # map the unknown domain onto the remaing most frequent letters
    rest_table = dict(zip(unknown_domain_mappings, permutation))
    combined_table = {**attack_table, **rest_table}

    candidate = "".join([combined_table[i] for i in message])
    print(candidate)
    