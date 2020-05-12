# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 08:51:09 2019

@author: adnan
"""

import functools

def do_twice(func):
    @functools.wraps(func)
    def inner_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return inner_do_twice