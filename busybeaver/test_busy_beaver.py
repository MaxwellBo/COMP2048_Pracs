# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 2 states.

Created on Sat Mar 30 13:55:25 2019

@author: shakes
"""
from turing_machine import TuringMachine

# Python generators are useful for Turing machines because they invert control
# over to the caller. They can generate an output stream lazily
#
# EXAMPLE:
# >>> x = (i ** 2 for i in range(1, 10))
# >>> next(x)
# 1
# >>> next(x)
# 4
# >>> next(x)
# 9
#
# This means that you could construct a Turing Machine lazily, repeatedly
# ask for output with next, _only when needed_, or collect all its outputs 
# if needed
# 
# EXAMPLE:
# >>> x = (i ** 2 for i in range(1, 10))
# >>> list(x)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

#create the Turing machine

bbeaver2 = TuringMachine( 
    { 
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('h', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver3 = TuringMachine( 
    { 
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('c', '1', 'R'),
        ('c', '0'): ('h', '1', 'R'),
        ('c', '1'): ('h', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver4 = TuringMachine( 
    { 
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('c', '1', 'R'),
        ('c', '0'): ('d', '1', 'R'),
        ('c', '1'): ('d', '1', 'R'),
        ('d', '0'): ('h', '1', 'R'),
        ('d', '1'): ('c', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver5 = TuringMachine( 
    { 
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('c', '1', 'R'),
        ('c', '0'): ('d', '1', 'R'),
        ('c', '1'): ('d', '1', 'R'),
        ('d', '0'): ('e', '1', 'R'),
        ('d', '1'): ('c', '1', 'R'),
        ('e', '0'): ('h', '1', 'R'),
        ('e', '1'): ('0', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

if __name__ == "__main__":
    def run(input_):
        w = input_
        # I get 4 ones
        # This is an optimal BB-2. 4 is the maximum number of 1s you can get for 2
        # states
        bbeaver2.debug(w, step_limit=1000)
        print()
        # 6
        bbeaver3.debug(w, step_limit=1000)
        print()
        # 13
        bbeaver4.debug(w, step_limit=1000)
        print()

        bbeaver5.debug(w, step_limit=1000)
        print()

    run('000000000000000000')

