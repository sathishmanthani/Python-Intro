# Course Name: Introduction to Programming DSC510
# Date: 7/6/2019
# Author: Sathish Manthani
# Description: This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation).
# Usage: This program expects operation  (+, -, *, / or average) as input and asks for input data according to the operation type chosen

# This function performs addition, subtraction, multiplication and division operations
def performCalculation(operation):
    """Exception handling for the input. Throw exception if the input values are not integers """
    try:
        var1 = int (input ("Enter first number:"))
        var2 = int (input ("Enter second number:"))
    except ValueError:
        return 'That is not a valid integer. Exiting the program...'

    result = None

    '''if loop for +, - , * and / math operations.'''
    if operation == '+':
        var3 = var1 + var2
        result = '\nAddition of {} and {} is {}'.format (var1, var2, var3)
    elif operation == '-':
        var3 = var1 - var2
        result = '\nSubtraction of {} and {} is {}'.format (var1, var2, var3)
    elif operation == '*':
        var3 = var1 * var2
        result = '\nMultiplication of {} and {} is {}'.format (var1, var2, var3)
    elif operation == '/':
        var3 = var1 / var2
        result = '\nDivision of {} by {} is {:.2f}'.format (var1, var2, var3)
    else:
        result = 'Invalid operation'

    return result


# End of Math function


# Function to calculate average of numbers
def calculateAverage():
    """Exception handling for the input. Throws exception if the input values are not integers """
    try:
        count = int (input ("How many numbers do you wish you input: "))
    except ValueError:
        return "That is not a valid number. Exiting the program..."

    '''Initializing loop counter and output value(result) variables '''
    loop_counter = 1
    output_var = 0

    '''While loop for the numbers to be averaged. It runs the number of times the user needs to enter input and totals the values'''
    while loop_counter <= count:
        try:
            input_num = int (input ('{}) Enter number here:'.format (loop_counter)))
        except ValueError:
            return "That is not a valid integer. Exiting the program..."
        loop_counter = loop_counter + 1
        output_var = output_var + input_num
    return '\nAverage of the numbers is {:.2f}'.format (output_var / count)


# End of Average function


# Main program
if __name__ == '__main__':
    '''Get input from user asking for what operation user wants to perform'''
    print ("\nPlease choose the operation you want to perform.")
    operation = input ("Enter operation type here. Permitted values are +, -, * , / or average \n >")

    '''Below code calls the function based on the input operation entered by the user'''
    '''If user enters any unexpected operation value ELSE block prints the error message'''
    if operation in ('+', '-', '*', '/'):
        print (performCalculation (operation))
    elif operation == 'average':
        print (calculateAverage ())
    else:
        print ("You entered an invalid operation. Permitted values are +, -, * , / or average")
        exit (1)
# End of program
