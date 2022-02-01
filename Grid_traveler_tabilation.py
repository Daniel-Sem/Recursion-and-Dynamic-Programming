# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:38:01 2022

@author: dcsem
"""

# Write a function to find all the way to get from the upper left cornder of a
# table to the lower right one.
# The function takes the dimentions as parameters.


def grid_traveler(rows, cols):
    
    """An implementation of a solution to the find-the-shortest-path-in-a-grid
        problem using tabulation."""
    
    table = [[0 for col in range(cols +1)] for row in range(rows + 1)]
    table[1][1] = 1
    
    for row in range(rows+1):
        for col in range(cols+1):
            
            if row+1 <= rows:
                table[row+1][col] += table[row][col]
            if col+1 <= cols:    
                table[row][col+1] += table[row][col]
    

    return table[rows][cols]


# print(grid_traveler(3,4))
# print(grid_traveler(6,7))
# print(grid_traveler(8,10))
# print(grid_traveler(2,4))
