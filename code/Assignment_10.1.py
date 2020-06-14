# File name: Assignment_10.1.py
# Author: Sathish Manthani
# Date: 08/09/2019
# Course Name: Introduction to Programming DSC510
# Description: This program uses object-oriented programming principles to create a CashRegister class and instances it.
#                It also calculates the Total price of the items along with the count of items.
# Usage: This program expects user to select if he/she wants to add a new item followed by the price of the item. It returns count of items and total price.


# Defining class CashRegister
class CashRegister:
    # Initializing the class with the two variables we need in methods
    def __init__(self):
        self.totalPrice = 0
        self.count_of_items = 0

    # Method to add item to the cart. It keeps aggregating the price and increments the count
    def addItem(self, price):
        self.totalPrice += price
        self.count_of_items += 1

    # Instance method to return the total price of the items
    def getTotal(self):
        return round(self.totalPrice, 2)

    # Instance method to return the count of items
    def getCount(self):
        return self.count_of_items


# Main method instanciates the class and gets user input and returns the total price and count of items.
def main():
    # Welcome message
    print("Welcome! Enjoy your shopping today!\n")

    # Creating instance of the class
    cr = CashRegister()

    # Below While loop gets user input continuously till the users chooses not to continue
    while True:
        # Get user input
        user_selection = input("\nWant to add a new item to the register (Y/N)?")
        # If yes then get the price of the item. Handle the exceptions related to input
        if user_selection.upper() == 'Y':
            try:
                item_price = float(input("Enter the price of the item: "))
            except ValueError:
                print("Please enter a valid price")
                continue
            # After getting price, add the item to the register
            cr.addItem(item_price)
        # If the user is done adding items then print the final output and exit
        elif user_selection.upper() == 'N':
            print("------------------------------------")
            print("\nTotal number of items you added:", cr.getCount())
            print("Total price of the items: ${}".format(cr.getTotal()))
            print("\nThank you for shopping with us today!\n")
            print("------------------------------------")
            break
        else:
            print("Invalid selection, Please choose Y or N.")


# Call the main program
if __name__ == '__main__':
    main()
