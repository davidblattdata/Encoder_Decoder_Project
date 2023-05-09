# Encoder_Decoder_Project
Encodes and Decodes messages using a Caesar Encoder and Vigenere Encoder.

This code provides a user interface to encode or decode messages using either a Caesar cipher or a Vigenere cipher.
A Caesar cipher is a simple substitution cipher in which each letter is shifted by a certain number of positions down the alphabet. The number of positions is called the "offset".
A Vigenere cipher is a more complex substitution cipher in which a message is encrypted using a keyword. Each letter of the keyword is used to shift the letters of the message, and the keyword is repeated as many times as necessary to match the length of the message.
The code includes four functions: caesar_decoder, caesar_encoder, vigenere_decoder, and vigenere_encoder, each of which performs the corresponding cipher operation on a given message.
The code also includes a main loop that prompts the user to choose whether to encode or decode a message, and which cipher to use. The user is then prompted to enter the message and any required parameters (such as the offset or keyword), and the corresponding function is called to encode or decode the message.
The code includes print statements to display the original and encoded/decoded messages for the user.
To exit the program, the user can enter 'x' at any time.
