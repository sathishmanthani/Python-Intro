# Course Name: Introduction to Programming DSC510
# Date: 8/3/2019
# Author: Sathish Manthani
# Description: This program will connect to api and fetch Chuck Norris joke randomly upon user input. The program will continuously run till the user inputs to stop.
# Usage: Enter Y to get random Chuck Norris joke, enter any other value to exit

# Importing requests module which helps to connect to REST APIs
import requests


# Define getJoke method to connect to the API and fetch random Chuck Norris joke
def getJoke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    # Raise exception if the connection fails to the URL
    try:
        response.raise_for_status ()
    except requests.exceptions.HTTPError as exp:
        return "Connection error: " + str(exp)
        exit(1)
    # If the connection succeeds then read the fetched JSON string
    resp = response.json ()
    # Access the Joke which is stored at key value 'value'
    joke = resp['value']
    return joke


# Main function to get user input and print the joke to the user
def main():
    input_counter = 1

    while True:
        user_input = input("\nEnter Y to continue, hit any other key to exit:")
        if input_counter == 1 and user_input.upper() == 'Y':
            print("Here's a Chris Norris joke:")
            print(getJoke())
            input_counter += 1
        elif input_counter > 1 and user_input.upper() == 'Y':
            print("Here's another one...")
            print(getJoke())
        else:
            print ("Have a nice day!")
            break


# Call the main function
if __name__ == '__main__':
    main()
