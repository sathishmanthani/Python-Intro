# Course Name: Introduction to Programming DSC510
# Date: 7/13/2019
# Author: Sathish Manthani
# Description: This program asks user to input temperature, stores the data in list object and displays the maximum and minimum temperature.
# Usage: This program expects temperatures as input, type stop to end the input. Displays maximum, minimum temperatures as output.


# Get the user input
def get_input():
    # Empty list
    temp_list = []
    while True:
        print("Enter temperature value, or type Stop to end:")
        user_input = input("")
        # Break the loop if user is done entering values
        if user_input.lower() == 'stop':
            break
        # Exception handling if a non integer is entered
        try:
            temp_list.append(int(user_input))
        except ValueError:
            print("That's not a valid number. Exiting the program...")
            exit(1)
    return temp_list


# Function to determine max value in the list
def max_temp(list):
    max_value = None
    # Using enumerate function to get index and value in the list
    # Below loop makes first value in the list as max and reassigns if any other value is greater in the list
    for key,value in enumerate(list):
         if key == 0:
             max_value = value
         elif max_value < value:
             max_value = value
    return max_value


# Function to determine min value in the list
def min_temp(list):
    min_value = None
    # Using enumerate function to get index and value in the list
    # Below loop makes first value in the list as max and reassigns if any other value is greater in the list
    for key,value in enumerate(list):
         if key == 0:
             min_value = value
         elif min_value > value:
             min_value = value
    return min_value


# Main function
def main():
    temp_list = get_input()
    print("List of temperatures entered:", temp_list)
    print("Count of temperatures entered:", len(temp_list))

#   print("Maximum temperature is:", max(temp_list))
    print("Maximum temperature is:", max_temp(temp_list))

#   print("Minimum temperature is:", min(temp_list))
    print("Minimum temperature is:", min_temp(temp_list))


#Main program
if __name__ == '__main__':
    main()






