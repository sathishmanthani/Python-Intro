from typing import Dict, Union

grocery_list = ['apple', 'water', 'orange', 'cake', 'popcorn']

for item in grocery_list:
    print ('Current item is: ' + item)

for i in range (10):
    print ('Its iteration number:', i)

# Initializing and sssigning values to dictionary
stocks = {'ticker': 'AMZN', 'PE': 26, 'Price': 2000}
print (stocks)

# Using items() method of dictionary to fetch keys and values
for key, value in stocks.items ():
    print (key, 'is', value)

# Accessing keys using keys() method
for key in stocks.keys ():
    print ('Key is:', key)

# Accessing values using values() method
for value in stocks.values ():
    print ('Value is:', value)

# Assigning more values to the dictionary
stocks['sentiment'] = 'Buy'
print (stocks)

# Initial balance
initial_balance = 2000

# Interest rate
int_rate = 0.06

# Number of years to calculate compound interest for. I took 10 years
years = list (range (1, 11))

# For loop to calaculate the interest itenratively
for year in years:
    '''Compound interest formula'''
    ending_balance = initial_balance * (1 + int_rate) ** year
    print ('Ending balance at year {} = ${:.2f}'.format (year, ending_balance))

# Create Car object using dictionary type
car_1 = {'model': 'toyota', 'cost': 25000}
car_2 = {'model': 'bmw', 'cost': 50000}
car_3 = {'model': 'lexus', 'cost': 6000}

# Create an empty dictionary to initialize
cars = {}

# Now add the car dictionary objects to cars dictionary
cars['car_1'] = car_1
cars['car_2'] = car_2
cars['car_3'] = car_3

# Print cars dictionary
print (cars)

print ('herre')

dict1 = {'steve': 1, 'jobs': 2, 'bill': 3}

for key, value in dict1.items ():
    length = len (key)
    spaces = ''
    for i in range (5 - length):
        spaces = spaces + ' '
    print (key, spaces, '|', value)
