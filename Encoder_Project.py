# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:53:19 2023

@author: blatt
"""

#alphabet for caesar
alph = '_abcdefghijklmnopqrstuvwxyz'

#Function for the caesar decoder
def caesar_decoder(message, offset):
  message = message.lower()
  decoded_message = ""

  for letter in message:
    if letter in alph:
      letter_to_shift_num = ord(letter) - 96 + offset
      mod_letter = letter_to_shift_num % 26
      shift_letter = alph[mod_letter]

      decoded_message += shift_letter
    else:
      decoded_message += letter

  print(decoded_message)

#Function for the caesar encoder
def caesar_encoder(message, offset):
  message = message.lower()
  encoded_message = ""

  for letter in message:
    if letter in alph:
      letter_to_shift_num = ord(letter) - 96 - offset
      mod_letter = letter_to_shift_num % 26
      shift_letter = alph[mod_letter]

      encoded_message += shift_letter
    else:
      encoded_message += letter

  print(encoded_message)

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
      """
      print('Count: ' + str(count))
      print('Letter to shift: ' + letter)
      print('Keyword[count]: ' + str(keyword[count]))
      """

      keyword_num = ord(keyword[count]) - 97
      #print('Keyword_num: ' + str(keyword_num))

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



  print('Decoded message: ' + decoded_message)

#Function for the vigenere encoder
def vigenere_encoder(message, keyword):
  print('\n\nMessage: ' + message)
  message = message.lower()
  decoded_message = ""
  count = 0

  for letter in message:
    if letter in alph:
      """
      print('Count: ' + str(count))
      print('Letter to shift: ' + letter)
      print('Keyword[count]: ' + str(keyword[count]))
      """

      keyword_num = ord(keyword[count]) - 96
      #print('Keyword_num: ' + str(keyword_num))

      keyword_num_mod = keyword_num % 26

      letter_to_shift_num = ord(letter) - 96 - keyword_num_mod
      mod_letter = letter_to_shift_num % 26
      shift_letter = alph[mod_letter]

      #print('Shifted letter: ' + shift_letter + '\n')

      decoded_message += shift_letter

      if count < len(keyword) - 1:
        count += 1
      else:
        count = 0

    else:
      decoded_message += letter



  print('Encoded message: ' + decoded_message)

  vigenere_decoder(decoded_message, keyword)

vigenere_encoder('It was quite the challenge.', 'friends')