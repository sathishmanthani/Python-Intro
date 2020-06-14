# File name: Assignment_4.1.py
# Author: Sathish Manthani
# Date: 06/28/2019
# Course Name: Introduction to Programming DSC510
# Description: This program calculates the total cost for installing fiber optic cable.
#    It also gives discount to the users who buy cable in bulk.
#    Discount model is like if the user purchases more than 100 feet, they will be charged $0.80 per foot.
#    If the user purchases more than 250 feet, they will be charged $0.70 per foot.
#    If they purchase more than 500 feet, they will be charged $0.50 per foot. Else, charge will be 0.85 per foot.
#    It also prints the receipt.
# Usage: This program expects company name and length of fiber option cable as input to calculate the cost.

# Importing datetime library to get today's date for printing in receipt
from datetime import datetime

# Welcome message
print ("\nHi there!")

# Get company name as input from user
company = input ("Please enter the company name:\n")

# Get Fiber Optic length in feet as input from user. Also convert the input to float number
cable_length = float (input ("What is the length of the fiber optic cable (in feet) to be installed?\n"))


# Following function returns the cost based on the length of the cable and price
def calc_cost(length, price):
    return length * price


# Discount model:
# If the user purchases more than 500 ft then charge 0.5 per foot
if cable_length > 500:
    total_cost = calc_cost(cable_length, 0.5)
# Else if the user purchases more than 250 ft then charge 0.7 per foot
elif cable_length > 250:
    total_cost = calc_cost(cable_length, 0.7)
# Else if the user purchases more than 100 ft then charge 0.8 per foot
elif cable_length > 100:
    total_cost = calc_cost(float (cable_length), 0.8)
# Else if the user purchases less than 100 ft then charge 0.87 per foot
else:
    total_cost = calc_cost(cable_length, 0.87)

# Print the receipt to the user
print ("                                              ")
print ("                                              ")
print ("**********************************************")
print ("                 RECEIPT                      ")
# Get today's date using the imported library above
print ("Date:", datetime.today ().strftime ('%Y-%m-%d'))
print ("Company name:           " + company)
print ("Length of the fiber optic cable:   ", cable_length, "ft")
# Print the total cost after rounding it to 2 decimal points
print ("Total Cost for installation:         $", str (round (total_cost, 2)))
print ("                                              ")
print ("                                              ")
print ("----------Have a nice day!--------------------")
print ("**********************************************")
