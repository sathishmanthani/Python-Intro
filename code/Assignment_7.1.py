# Course Name: Introduction to Programming DSC510
# Date: 7/20/2019
# Author: Sathish Manthani
# Description: This program will read data from a file and Calculates total words in it. It also prints number of occurrences of each word in the file.
# Usage: This program reads and prints data from Gittysburg.txt file. No input is needed from the user.


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


# This function prints the ouptut in easily readable format
def pretty_print(dict1):
    print('\nLength of the dictionary:', len(dict1))
    print('Word            Count')
    print('-----------------------')
    for key, value in sorted(dict1.items(), key=itemgetter(1), reverse=True):
        length = len(key)
        # spaces = ''
        # for i in range(14-length):
        #     spaces = spaces + ' '
        # print(key, spaces, value)
        print('{:15s}{:3d}'.format(key,value))

# Main function reads from the file, it also does exception handling. Calls the above functions to calculate word occurrences and print the output.
def main():
    dict1 = {}
    try:
# gba_file = open('gettysburg.txt', 'r')
        gba_file = open('test_file.txt', 'r')
        for line in gba_file:
            process_line(line, dict1)
        pretty_print(dict1)
        gba_file.close()
    except FileNotFoundError:
        print("Error reading from the file. Check the name and path of the file.")
    except IOError:
        print ("Error reading from the file. Check if the file is readable.")


# Calling the main function
main()

