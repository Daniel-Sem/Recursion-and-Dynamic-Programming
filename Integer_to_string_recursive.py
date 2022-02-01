# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 09:46:53 2022

@author: dcsem
"""


def toStr(num, base):
    
    '''Using a recursive approach, converts an integer to a string in a given
        base between binary and hexadecimal.'''
    
    convert_string = "0123456789ABCDEF"
    
    if num < base:
        return convert_string[num]
    
    else:
        return toStr(num // base, base) + convert_string[num % base]


print(toStr(10, 2))