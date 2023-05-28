# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:13:01 2023

@author: blatt
"""

import sys

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]

letter_to_num_dict = {key:value for key, value in zip(letters, numbers)}
num_to_letter_dict = {key:value for key, value in zip(numbers, letters)}
    
#Returns a new string based on a message and a keyword.
def vigenere_encoder(message, keyword):
    count = 0
    new_string = ""
    
    print(message)
    for let in message:
        if let == ' ':
            new_string += ' '
            continue
        message_num_by_letter = letter_to_num_dict[let]
        keyword_num_by_letter = letter_to_num_dict[keyword[count % len(keyword)]]
        letn = num_to_letter_dict[(message_num_by_letter + keyword_num_by_letter + 1) % len(numbers)]
        new_string += letn
        count += 1
    return new_string

#Reverses the action of the vigenere encoder function.
def vigenere_decoder(message, keyword):
    count = 0
    new_string = ""
    
    for let in message:
        if let == ' ':
            new_string += ' '
            continue
        message_num_by_letter = letter_to_num_dict[let]
        keyword_num_by_letter = letter_to_num_dict[keyword[count % len(keyword)]]
        letn = num_to_letter_dict[(message_num_by_letter - keyword_num_by_letter - 1) % len(numbers)]
        new_string += letn
        count += 1
    return new_string

#Exits the program.
def exit_program():
    print('Program Ending...')
    sys.exit(0)

#Returns a message.
def input_message():
    while True:
        message = input('Enter a message: ')
        
        for let in message:
            if let not in letters:
                print('Must be letter, number, or sign')
                continue
            else:
                break
        break
        
    return message

#Returns a keyword.
def input_keyword():
    while True:
        keyword = input('Enter a keyword: ')
        
        for let in keyword:
            if let not in letters:
                print('Must be letter, number, or sign')
                continue
            else:
                break
        break
        
    return keyword

#Allows user to enter a message and a keyword and returns an encoded string or returns a decoded string.
def input_coder():
    print("\nWelcome to Vigenere Decoder!")
    while True:
        coder = input("Press 'e' to Encode and 'd' to Decode or 'x' to exit: ")
        if coder == 'x':
            exit_program()
    
        elif coder == 'e':
            message = input_message()
            keyword = input_keyword()
    
            print("\nYour encoded message is: " + str(vigenere_encoder(message, keyword)) + ".")
    
        else: 
            message = input_message()
            keyword = input_keyword()
            print("\nYour decoded message is: " + str(vigenere_decoder(message, keyword) + "."))

#Starts the program
input_coder()