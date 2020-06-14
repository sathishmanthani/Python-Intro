import datetime

# String with trailing and leading spaces
s1 = '   Sathish Manthani     '

s2 = s1.strip()

print('Before strip:', s1)
print('After strip:', s2)

str = '***&Hi**There#####'

#Using strip method to remove leading and trailing special characters
new_str = str.strip('*#&')

print(new_str)
#output:

# Full name string
full_name = 'Tom Hanks'

# Using split method to split full name by first name and last name
name = full_name.split()

# Use name array to print first name and last name
print('First name is {} \nLast name is {}'.format(name[0], name[1]))

#Output

# List of names stored in one string variable
names_string = "Tom Hanks, John Cena, Michael Jackson"

# Split the names and store in array
name_array = names_string.split(',')

#Print the names
for i in name_array:
    print('Name is{} '.format(i))

# list of elements
list = ['a', 'b', 'c']

# Choose separator, you can leave it empty if you want elements to be concatenated without separator
separator = '-'

# Join the elements in array to form a string
str = separator.join(list)

print(str)

dt = datetime.datetime.now()

print(dt)

print(dt.strftime("%Y %M %d"))