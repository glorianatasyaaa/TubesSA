#!/usr/bin/python3

import random, datetime

'''
function dp(price, n):
input: array of price and n length of rod
output: max profit and cutting point

1.   DP <- array[n+1] of integer
2.   for i <- 1 to n+1 do
3.       for j <- 0 to i do
4.           maxPrice <- getMaxPrice(i, j) // get max price from cutting point
5.       endfor
6.       DP[i] <- maxPrice
7.   endfor
8.   return last element of DP array

function bruteforce(price, n):
kamus:
    bestPrice : integer
    temporaryPrice : integer
    i, j : integer
algoritma:
    1.  bestPrice <- 0
    2.  
    3.  for i <- 0 to 2^(n-1) do
    4.      for j <- 0 to n-1 do
    5.          temporaryPrice <- doCalculateCuttingPoint(i, j)
    6.      endfor
    7.      if temporaryPrice > bestPrice then
    8.          bestPrice <- temporaryPrice
    9.      endif
   10.  endfor
   11.  return bestPrice
'''

def dynamic_programming(price, n, verbose = False):
    dp_vals = [0] * (n + 1)
    dp_rods = [[] for _ in range(n + 1)]
    
    if verbose: print()
    
    for i in range(1, n+1):
        max_val = -1
        best_cut = None
        # print(f'dp[{i}] = max {{')
        for j in range(i):
            # print(f'\tprice[{j}] + dp[{i-j-1}] = {price[j]} + {dp_vals[i-j-1]} = {price[j] + dp_vals[i-j-1]}')
            if price[j] + dp_vals[i-j-1] > max_val:
                max_val = price[j] + dp_vals[i-j-1]
                best_cut = j
        
        dp_vals[i] = max_val
        dp_rods[i] = dp_rods[i - best_cut - 1] + [best_cut + 1]
        
        # print('}')
        # print(f'dp[{i}] = {max_val}')
        # print(f'dp = {dp_vals}')
        if verbose:    
            print(f'{i:>3}', end = ' | ')
            for val in dp_vals:
                print(f'{val:>2} ', end = '')
            print()
    
    if verbose: print()
    
    return dp_vals[n], dp_rods[n]

def bruteforce(price, n, verbose = False):
    best_value = 0
    best_cuts = []
    
    if verbose: print()
    
    for i in range(2 ** (n - 1)):
        tmp_value = 0
        tmp_cut = 0
        tmp_rod = []
        
        for j in range(n - 1):
            if (i >> j) & 1:
                tmp_value += price[tmp_cut]
                tmp_rod.append(tmp_cut + 1)
                tmp_cut = 0
            else:
                tmp_cut += 1
        
        tmp_value += price[tmp_cut]
        tmp_rod.append(tmp_cut + 1)
        
        if tmp_value > best_value:
            best_value = tmp_value
            best_cuts = tmp_rod

        if verbose:
            print(f'{i:>3}', end = ' | ')
            for i in range(len(tmp_rod)):
                print(f'{tmp_rod[i]:>2} ', end = '')
            print()
    
    if verbose: print()
    
    return best_value, best_cuts

price = [1, 5, 8, 9, 10, 17, 17, 20, 21, 24, 30, 35, 40, 43, 50, 55, 60, 66, 70, 74]
rod_length = 8
verbose = True

print("- Data -")
print(f"Price: {price}")
print(f"N: {rod_length}" )

print()
print("- Dynamic Programming -")

start = datetime.datetime.now()
max_value, cuts = dynamic_programming(price, rod_length, verbose=verbose)
end = datetime.datetime.now()

time_execution = (end - start).microseconds

print(f"Max profit: {max_value}")
print(f"Solution: {cuts}")
print(f"Time execution: {time_execution} ms")

print()
print("- Bruteforce -")

start = datetime.datetime.now()
max_value, cuts = bruteforce(price, rod_length, verbose=verbose)
end = datetime.datetime.now()

time_execution = (end - start).microseconds

print(f"Max profit: {max_value}")
print(f"Solution: {cuts}")
print(f"Time execution: {time_execution} ms")
