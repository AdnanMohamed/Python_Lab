# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:41:27 2020

@author: adnan
"""
# The program will prompt the user for a floating point number 
# which stands for gallons of gasoline. You will reprint that value 
# along with other information about gasoline and gasoline usage

def gallons_to_liters(gallons):
    '''convert the given gallons of gasoline to the number of liters'''
    liters = 3.7854
    return round(liters*gallons, 2)

def gallons_to_barrels(gallons):
    ''' converts the given gallons of gasoline to the equivalent number of barrels'''
    gallon = 19.5 # 1 barrel = 19.5 gallons of gas
    return round(gallons / gallon, 2)

def gasoline_to_co2(gallons):
    ''' returns the equivalent number of co2 pounds to the gallons of gasoline'''
    pounds = 20 # 1 gallon of gas = 20 pounds of co2
    return round(gallons * pounds, 2)

def gasoline_to_ethanole(gallons):
    ''' returns the equivalent gallons of ethanole'''
    return round(gallons * (115000/75700), 2)

def gas_cost(gallons):
    ''' returns the cost of gallons of gas in dollars'''
    return round(gallons * 4, 2)

gallons_of_gas  = float(input("Please enter the number of gallons of gasoline: "))

print(f"Original number of gasoline: {gallons_of_gas}")
print(f"{gallons_of_gas} gallons of gasoline = {gallons_to_liters(gallons_of_gas)} liters.")
print(f"{gallons_of_gas} gallons of gasoline requires {gallons_to_barrels(gallons_of_gas)} barrels of oil.")
print(f"{gallons_of_gas} gallons of gasoline produces {gasoline_to_co2(gallons_of_gas)} pounds of CO2")
print(f"{gallons_of_gas} gallons of gasoline is energy equivalent to {gasoline_to_ethanole(gallons_of_gas)} gallons of ethanole")
print(f"{gallons_of_gas} gallons of gasoline costs ${gas_cost(gallons_of_gas)}")

