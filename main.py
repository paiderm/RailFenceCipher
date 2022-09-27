'''
    Since the message that is encrypted is the same length as the decrypted message, we can insert all the letters in the
    indicies === 0 (mod 2(depth-1)), then === +/- 1, then +/- 2, ..., lastly depth-1
'''
def decryptMessage(message, depth):
    decryptedMessage = ' ' * len(message)
    mod = 2 * (int(depth) - 1)

    counter = 0
    for j in range(int(depth)):
        for spot in range(len(decryptedMessage)):
            if (spot % mod == j or spot % mod == mod - j):
                decryptedMessage = replace_char_at_index(decryptedMessage, spot, message[counter])
                counter += 1

    return decryptedMessage

'''
    encryptMessage(message, depth) looks for all of the letters and indicies +/- i and puts into the encrypted message
    encryptedMessage = [0] + [+/- 1] + [+/- 2] + ... + [depth - 1]
'''
def encryptMessage(message, depth):
    encryptedMessage = ''
    mod = 2*(int(depth) - 1)

    for i in range(int(depth)):
        for j in range(len(message)):
            if j % mod == i or j % mod == mod - i:
                encryptedMessage += message[j]

    return encryptedMessage;

def encryptMessageAlternate(message, depth):
    encryptedMessage = ''
    firstMod = 2*(int(depth) - 1)
    mod = firstMod

    for i in range(int(depth)):
        # This block of code accounts for the "peaks" of the fence
        if mod == firstMod:
            # add characters that are in [0] equivalence class (mod mod) to encrypted message and replace with spaces in the original message
            # replace with spaces to not mess up the indexing
            for j in range(0, len(message)):
                if j % mod == 0:
                    encryptedMessage += message[j]
                    message = replace_char_at_index(message, j, ' ')
            # squish the word back together
            message = message.replace(" ", "")
            # subtract 1 from the mod since peaks only have 1 letter ???
            mod -= 1
        # This block of code accounts for the middle section of the fence
        elif mod != 1:
            for j in range(0, len(message)):
                # look for characters at the negative sloped part of fence
                # add characters that are in [0] equivalence class (mod mod) to encrypted message and replace with spaces in the original message
                if j % mod == 0:
                    encryptedMessage += message[j]
                    message = replace_char_at_index(message, j, ' ')
                # checks if there is a corresponding positive sloped part of the fence
                # add characters that are in [mod - 1] === [-1] equivalence class (mod mod) to encrypted message and replace with spaces in the original message
                if mod != firstMod and j != 1 and j % mod == mod - 1:
                    encryptedMessage += message[j]
                    message = replace_char_at_index(message, j, ' ')
            # squish word back together
            message = message.replace(" ", "")
            # move onto the next mod needed for the next middle row
            mod -= 2
        # This block of code accounts for the "valleys" of the fence
        # There is nothing left of the string to split so add it to the encrypted message
        else:
            encryptedMessage += message
    return encryptedMessage
def replace_char_at_index(org_str, index, replacement):
    ''' Replace character at index in string org_str with the
    given replacement character.'''
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str

def encryptDecryptMessage(choice, message, depth):
    output = ''
    if choice.upper() == 'E':
        output = encryptMessage(message, depth)
    if choice.upper() == 'D':
        output = decryptMessage(message, depth)
    return output

def isAlphabetic(string):
    for character in string:
        if not character.isalpha() and character != ' ':
            return False
    return True

def main():
    userChoice = input("Enter an E to encrypt a message, a D to decrypt a message, a H to hash a message, a C to crack an encrypted message, and Q to quit: ").upper()
    while userChoice != 'Q':
        if userChoice == 'E' or userChoice == 'D' or userChoice == 'H':
            key = input("Enter the Depth: ").upper().replace(" ", "")
            while (not key.isnumeric()):
                print("Invalid response!")
                key = input("Enter the Depth: ").upper().replace(" ", "")
            if userChoice == 'E':
                message = input("Enter the message to be encrypted: ").upper().replace(' ', '')
                while (not isAlphabetic(message)):
                    print("Invalid response!")
                    message = input("Enter the message to be encrypted: ").upper().replace(' ', '')
                output = encryptMessage(message, key)
            if userChoice == 'D':
                message = input("Enter the cypher text to decrypt: ").upper()
                while (not isAlphabetic(message)):
                    print("Invalid response!")
                    message = input("Enter the cypher text to decrypt: ").upper()
                output = decryptMessage(message, key)
            if userChoice == 'H':
                message = input("Enter the message to hash: ").upper()
                while (not isAlphabetic(message)):
                    print("Invalid response!")
                    message = input("Enter the message to hash: ").upper()
            print(output)
        else:
            print("Invalid response!")
        userChoice = input(
            "Enter an E to encrypt a message, a D to decrypt a message, a H to hash a message, a C to crack an encrypted message, and Q to quit: ").upper()

if __name__ == '__main__':
    main()