import string

# string.ascii_lowercase contains 'abcdefghijklmnopqrstuvwxyz'
alphabet = string.ascii_lowercase

# Enumerate starting from 1
enumerated_alphabet = list(enumerate(alphabet, start=1))

# Printing the result
for number, letter in enumerated_alphabet:
    print(f"{number}: {letter}")