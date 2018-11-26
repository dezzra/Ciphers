# Caesar Cipher

# Caesar Cipher
from tkinter import *

window = Tk()

#the string to be encrypted/decrypted
message = input('Enter a message: ')
message = message.upper()

# the encryption/decryption key
key = 22

# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the message
translated = ''

# run the encryption/decryption code on each symbol in the message string
def encrypt(message):
    global key, translated
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num + key
                #handle wraparound (replace this with modular arithmetic)
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol

def decrypt(message):
    global key, translated
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
                #handle wraparound (replace this with modular arithmetic)
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    #add code to update label here

print(translated)

window.title('Caesar Cipher')
lbl_msg = Label(window, text = 'Message:')
lbl_orig = Label(window, text = 'Original Message:')
lbl_enc = Label(window, text = 'Encrypted Message:')
enc_btn = Button(window, text = 'Encrypt', command=encrypt)
dec_btn = Button(window, text = 'Decrypt', command=decrypt)

lbl_msg.pack(side = LEFT)
lbl_orig.pack(side = LEFT)
lbl_enc.pack(side = LEFT)
enc_btn.pack(side = RIGHT)
dec_btn.pack(side = RIGHT)
window.mainloop()
