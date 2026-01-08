# The Caesar Cipher is a simple substitution encryption technique where each letter in a message is replaced by a
# letter a fixed number of positions down the alphabet. For example, with a "shift" of 3, the letter A would be
# replaced by D, B would become E, and so on. Historically named after Julius Caesar, it is now considered an
# introductory concept in cryptography rather than a secure way to protect data.

# I have decided to complicate a little and instead of using array for an alphabet, I am going to use ASCII codes
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = ''

while direction != 'end':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'end' to exit the program:\n").lower()
    if direction != "end":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        for letter in text:
            if 96 < ord(letter) < 123:
                if ord(letter) + shift > 122:
                    print(chr(ord(letter) + shift - 25), end="")
                else:
                    print(chr(ord(letter) + shift), end="")
            else:
                print(letter, end="")
        print('')

    elif direction == "decode":
        for letter in text:
            if 96 < ord(letter) < 123:
                if ord(letter) - shift > 96:
                    print(chr(ord(letter) - shift), end="")
                else:
                    print(chr(ord(letter) - shift + 25), end="")
            else:
                print(letter, end="")
        print('')


# Results as expected. output:
# Type 'encode' to encrypt, type 'decode' to decrypt, type 'end' to exit the program:
# encode
# Type your message:
# srecno novo leto!
# Type the shift number:
# 15
# ihtrde dele btje!
# Type 'encode' to encrypt, type 'decode' to decrypt, type 'end' to exit the program:
# decode
# Type your message:
# ihtrde dele btje!
# Type the shift number:
# 15
# srecno novo leto!
# Type 'encode' to encrypt, type 'decode' to decrypt, type 'end' to exit the program:
# end

# Process finished with exit code 0
