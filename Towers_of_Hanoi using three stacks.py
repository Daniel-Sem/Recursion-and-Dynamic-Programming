# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:27:50 2022

@author: dcsem
"""

'''Recursive solution to the Towers of Hanoi problem, that uses three stacks
    from MyStack to represend the towers instead of relying on the recursion stack.'''

from MyStack import Stack as s

def move_tower(height, from_pole, to_pole, with_pole):
    
    
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(fp,tp):
    
    print("Moving disk from",fp,"to",tp)

    if fp == 'one' and tp == 'two':
        stack_two.push(stack_one.pop())
    if fp == 'one' and tp == 'three':
        stack_three.push(stack_one.pop())
    if fp == 'two' and tp == 'three':
        stack_three.push(stack_two.pop())
    if fp == 'two' and tp == 'one':
        stack_one.push(stack_two.pop())
    if fp == 'three' and tp == 'one':
        stack_one.push(stack_three.pop())
    if fp == 'three' and tp == 'two':
        stack_two.push(stack_three.pop())
        
    draw_stacks()
 
def draw_stacks():

    if not stack_one.is_empty():
        print('Stack one:')
        stack_one.show()
    else:
        print("Stack one is empty")
    if not stack_two.is_empty():
        print('Stack two:')
        stack_two.show()
    else:
        print("Stack two is empty")
    if not stack_three.is_empty():
        print('Stack three:')
        stack_three.show()
    else:
        print("Stack three is empty")

stack_one = s()
stack_two = s()
stack_three = s()
num = 3

for i in range(num):
    stack_one.push("0")

draw_stacks()
move_tower(num, "one", "two", "three")
