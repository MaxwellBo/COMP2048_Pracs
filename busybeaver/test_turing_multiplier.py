# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine

#create the Turing machine
multiplier = TuringMachine( 
    { 
        ('q0', '1'): ('SkipFirst', '', 'R'),
        # We already have our first iteration; it's the accumulator
        ('SkipFirst', '1'): ('SkipGlobalLoop', 'd', 'R'),
        # 1 * x: Keep x and accept
        ('SkipFirst', '0'): ('qa', '', 'R'),
        ('SkipGlobalLoop', '1'): ('SkipGlobalLoop', '1', 'R'),
        ('SkipGlobalLoop', '0'): ('MarkAccumulatorLoopIndex', '0', 'R'),
        ('MarkAccumulatorLoopIndex', '1'): ('GetToEndOfAccAndMark', '*', 'R'),
        ('GetToEndOfAccAndMark', '1'): ('GetToEndOfAccAndMark', '1', 'R'),
        ('GetToEndOfAccAndMark', ''): ('GetToAccLoopIndexLeft', '#', 'L'),
        ('MarkEndOfAcc', '1'): ('AddOne', '1', 'L'),
        ('AddOne', '1'): ('GetToAccLoopIndexLeft', '1', 'L'),
        ('GetToAccLoopIndexLeft', '1'): ('GetToAccLoopIndexLeft', '1', 'L'),
        ('GetToAccLoopIndexLeft', '#'): ('GetToAccLoopIndexLeft', '#', 'L'),
        ('GetToAccLoopIndexLeft', '*'): ('IncrAccLoopIndex', '1', 'R'),
        ('IncrAccLoopIndex', '#'): ('GetToGlobalLoopIndex', '*', 'L'),
        ('IncrAccLoopIndex', '1'): ('GetToEndOfAccAndAdd', '*', 'R'),
        ('GetToEndOfAccAndAdd', '1'): ('GetToEndOfAccAndAdd', '1', 'R'),
        ('GetToEndOfAccAndAdd', ''): ('GetToAccLoopIndexLeft', '1', 'L'),
        ('GetToEndOfAccAndAdd', '#'): ('GetToEndOfAccAndAdd', '#', 'R'),
        ('GetToGlobalLoopIndex', '1'): ('GetToGlobalLoopIndex', '1', 'L'),
        ('GetToGlobalLoopIndex', '0'): ('GetToGlobalLoopIndex', '0', 'L'),
        ('GetToGlobalLoopIndex', 'd'): ('IncrGlobalLoopIndex', '', 'R'),
        ('GetToAccLoopIndexRight', '1'): ('GetToAccLoopIndexRight', '1', 'R'),
        ('GetToAccLoopIndexRight', '0'): ('GetToAccLoopIndexRight', '0', 'R'),
        ('GetToAccLoopIndexRight', '*'): ('GetToEndOfAccAndMark', '*', 'R'),
        ('IncrGlobalLoopIndex', '1'): ('GetToAccLoopIndexRight', 'd', 'R'),
        ('IncrGlobalLoopIndex', '0'): ('Cleanup', '1', 'R'),
        ('Cleanup', '1'): ('Cleanup', '1', 'R'),
        ('Cleanup', '*'): ('Cleanup', '1', 'R'),
        ('Cleanup', ''): ('PruneLast', '', 'L'),
        ('PruneLast', '1'): ('qa', '', 'R')
    }
)

multiplier.debug('1110111', step_limit=300) # output 1111111111
multiplier.debug('11101', step_limit=300) # output 111
multiplier.debug('10111', step_limit=300) # output 111