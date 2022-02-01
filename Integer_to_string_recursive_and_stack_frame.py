# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 10:35:20 2022

@author: dcsem
"""
from MyStack import Stack


def toStr(num, base):
    
    '''Using an iterative approach, converts an integer to a string in a given
        base between binary and hexadecimal.'''    
    
    convert_string = "0123456789ABCDEF"
    r_stack = Stack()
    
    while num > 0:
        
        if num < base:
            r_stack.push(convert_string[num])
            
        else:
            r_stack.push(convert_string[num % base])
        num = num // base
        
    result = ''
    while r_stack.is_empty() != True:
        result = result + r_stack.pop()
        
    return result

print(toStr(1453,16))
        