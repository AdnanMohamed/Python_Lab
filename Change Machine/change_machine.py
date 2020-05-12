# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:12:57 2020

Task: The program will simulate a simple change maker for a vending machine.

@author: Adnan H. Mohamed
"""

# =============== FUNCTIONS FOR THE PROGRAM ====================
def init_stock():
    """
    initializes the stock with 25 quarters, dimes, and nickels.
    Returned value is a dictionary of keys:{five, one, quarter, dime, nickel},
    and integer values indicating the number of each category of money available
    in the stock.
    """
    return {"five":0, "one": 0, "quarter": 25, "dime": 25, "nickel":25}

def display_stock(stock):
    """
    Displays the amount of money available in the stock
    """
    print("Stock contains:-")
    for typ in stock:
        print(typ + f"  {stock[typ]}")

def welcome():
    """
    Welcomes the user to the program.
    """
    print("\t*** Welcome to the change maker for the vending machine. ***")
    
def is_valid(money):
    """
    Precondition: money is the a string representing money like 1.34
    Postcondition: returns true if, and only if, the cents amount is
    divisible by 5
    """
    return (float(money) * 100 % 5) == 0

def get_price():
    """
    asks the user for the price of the item or quit if he/she wants.
    Returned value is a amount in dollars (xx.xx) and multiple of 5 cents.
    """

    while (True):
        price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        if(price.capitalize() == 'Q'):
            return -1
        elif price.replace('.', '').isdigit() and not is_valid(price):
            print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
        elif not price.replace('.', '').isdigit():
            print("Illegal entry: Must be a price like (1.75) or 'q' for quit.\n")
        else:
            return float(price)

def menu():
    """
    displays the menu of choices for deposits
    """
    print('''
Menu for deposits:
    'n' - deposit a nickel
    'd' - deposit a dime
    'q' - deposit a quarter
    'o' - deposit one dollar
    'f' - deposit five dollars
    'c' - cancel the purchase
''')
        
def make_change(price, payed, stock):
    """
    Precondition: price is the price of the item, payed is the amount payed (in cents).
    Postcondition: returns a tuple containing a dict  specifying the number of
    quarters; dimes; and nickels of change, and the second element of the tuple
    is a float specifying the amount due for the user (in dollars) in case
    no sufficient coins to make the change.
    """        
    change = {"quarters":0,"dimes":0,"nickels":0}
    due_amount = (payed - price)  # the amount to make change for.
    if(due_amount < 0):         # in case the costumer canceled and asks for refund before
        due_amount = payed      # paying the entire price.
    while due_amount > 0:
        if stock["quarter"] > 0 and 25 <= due_amount:
            due_amount -= 25
            change["quarters"]+=1
            stock["quarter"] -= 1
        elif stock["dime"] > 0 and 10 <= due_amount:
            due_amount -= 10
            change["dimes"] += 1
            stock["dime"] -= 1
        elif stock["nickel"] > 0 and 5 <= due_amount:
            due_amount -= 5
            change["nickels"] += 1
            stock["nickel"] -= 1
        else:
            return (change, due_amount/100)
    
    return (change, due_amount/100)

def amount_in_dollars(option):
    """
        Precondition: option is one of the letters: n, d, q, o, f
        Postcondition: returns .05, .1, .25, 1, or 5
        depending on the option.
    """            
    coin_ref = {"n":.05, "d":.1, "q":.25, "o":1, "f":5}
    return coin_ref[option]    

def calc_total_money(stock):
    """
    returns a tuple (int, int) where the first position specifying
    the amount of dollars and the cents in the second.
    """
    tot_amount = stock["five"] * 5
    tot_amount += stock["one"]
    tot_amount += stock["quarter"] / 4
    tot_amount += stock["dime"] / 10
    tot_amount += stock["nickel"] / 20
    
    return (int(tot_amount), int(str(tot_amount)[str(tot_amount).find('.')+1::]))

def update_stock(option, stock):
    """
    given an option the stock is updated (added to the stock)
    depending on the user choice
    """
    lowered_opt = option.lower()
    if lowered_opt == 'f':
        stock["five"]+=1
    elif lowered_opt == 'o':
        stock["one"] += 1
    elif lowered_opt == 'q':
        stock["quarter"] += 1
    elif lowered_opt == 'd':
        stock["dime"] += 1
    else:
        stock["nickel"] +=1
    
# ======================= END OF FUNCTIONS  ===========================            
            
            
            
if (__name__ == "__main__"):
    welcome()            
    stock = init_stock()   # initializing the stock of money for the change maker.
    
    while(True):
        display_stock(stock)
        price = payment_due = get_price() * 100  # convert the price to cents for ease
        if price == -100:  # the user wants to quit.
            break
        total_payed = 0
        menu() 
        while(payment_due > 0):
            print("Payment due: $" + str(payment_due/100))
            option = input("Indicate deposit option: ")
            if((len(option) > 1) or (option.lower() not in "ndqofc")):
                print(f"Invalid option: {option}")
            elif option.lower() == 'c':
                change = make_change(price, total_payed, stock)     # calculate the refund since the user decided to cancel.
                break
            else:
                total_payed += amount_in_dollars(option) * 100
                payment_due -= amount_in_dollars(option) * 100
                update_stock(option, stock)
        else:
            change = make_change(price, total_payed, stock)
            
        if(total_payed == price):        # the user payed the price exactly.
            print("No change due.")
        else:
            print("Take the change below.")  # prompt the user for the change.
            for t in change[0]:
                if change[0][t] > 0:
                    print(change[0][t], t)
            print()    
        if(change[1] > 0):  # the machine had no sufficient change
            print("Please visit the store manager for remaining refund.")
            dollars = int(change[1])
            cents = int(change[1] * 100 % 100)
            print(f"Amount due is: {dollars} dollars and {cents} cents")
            
    
    dollars, cents = calc_total_money(stock)    
    print(f"Total: {dollars} dollars and {cents} cents")
    