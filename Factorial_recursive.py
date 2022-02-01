# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 09:29:15 2022

@author: dcsem
"""

def fact(data):
    
    """Recursive implementation of finding the factorial of a number."""
    
    if data == 0:
        return 1
    
    else:
        return data * fact(data - 1)

# num = int(3)

# print('The factorial of',num,'is:',fact(num))



