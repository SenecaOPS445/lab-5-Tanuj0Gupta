#!/usr/bin/env python3
# Author ID: 162349229


def read_file_string(file_name):
    f = open(file_name, 'r')  # Open file in read mode
    content = f.read()  # Read the whole file
    f.close()  # Close file
    return content  # Return content as string

def read_file_list(file_name):
    f = open(file_name, 'r')  # Open file in read mode
    lines = f.readlines()  # Read lines into a list
    f.close()  # Close file
    return [line.strip() for line in lines]  # Remove new-line characters from each line

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')  # Open file in append mode
    f.write(string_of_lines)  # Append string to the file
    f.close()  # Close file

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')  # Open file in write mode
    for line in list_of_lines:
        f.write(line + '\n')  # Write each item from the list as a new line
    f.close()  # Close file

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f_read = open(file_name_read, 'r')  # Open source file in read mode
    f_write = open(file_name_write, 'w')  # Open destination file in write mode
    line_number = 1  # Initialize line number
    for line in f_read:
        f_write.write(str(line_number) + ':' + line)  # Write line number before content
        line_number += 1  # Increment line number
    f_read.close()  # Close source file
    f_write.close()  # Close destination file

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    # Append string to file1 and print its contents
    append_file_string(file1, string1)
    print(read_file_string(file1))

    # Write list to file2 and print its contents
    write_file_list(file2, list1)
    print(read_file_string(file2))

    # Copy contents of file2 to file3 with line numbers and print contents
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
