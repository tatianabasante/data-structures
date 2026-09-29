# Name script file: loop1.py
# This script roll dice ten times

from random import randint
import os

def rollDice():
 i = 1
 while i <= 10:
    key = input("Press any key to roll the dice :::")
    print(f"::: Roll {i} :::")
    print(f"Die 1: {randint(1, 6)}")
    print(f"Die 2: {randint(1, 6)}")
    print("\n")
    i += 1
rollDice()