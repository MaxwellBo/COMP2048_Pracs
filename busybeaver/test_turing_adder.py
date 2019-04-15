# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine
from test_turing_machine_example1 import print_transitions

transitions = { 
    #Write your transition rules here as entries to a Python dictionary
    #For example, the key will be a pair (state, character)
    #The value will be the triple (next state, character to write, move head L or R)
    #such as ('q0', '1'): ('q1', '0', 'R'), which says if current state is q0 and 1 encountered
    #then transition to state q1, write a 0 and move head right.
    ('q0', '1'): ('SkipFirst', '1', 'R'),
    ('SkipFirst', '1'): ('SkipFirst', '1', 'R'),
    ('SkipFirst', '0'): ('SkipSecond', '1', 'R'),
    ('SkipSecond', '1'): ('SkipSecond', '1', 'R'),
    ('SkipSecond', ''): ('PruneLast', '', 'L'),
    ('PruneLast', '1'): ('qa', '', 'R')
}

if __name__ == "__main__":
    print_transitions(transitions)

    # This turing machine accepts only the ## string
    # It rejects on any other input
    machine = TuringMachine(transitions)

    def run(input_):
        w = input_
        print("Input:",w)
        print("Accepted" if machine.accepts(w) else "Rejected")
        machine.debug(w)
        print()

    # SHOULD ACCEPT
    run("110111")
    # outputs 11111

    # SHOULD ACCEPT
    run("11101111")
    # outputs 1111111