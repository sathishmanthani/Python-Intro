# Importing JSON library
import json

# Dictionary object of Python
# Accounts dictionary object
accts_dict = { 'accounts':[{'name':'Tom', 'balance':100},
                           {'name':'Brad', 'balance':200},
                           {'name':'Jerry', 'balance':300},
                          ]
             }

# Converting the dictionary object to JSON string
json_obj = json.dumps(accts_dict, indent=4)

# Print the JSON object
print(json_obj)
print(type(json_obj))


# Write the Python object to Json file
with open('C:\\Users\\siris\\Desktop\\MS\\practice\\accts_data.json', 'w') as accounts:
    # Use dump() method to convert dictionary object to json
    json.dump(accts_dict, accounts)


# Reading JSON data from file
with open('C:\\Users\\siris\\Desktop\\MS\\practice\\accts_data.json', 'r') as accounts:
    # Using dump() method to convert JSON data to Python Object
    accounts_json = json.load(accounts)
print(accounts_json)
print(type(accounts_json))

# Reading JSON data from file
with open('C:\\Users\\siris\\Desktop\\MS\\practice\\accts_data.json', 'r') as accounts:
    # Using dump() method to convert JSON data to Python Object
    accounts_json = json.load(accounts)
print(accounts_json)
print(type(accounts_json))

# Accessing value in the json object. It is similar to accessing a list value that is stored in dictionary object
print(accounts_json['accounts'][0]['name'])



# Import JSON module
import json
# Import requests module which will let you access URLs
import requests


# api-endpoint
URL = "https://jsonvat.com/"

# Access the URL and get request. Save the response as response object
response = requests.request("GET", URL)

# Using reponse object's text to convert the string to JSON object
json_obj = json.loads(response.text)


# Pretty printing - Use dumps() method convert the json object back to human readable string
sorted_text = json.dumps(json_obj, indent=4, sort_keys=True)

print(sorted_text)
#print(type(sorted_text))

# Looping through the json object to get Country name followed by effective_from date and standard rate
for item in json_obj['rates']:
    print(item['name'])
    for sub_item in item['periods']:
        print(sub_item['effective_from'], sub_item['rates']['standard'])
