#!/usr/bin/python3
##!/home/lxl/anaconda3/envs/crash_course/bin/python
"""
This is a simple Python script that prints a message to the screen.

"""
import sys

def print_hello_world():
    """ print hello world to the screen"""
    print("Hello world!")

def print_bank_character():
    """ a list of different ways to print a blank character"""
    print() # print a blank line
    # print("\n") # print a blank line
    # print("\t") # print a tab
    # print("\r") # print a carriage return
    print("Hello\nPython world!") # 
    print("Hello\tPython world!") # Tab: Hello    Python world!
    print("Hello\rPython world!") # Carriage Return: Python world


def end_para_demo():
    """ demonstration of the end parameter in the print function"""
    print("Hello", end=" ")
    print("world!")

    print("Hello", end="\n")
    print("world!")


def print_interpreter_info():
    """ print the interpreter version and path"""
    print(sys.version) # print the current interpreter version
    print()
    print(sys.executable) # print the current interpreter's path


if __name__ == "__main__":
    print_hello_world()
    print_bank_character()
