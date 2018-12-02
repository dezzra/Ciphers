# Caesar Cipher
#the string to be encrypted/decrypted
message = input('Enter a message: ')

# the encryption/decryption key
key = 13

# tells the program to encrypt or decrypt
mode = 'decrypt'

# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the string in message
message = message.upper()

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = (num + key) % len(LETTERS)
        elif mode == 'decrypt':
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
        # add encrypted/decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]
    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

# print the encrypted/decrypted string to the screen
print(translated)
