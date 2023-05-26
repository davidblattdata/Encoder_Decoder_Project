# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:13:01 2023

@author: blatt
"""

#t and u are broken for some reason
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]

lp = {key:value for key, value in zip(letters, points)}
pl = {key:value for key, value in zip(points, letters)}
    
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    
    #Optimize
def vigenere_encoder(message, keyword):
    count = 0
    new_string = ""

    for let in message:
        if let == ' ':
            new_string += ' '
            continue
        num = lp[let]
        numk = lp[keyword[count % len(keyword)]]
        letn = pl[(num + numk + 1) % 52]
        new_string += letn
        count += 1
    print('Test 3: ' + message)
    return new_string

def vigenere_decoder(message, keyword):
    count = 0
    new_string = ""
    
    for let in message:
        if let == ' ':
            new_string += ' '
            continue
        num = lp[let]
        numk = lp[keyword[count % len(keyword)]]
        letn = pl[(num - numk - 1) % 52]
        new_string += letn
        count += 1
    return new_string


while True:
    coder = input("Press 'e' to Encode and 'd' to Decode: ")
    if coder == 'x':
        break
    while True:
        message = input('Enter a message: ')
        if message[0] not in alph:
            print("You need to imput a letter message.")
            continue
        else:
            break
        
    while True:
        keyword = input('Enter a keyword: ')
        if keyword[0] not in alph:
            print("You need to imput a letter message.")
            continue
        else:
            break
    
    
    if coder == 'e':
        print("\nYour encoded message is: " + str(vigenere_encoder(message, keyword)) + ".")

        
    else:
        print("\nYour decoded message is: " + str(vigenere_decoder(message, keyword)) + ".")
        
    break_continue = input("Press 'x' to exit or 'c' to continue: ")
    if break_continue == 'x' or break_continue == 'X':
        print('Program exiting...')
        break
    
    