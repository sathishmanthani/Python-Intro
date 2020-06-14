# File name: Assignment_2.1.py
# Author: Sathish Manthani
# Date: 06/15/2019
# Course Name: Introduction to Programming DSC510
# Description: This program calculates the total cost for installing fiber optic cable. It also prints the receipt.
# Usage: This program expects company name and length of fiber option cable as input to calculate the cost.

# Importing datetime library to get today's date for printing in receipt
from datetime import datetime

# Welcome message
print("\nHi there!")

# Get company name as input from user
company = input("Please enter the company name:\n")

# Get Fiber Optic length in feet as input from user. Also convert the input to float number
optic_len = float(input("What is the length of the fiber optic cable (in feet) to be installed?\n"))

# Multiply the length with 0.87 to get total cost
total_cost=0.87*optic_len

# Print the receipt to the user
print("                                              ")
print("                                              ")
print("**********************************************")
print("                 RECEIPT                      ")
# Get today's date using the imported library above
print("Date:", datetime.today().strftime('%Y-%m-%d'))
print("Company name:           "+ company)
print("Length of the fiber optic cable:     ", optic_len)
print("Total Cost for installation:         ", total_cost)
print("                                              ")
print("                                              ")
print("----------Have a nice day!--------------------")
print("**********************************************")