# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:30:44 2020

Program Description: The program will compute and display information 
for a utility company which supplies water to its customers.

@author: Adnan H. Mohamed
"""

# ==========   HELPING FUNCITONS  ================

def get_customer_code():
    """
    asks the user for the customer code and returns
    the users entry
    """   
    code = input("Enter customer code [r, c, i]: ")
    return code
        
def calc_gallons(b_reading, e_reading):
    """
    Precondition: b_reading, e_reading are the beginning period reading of the
    meter and the end period reading respectively.
    Postcondition: returns the amount of gallons consumed by the costumer.
    """
    if(b_reading < e_reading):
        return (e_reading - b_reading) / 10
    else:
        return (e_reading + (1000000000 - b_reading)) / 10

def calc_bill(code, gallons):
    """
    Precondition: code, is one of the letters {'r', 'c', 'i'}
    which indicates the type of costumer. 'gallon' is the amount
    of gallons consumed by the customer.
    Postcondition: returns the bill for the customer (in dollars).
    """
    
    res_rate = .0005      # the residential type customer charge rate.
    ind_com_rate = .00025  # the industrial or commercial additional charge rate
    
    c_upper_limit = 4 * (10**6)  # commercial upper limit of gallon consumption before
                                 # applying additional charges.
                                 
    i_upper_limit = 10 * (10**6) # industrial type upper limit of gallon consumption
                                 # before applying additonal charges.
                                 
    if code == 'r':                # if it's a resident bill
        return 5 + (res_rate * gallons)
    elif code == 'c':               # commercial bill
        bill = 1000
        if gallons > c_upper_limit:       # apply charge if consumed more than 4m gallons.
            bill += ind_com_rate * (gallons - c_upper_limit)
        return bill
    else:                           # industrial bill
        if gallons > i_upper_limit:
            return 2000 + (ind_com_rate * (gallons - i_upper_limit))
        elif gallons > 4 * (10**6):
            return 2000
        else:
            return 1000
        
def display_info(code, b_reading, e_reading, gallons, bill):
    """
    displays the customer's information which are given as
    arguments.
    """
    b_formated = "0"*(9-len(str(b_reading))) + str(b_reading)  # beginning meter reading formated as 9 digit.
    e_formated = "0"*(9-len(str(e_reading))) + str(e_reading)  # ending meter reading formated as 9 digit.
    print(f'''
          
    Customer Code: {code}
    Beginning Meter Reading: {b_formated}
    Ending Meter Reading: {e_formated}
    Gallons of consumed water: {gallons}
    Amount Billed: ${round(bill, 2)}
    
    ''')     
    
    # ================= END OF FUNCTIONS =================
    
def valid_reading(meter_reading):
    """
    Returns true if, and only if, meter_reading is
    an integer in the range [0, 999999999], else returns false
    """
    return str(meter_reading).isdigit() and meter_reading in range(1000000000)    
    
if(__name__ == "__main__"):

    print('''\nYou have three letters for customer code: ['r', 'c', 'i']
any letter other than those means you are done.''')

    while(True):
        reply = 'Y'
        customer_code = get_customer_code()
        if(customer_code not in "rci"):
            break
        init_reading = int(input("enter beginning meter reading: "))
        end_reading = int(input("enter ending meter reading: "))
        gallons_consumed = calc_gallons(init_reading, end_reading)
        bill = calc_bill(customer_code, gallons_consumed)
        if(valid_reading(init_reading) and valid_reading(end_reading)):
            display_info(customer_code, init_reading, end_reading, gallons_consumed,bill)
        else:
            print("\n***INVALID READINGS.\n")
