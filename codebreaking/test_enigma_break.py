# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time 

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"

def decrypt_with_key(key):
    engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                    rotor.ROTOR_II, rotor.ROTOR_III, key=key,
                                    plugs="AA BB CC DD EE")

    return engine.encipher(ShakesHorribleMessage)

def go():
    all_possible_keys = [ i + j + k for i in capitalLetters for j in capitalLetters for k in capitalLetters ]
    print('Maximum possble attempts required:', len(all_possible_keys))
    
    counter = 0
    for key in all_possible_keys:
        counter += 1

        candidate = decrypt_with_key(key)

        if candidate.endswith((crib,)):
            print('Decoded message:', candidate)
            print('Attempts required:', counter)
            break

if __name__ == "__main__":
    start = time.time()
    go()
    end = time.time()
    print('Time taken:', end - start)

    combinations_with_3_rotors = len(capitalLetters) ** 3
    combinations_with_5_rotors = len(capitalLetters) ** 5
    time_taken_per_combination = (end - start) / combinations_with_3_rotors
    print('Estimated time it would take if there were 5 rotors:', time_taken_per_combination * combinations_with_5_rotors)