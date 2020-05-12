# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 06:17:54 2020

@author: adnan
"""
from tkinter import *
import requests
import json

def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"

def my_portfolio():
    #request the data
    api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    
    #save the data in a variable
    api = json.loads(api_request.content)
    
    # Coins which you are investing in
    coins = [
                {
                        "symbol": "BTC",
                        "amount_owned" : 2,
                        "price_per_coin" : 8050.84 # in dollars at the time of purchace
                },
                
                {
                        "symbol": "ETH",
                        "amount_owned" : 3,
                        "price_per_coin" : 188.4 # in dollars at the time of purchace
                },
                        
                {
                        "symbol": "BSV",
                        "amount_owned" : 5,
                        "price_per_coin" : 170 # in dollars at the time of purchace
                }
            ]
            
             
    
    #print the symbol and price of the first 5 cryptocurrencies
    num_rows = 1
    total_p_l = 0
    total_current_value = 0
    for coin in coins:
        for i in range(5):
            if api[i]["symbol"] == coin["symbol"]:
                
                total_amount_paid = coin["amount_owned"] * coin["price_per_coin"]
                current_value = coin["amount_owned"] * float(api[i]["price_usd"])
                total_current_value += current_value
                profit_loss_per_coin = float(api[i]["price_usd"]) - coin["price_per_coin"]
                single_profit = profit_loss_per_coin * coin["amount_owned"]    
                total_p_l += single_profit
                
                name = Label(pycrypto, text = api[i]["name"], bg = "#F3F4F6", fg = "black", font = "Lato 12", padx = "5", pady = "5", borderwidth = 2, relief = "sunken")
                name.grid(column = 0, row = num_rows, sticky = N+S+W+E)
                
                price = Label(pycrypto, text = f"${round(float(api[i]['price_usd']), 2)}", bg = "gold", fg = "brown", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "raised")
                price.grid(column = 1, row = num_rows, sticky = N+S+W+E)
                
                coins_owned = Label(pycrypto, text = coin["amount_owned"], bg = "#F3F4F6", fg = "black", font = "Lato 12", padx = "5", pady = "5", borderwidth = 2, relief = "sunken")
                coins_owned.grid(column = 2, row = num_rows, sticky = N+S+W+E)
                
                total_amount_paid = Label(pycrypto, text = f"${round(total_amount_paid, 2)}", bg = "#F3F4F6", fg = "black", font = "Lato 12", padx = "5", pady = "5", borderwidth = 2, relief = "sunken")
                total_amount_paid.grid(column = 3, row = num_rows, sticky = N+S+W+E)
                
                current_value = Label(pycrypto, text = f"${round(current_value, 2)}", bg = "#F3F4F6", fg = "black", font = "Lato 12", padx = "5", pady = "5", borderwidth = 2, relief = "sunken")
                current_value.grid(column = 4, row = num_rows, sticky = N+S+W+E)
                
                p_l_coin = Label(pycrypto, text = f"${round(profit_loss_per_coin, 2)}", bg = "#F3F4F6", fg = font_color(profit_loss_per_coin), font = "Lato 12", padx = "5", pady = "5", borderwidth = 2, relief = "sunken")
                p_l_coin.grid(column = 5, row = num_rows, sticky = N+S+W+E)
                
                total_profit_label = Label(pycrypto, text = f"${round(single_profit, 2)}", bg = "#F3F4F6", fg = font_color(single_profit), font = "Lato 12", padx = "5", pady = "5", borderwidth = 2, relief = "sunken")
                total_profit_label.grid(column = 6, row = num_rows, sticky = N+S+W+E)
                
                num_rows += 1
    total_pl_label = Label(pycrypto, text = f"${round(total_p_l, 2)}", bg = "#F2F4F6", fg = font_color(total_p_l), font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "sunken")
    total_pl_label.grid(column = 6, row = num_rows, sticky = N+S+W+E)
    
    total_current_val_label = Label(pycrypto, text = f"${round(total_current_value, 2)}", bg = "#F2F4F6", fg = font_color(total_current_value), font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "sunken")
    total_current_val_label.grid(column = 4, row = num_rows, sticky = N+S+W+E)
    
    #clear the what is in api
    api = ""
    
    #Create a button called update
    name = Button(pycrypto, text = "Update", bg = "#274796", fg = "white", command = my_portfolio, font = "Lato 12", padx = "5", pady = "5", borderwidth = 2, relief = "raised")
    name.grid(column = 6, row = num_rows + 1, sticky = N+S+W+E)
# Create an instance of tkinter's class
pycrypto = Tk()
# All application coding and widgets

# The GUI title
pycrypto.title("My Portfolio")

# changing the icon
pycrypto.iconbitmap("smile.ico")

#Adding label background-black, font-white
name = Label(pycrypto, text = "Coin Name", bg = "green", fg = "white", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
name.grid(column = 0, row = 0, sticky = N+S+W+E)

price = Label(pycrypto, text = "Price", bg = "green", fg = "white", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
price.grid(column = 1, row = 0, sticky = N+S+W+E)

coins_owned = Label(pycrypto, text = "Coin Owned", bg = "green", fg = "white", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
coins_owned.grid(column = 2, row = 0, sticky = N+S+W+E)

total_amount_paid = Label(pycrypto, text = "Total Amount Paid", bg = "green", fg = "white", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
total_amount_paid.grid(column = 3, row = 0, sticky = N+S+W+E)

current_value = Label(pycrypto, text = "Current Value", bg = "green", fg = "white", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
current_value.grid(column = 4, row = 0, sticky = N+S+W+E)

p_l_coin = Label(pycrypto, text = "P/L Per Coin", bg = "green", fg = "white", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
p_l_coin.grid(column = 5, row = 0, sticky = N+S+W+E)

total_profit = Label(pycrypto, text = "Total Profit/Loss", bg = "green", fg = "white", font = "Lato 12 bold", padx = "5", pady = "5", borderwidth = 2, relief = "groove")
total_profit.grid(column = 6, row = 0, sticky = N+S+W+E)

my_portfolio()
# Main loop
pycrypto.mainloop()
