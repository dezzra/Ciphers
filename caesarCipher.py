# Caesar Cipher
from tkinter import *

window = Tk()
window.title('Caesar Cipher')

#display the string to be encrypted/decrypted
#add more code here to do that
#message = message.upper()

# the encryption/decryption key
key = 22

# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# run the encryption/decryption code on each symbol in the message string
def encrypt(msg):
    global key, translated
    translated = ''
    msg = msg.upper()
    lbl_origMsg.configure(text = msg)
    lbl_enc.configure(text = 'Encrypted Message:')
    for symbol in msg:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num + key
                #handle wraparound (replace this with modular arithmetic)
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    lbl_encMsg.configure(text = translated)
    print('Original message:', msg)
    print('Encrypted message:', translated)

def decrypt(msg):
    global key, translated
    translated = ''
    msg = msg.upper()
    lbl_origMsg.configure(text = msg)
    lbl_enc.configure(text = 'Decrypted Message:')
    for symbol in msg:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
                #handle wraparound (replace this with modular arithmetic)
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    lbl_encMsg.configure(text = translated)
    print('Original message:', msg)
    print('Decrypted message:', translated)

def reset():
    global translated
    translated = ''
    lbl_origMsg.configure(text = '')
    lbl_encMsg.configure(text = '')
    pass

def about():
    # add code to explain what this program does, and how, in another popup.
    pass

entry = Entry(window)

message = entry.get()

lbl_msg = Label(window, text = 'Message:')
lbl_orig = Label(window, text = 'Original Message:')
lbl_origMsg = Label(window, text = 'a')
lbl_enc = Label(window, text = 'Encrypted Message:')
lbl_encMsg = Label(window, text = 'b')
enc_btn = Button(window, text = 'Encrypt', command=encrypt(message))
dec_btn = Button(window, text = 'Decrypt', command=decrypt(message))
res_btn = Button(window, text = 'Reset', command=reset())
about_btn = Button(window, text = 'About', command=about())

entry.grid(row = 1, column = 2)
lbl_msg.grid(row = 1, column = 1)
lbl_orig.grid(row = 2, column = 1)
lbl_origMsg.grid(row = 2, column = 2)
lbl_enc.grid(row = 3, column = 1)
lbl_encMsg.grid(row = 3, column = 2)
enc_btn.grid(row = 1, column = 3, rowspan = 2)
dec_btn.grid(row = 1, column = 4, rowspan = 2)
res_btn.grid(row = 3, column = 3)
about_btn.grid(row = 3, column = 4)

window.mainloop()
mainloop()
