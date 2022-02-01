# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 10:18:46 2022

@author: dcsem
"""

# Write a function that takes a string as a parameter and returns True if the string is a palindrome,
# False otherwise. Remember that a string is a palindrome if it is spelled the same both forward
# and backward. for example: radar is a palindrome.

def palindrome_checker(data):
    
    '''Compares each element in the original input and the reversed. Returns True
        if they are exactly the same and False otherwise.'''
    
    data = data.lower()

    is_equal = True
    count = (len(data)-1)
    rev_data = rev_str(data)

    while count > 0 and is_equal:
        if data[count] != rev_data[count]:
            is_equal = False
        count = count - 1
            
    return is_equal
    
        
def rev_str(data):
    
    '''Returns the recursively reversed string.'''    
    
    if len(data) == 1:
        return data[0]
    
    else:
        return rev_str(data[1:]) + data[0]



# the_str = 'Kanakanak'

# print(palindrome_checker(the_str))

