#!/usr/bin/env python3
# Author ID: 162349229

# Function to read the file and return its contents as a single string
def read_file_string(file_name):
    f = open(file_name, 'r')  # Open file in read mode
    content = f.read()  # Read the entire file
    f.close()  # Close the file
    return content  # Return the content

# Function to read the file and return its contents as a list of lines
def read_file_list(file_name):
    f = open(file_name, 'r')  # Open file in read mode
    lines = f.readlines()  # Read all lines into a list
    f.close()  # Close the file
    return [line.strip() for line in lines]  # Remove newline characters

# Main execution
if __name__ == '__main__':
    file_name = 'data.txt'  # File to read
    print(read_file_string(file_name))  # Print file content as a string
    print(read_file_list(file_name))  # Print file content as a list
