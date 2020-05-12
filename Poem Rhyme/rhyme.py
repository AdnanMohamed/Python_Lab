# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:41:47 2019

@author: adnan
"""

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"
sentence1=''.join([x.capitalize()+'! 'for x in start1])
for first,second in rhymes:
    print(sentence1+first.capitalize()+'! ')
    print(start2+' '+second+' ')
