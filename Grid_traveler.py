# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:11:15 2022

@author: dcsem
"""
""" In this file there are two implementations of a solution to the grid traveler
    problem - plain recursive and recursive with memoisation.
    
    The script shows the execution times for the two different approaches."""


# from timeit import Timer as t

def gridTraveler(rows,cols):
    
    if rows == 1 and cols == 1:
        return 1
    if rows == 0 or cols == 0:
        return 0
    else:
        return gridTraveler(rows-1, cols) + gridTraveler(rows, cols-1)


def gridTraveler_memo(rows, cols, memo = {}):
    
    key = str(rows) + ','+ str(cols)
    
    if key in memo.keys():
        return memo[key]
    if rows == 1 and cols == 1:
        return 1
    if rows == 0 or cols == 0:
        return 0
    
    else:
        memo[key] = gridTraveler(rows-1, cols) + gridTraveler(rows, cols-1)
        return memo[key]

# print(gridTraveler(2,3))
# print(gridTraveler(4,2))
# print(gridTraveler(6,5))
# print(gridTraveler(8,6))

# print(gridTraveler_memo(2,3))
# print(gridTraveler_memo(4,2))
# print(gridTraveler_memo(6,5))
# print(gridTraveler_memo(8,6))

# rows = 8
# cols = 7

# grid_t = t("gridTraveler(rows,cols)",
# "from __main__ import gridTraveler, rows, cols")

# grid_memo_t = t("gridTraveler_memo(rows,cols)",
# "from __main__ import gridTraveler_memo, rows, cols")

# print('Recursive grid traveler takes: ',grid_t.timeit(number=100), 'miliseconds')
# print('Recursive grid traveler with memo takes: ',grid_memo_t.timeit(number=100), 'miliseconds')
