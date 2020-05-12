# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:38:35 2020

Describtion: Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number and 
for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.

@author: adnan
"""

def fzbz_print(num):
    '''
        Prints FizzBuzz if the number is a multiple of 3 AND 5.
        Prints Fizz if the number is a multiple of 3 ONLY.
        Prints Buzz if the number is a multiple of 5 ONLY.
        else prints the number
    '''
    if(num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif(num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    else:
        print(num)

for i in range(1,101):
    fzbz_print(i)