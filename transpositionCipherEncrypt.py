# Transposition Cipher Encryption

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    print('"' + ciphertext + '"')

def encryptMessage(key, message):
    # each string in ciphertext represents a column in the grid
    ciphertext = [''] * key

    # loop through each column in ciphertext
    for col in range(key):
        pointer = col

        # keep looping until pointer goes past the length of the message
        while pointer <len(message):
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # convert ciphertext list into a single string value and return it
    return ''.join(ciphertext)

# if this file is run (instead of imported as a module) call
# the main() function.

if __name__ == '__main__':
    main()
