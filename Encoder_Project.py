# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:53:19 2023

@author: blatt
"""

#alphabet for caesar
alph = '_abcdefghijklmnopqrstuvwxyz'

#Function for the caesar decoder
def caesar_decoder(message, offset):
    print('Message: ' + message)
    message = message.lower()
    decoded_message = ""
    
    for letter in message:
        
        if letter in alph:
          letter_to_shift_num = ord(letter) - 96 + (offset - 1)
          mod_letter = letter_to_shift_num % 26
          shift_letter = alph[mod_letter]
        
          decoded_message += shift_letter
        else:
          decoded_message += letter
        
    return decoded_message

print('Decoded Message: ' + caesar_decoder('fcjjm', 2))

#Function for the caesar encoder
def caesar_encoder(message, offset):
    
    print('Message: ' + message)
    message = message.lower()
    encoded_message = ""

    for letter in message:
      if letter in alph:
    
          letter_to_shift_num = ord(letter) - 96 - (offset + 1)
          mod_letter = letter_to_shift_num % 26
          shift_letter = alph[mod_letter]
            
          encoded_message += shift_letter
      else:
        encoded_message += letter
    return encoded_message


#alphabet for Vigenere
alph = 'abcdefghijklmnopqrstuvwxyz'

#Function for the vigenere decoder
def vigenere_decoder(message, keyword):
    print('\n\nMessage: ' + message)
    message = message.lower()
    decoded_message = ""
    count = 0
    
    for letter in message:
      if letter in alph:
    
        keyword_num = ord(keyword[count]) - 96
    
        keyword_num_mod = keyword_num % 26
    
        letter_to_shift_num = ord(letter) - 96 + keyword_num_mod
        mod_letter = letter_to_shift_num % 26
        shift_letter = alph[mod_letter - 1]
    
        #print('Shifted letter: ' + shift_letter + '\n')
    
        decoded_message += shift_letter
    
        if count < len(keyword) - 1:
          count += 1
        else:
          count = 0
    
      else:
        decoded_message += letter

    return decoded_message

#Function for the vigenere encoder
def vigenere_encoder(message, keyword):
    print('\n\nMessage: ' + message)
    message = message.lower()
    decoded_message = ""
    
    count = 0
    for letter in message:
      if letter in alph:
        keyword_num = ord(keyword[count]) - 95
    
        keyword_num_mod = keyword_num % 26
    
        letter_to_shift_num = ord(letter) - 96 - keyword_num_mod
        mod_letter = letter_to_shift_num % 26
        shift_letter = alph[mod_letter]

    
        decoded_message += shift_letter
    
        if count < len(keyword) - 1:
          count += 1
        else:
          count = 0
    
      else:
        decoded_message += letter
        
    return decoded_message
      

#Let's user choose which function to use with usable interface.
while True:
    ed_response = input("'e' to encode or 'd' to decode or 'x' to exit': ")
    if ed_response == 'e':
        ecv_response = input("'c' for a Caesor Encoder or 'v' for a Vigenere Encoder: '")
        if ecv_response == 'c':
            mc_response = input("Enter a message to encode: ")
            oc_response = int(input("Enter an offset value (integer): "))
            print('Encoded Message: ' + str(caesar_encoder(mc_response, oc_response)))
        else:
            mv_response = input("Enter a message to encode: ")
            ov_response = input("Enter a keyword: ")
            print('Encoded Message: ' + vigenere_encoder(mv_response, ov_response))
    elif ed_response == 'd':
        dcv_response = input("'c' for a Caesor Decoder or 'v' for a  Vigenere Decoder: ")
        if dcv_response == 'c':
            mc_response = input("Enter a message to encode: ")
            oc_response = int(input("Enter an offset value (integer): "))
            print(type(oc_response))
            print('Decoded Message: ' + caesar_decoder(mc_response, oc_response))
            
        else:
            mv_response = input("Enter a message to encode: ")
            ov_response = input("Enter a keyword: ")
            print('Decoded Message: ' + vigenere_decoder(mv_response, ov_response))
    else:
        print('Program Exiting...')
        break



