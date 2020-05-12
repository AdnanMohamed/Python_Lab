# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:37:15 2020

This program is a simple interactive program that asks the user
to input the current time and the time to wait. The program displays
for the user the time it'll be after the waiting time.

@author: Adnan H. Mohamed
"""

def sum_time(t1, t2):
    '''
    Precondition: t1 and t2 are tuples of (hour, min) specifying the time in 
    24- hour notation.
    Postcondition: the returned value is a tuple (hour, min) of the time after
    advancing in time with t2.
    '''
    minutes = t1[1] + t2[1]
    hours = (t1[0] + t2[0]) % 24 + (minutes // 60)
    minutes = (t1[1] + t2[1]) % 60     
    return (hours, minutes)

def time_12(time):
    '''
    Precondition: time is a tuple (hours, minutes) representing the time in
    24-hour notation.
    Postcondition: the return value is a string representing the time in
    12-hour notation.
    '''
    
    if(time[0] == 0):
        return '12:' + str(time[1]) + " AM"
    elif(time[0]==12):
        return '12:' + str(time[1]) + " PM"
    if(time[0] < 12):
        return str(time[0]) + ':' + str(time[1]) + " AM"
    else:
        return str(time[0]-12) + ':' + str(time[1]) + " PM"

print("Please enter the time in 24-hour notation format [hh:mm]")

replay = 'yes'
while(replay.capitalize()[0] == 'Y'):
    current_time = input("Please enter the current time: ")
    waiting_time = input("Please enter the waiting time: ")
    
    current_time = current_time.split(':')
    current_time = (int(current_time[0]), int(current_time[1]))
    waiting_time = waiting_time.split(':')
    waiting_time = (int(waiting_time[0]), int(waiting_time[1]))
    
    advanced_time = sum_time(current_time, waiting_time)
    advanced_time = time_12(advanced_time)
    
    print("The time will be: " + advanced_time)
    
    replay = input("Would you like trying again? (yes/no): ") 