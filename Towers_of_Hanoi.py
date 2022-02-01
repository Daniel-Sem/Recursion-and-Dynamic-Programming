# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 09:08:15 2022

@author: dcsem
"""


def move_tower(height, from_pole, to_pole, with_pole):
    
    '''Recursive solution to the Towers of Hanoi problem.'''
    
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(fp,tp):
   
    print("Moving disk from",fp,"to",tp)
          

num = 3
move_tower(num, "one", "two", "three")