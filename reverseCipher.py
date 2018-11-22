#This program takes a message input from the user, and reverses it.

message = input('Enter a message: ')

translated = ''

#We must include '- 1' in the following assignment, because we intend this
#number to be an index, which always starts at 0, not 1.

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1
    print(i, message[i], translated)
