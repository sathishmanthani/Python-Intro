# Course Name: Introduction to Programming DSC510
# Date: 7/27/2019
# Author: Sathish Manthani
# Description: This program will read data from a file and Calculates total words in it. It also calculates number of occurrences of each word and writes it to given output file.
# Usage: This program reads from Gittysburg.txt file and writes output to target file. User inputs the target file name.

# Importing Operator library to use in pretty printing
from operator import itemgetter


# This function adds words to the dictionary.
# It also checks if the word exists or not and adjusts the word occurrence counter accordingly
def add_word(word1, dict1):
    # Default is_word_new variable to True
    is_word_new = True
    for word, count in dict1.items():
        if word1 == word:
            dict1[word1] = count + 1
            is_word_new = False
    # Set the word occurrence value to 1 if its a new word
    if is_word_new:
        dict1[word1]=1


# This function reads line from the file and splits the lines into words and uses add_word function to add the words to dictionary
def process_line(line1, dict1):
    for word in line1.split():
        add_word(word, dict1)


# Process file function - it takes filename and dictionary as input arguments and appends word/count of occurrences data to the target file
def process_file(file1,dict1):
    with open(file1, 'a') as output_file:
        output_file.write('\n\nWord            Count\n')
        output_file.write('-----------------------\n')
        for key, value in sorted(dict1.items(), key=itemgetter(1), reverse=True):
            output_file.write('{:15s}{:3d}\n'.format(key,value))


# Main function reads from the file, it also does exception handling. Calls the above functions to calculate word occurrences and print the output.
def main():
    print("\nUsage: This program reads from Gittysburg.txt file and writes the output to target file. User needs to enter the target file name.")
    dict1 = {}
    try:
        with open('gettysburg.txt', 'r') as gba_file:
            for line in gba_file:
                process_line(line, dict1)
    except FileNotFoundError:
        print("Error reading from source file. Check the name and path of the file.")
    except IOError:
        print ("Error reading from source file. Check if the file is readable.")

# Get the output file name as input from user and handle exceptions
    try:
        target_file = str(input('Enter target file name: '))
    except IOError:
        print("Invalid target file name or path")
        exit(1)
# Open output file for writing and print the excepted output by calling process_file() method
    try:
        with open(target_file, 'w+') as t_file:
            t_file.write('Length of the dictionary: {}'.format(len(dict1)))
        process_file(target_file, dict1)
        print ('Output is successfully written to the file: {}'.format(target_file))
    except FileNotFoundError:
        print ("Error writing to the target file. Check the name and path of the file.")
    except IOError:
        print ("Error writing to the target file. Check if the file is writeable.")


# Calling the main function
main()

