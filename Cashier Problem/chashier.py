# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:28:46 2020

@author: Adnan Hashem Mohamed

Program's Task: Given 'n' cents, provide the least number of
coins as change using quarters, dimes, nickles, and pennies.
"""

def change(cents):
    '''
    Precondition: 'cents' is an integer representing the number of cents.
    Postconition: Return value is a tuple of 2 values, first is a dictionary
    where the keys are quarters, dimes, nickles, and pennies; the values are
    the number of of the type of coin used in the change.
    The second element is a number representing the number of coins used in the change
    '''
    coins_reference = {"quarters":25, "dimes":10, "nickles":5, "pennies":1}
    
    coins = {"quarters":0, "dimes":0, "nickles":0, "pennies":0}
    
    for coin in coins_reference:
        while cents - coins_reference[coin] >= 0:
            cents -= coins_reference[coin]
            coins[coin] += 1
    
    tot_num_coins = sum(coins.values())
    
    return (coins, tot_num_coins)        

cents = int(input("Enter the number of cents: "))

coins = change(cents)

print(f"Least number of coins: {coins[1]}")
for coin_type in coins[0]:
    print(f"{coin_type}: {coins[0][coin_type]}")



