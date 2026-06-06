#!/usr/bin/env python3

class Coffee:
    def __init__(self,size,price):
        self.size=size
        self.price=price

    def tip(self):
        print("This coffee is great.here's a tip!")
        self.price +=1

size_input=input("Enter Coffee size:")  
price_input=float(input("Enter Coffee price:"))      

if size_input != "Small"  and size_input != "Medium" and size_input!= "Large":
    print("size must be Small,Medium or Large")
else:    
    coffee_details=Coffee(size_input,price_input)
    coffee_details.tip()
