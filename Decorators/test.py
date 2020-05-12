# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 08:57:59 2019

@author: adnan
"""

from decorators import do_twice

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@do_twice
def say_whee():
    print("Whee!")

say_whee()
