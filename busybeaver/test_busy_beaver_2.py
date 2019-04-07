# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 2 states.

Created on Sat Mar 30 13:55:25 2019

@author: shakes
"""
from turing_machine import TuringMachine


#create the Turing machine
bbeaver = TuringMachine( 
    { 
        #Write your transition rules here as entries to a Python dictionary
        #For example, the key will be a pair (state, character)
        #The value will be the triple (next state, character to write, move head L or R)
        #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
        #then transition to state q1, write a 0 and move head right.
        
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver.debug('00000000000000', step_limit=1000)
