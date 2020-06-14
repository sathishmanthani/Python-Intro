
# Week 3 - if statements and boolean
# Author: Sathish Manthani
# Date: 6/16/2019

grade = 91

if grade > 90:
    print('Got a good grade')
elif grade >60:
    print('Got a decent grade')
else:
    print('Bad grade')



for var1 in range(2,10,2):
    print(var1)


list1 = ['a', 'b', 'c']
for var1 in list1:
    print(var1)

str1 = "tashu,manthani"
for var1 in str1.split(','):
    print(var1)

str2 = str1.split(',')
print(str2)


'''

try:
    rate = float(input("Input rate:"))
except F:
    print("Not a number")
else:
    print("Different error")
finally:
    print("Final block")
'''

Balance = 100
Transaction_type = 'Debit'
Transaction_Amt =10

if Transaction_type == 'Debit':
   print('Account debited')
   Balance = Balance - Transaction_Amt
elif Transaction_type == 'Credit':
    print('Account credited')
    Balance = Balance + Transaction_Amt
else:
    print('Account Balance is', Balance)

while True:
    input_text = input('Enter your input or type exit:')
    if input_text == 'exit':
        break
    print('Your input:' + input_text)




