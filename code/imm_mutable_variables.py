
Var1=100

print(id(Var1))     #Prints memory location value: 140719583322240
print(id(100))      #Prints memory location value: 140719583322240

Var1=200    #Now Var1 refers to memory location of value 200

print(id(Var1)) #Prints new memroy location code 140719583325440
print(id(100))  #Prints memory location code of 100: 140719583322240
print(id(200))   #Prints memory location code of 200: 140719583325440


list1 = ['apples', 'oranges', 'bananas']
print(list1)
print(id(list1))        #Prints memory location code: 2173159236168

list1.append("avacodo") #Adding a new item to the list. i.e. changing the list
print(list1)            #Prints new list ['apples', 'oranges', 'bananas', 'avacodo']
print(id(list1))        #Prints its original memory location code: 2173159236168. So the new value is added to the existing memory location by changing it.

list1.remove("apples")  #Removing an existing item from the list. i.e. changing the list again
print(list1)            #Prints new list ['oranges', 'bananas', 'avacodo']
print(id(list1))        #Prints its original memory location code: 2173159236168. So the old value was removed to the existing memory location by changing it.

list1.insert(1,"kiwi")  #Inserting a new item at position 1 in the list i.e. changing the list again
print(list1)            #Prints new list ['oranges', 'kiwi', 'bananas', 'avacodo']. Note that, position 1 is 2nd element in the list and position 0 being the 1st element.
print(id(list1))        #Prints its original memory location code: 2173159236168.


