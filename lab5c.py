#!/usr/bin/env python3
# Author ID: 162349229

def add(number1, number2):
    try:
        return int(number1) + int(number2)  # Convert to int and add
    except ValueError:  # If conversion fails
        return 'error: could not add numbers'

def read_file(filename):
    try:
        f = open(filename, 'r')  # Open file in read mode
        lines = f.readlines()  # Read all lines into a list
        f.close()  # Close file
        return lines  # Return the list of lines
    except FileNotFoundError:  # If file does not exist
        return 'error: could not read file'
if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception