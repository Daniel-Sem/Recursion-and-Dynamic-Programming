# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 20:54:30 2022

@author: dcsem
"""

""" In this file there are 3 implementations of a solution to find the n-th
    fibonacci number - iterative, plain recursive and recursive with memoisation.
    
    The script shows the execution times for the three different approaches."""

# from timeit import Timer as t

def fib_rec(num):
    
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        return fib_rec(num-1) + fib_rec(num-2)
    

def fib(num):
    
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        current,previous = 1,1
        
        for i in range(num-2):
            result = current + previous
            previous = current
            current = result
        return result
    
def fib_rec_memo(n, memo = {}):
    
    if n in memo.keys():
        return memo[n]
    
    if n <=2:
        return 1
    
    else:
        memo[n] = fib_rec_memo(n-1, memo) + fib_rec_memo(n-2, memo)
        return memo[n]
        



# num = 15


# print(fib_rec_memo(num))
# print(fib_rec(num))
# print(fib(num))


# fib_t = t("fib(num)",
# "from __main__ import num, fib")
# fib_rec_t = t("fib_rec(num)",
# "from __main__ import num, fib_rec")
# fib_rec_memo_t = t("fib_rec_memo(num)",
# "from __main__ import num, fib_rec_memo")


# print('Iterative fibonacci takes: ',fib_t.timeit(number=100), 'miliseconds')
# print('Recursive fibonacci takes: ',fib_rec_t.timeit(number=100), 'miliseconds')
# print('Recursive fibonacci with memo takes: ',fib_rec_memo_t.timeit(number=100), 'miliseconds')



