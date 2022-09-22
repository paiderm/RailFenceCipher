import math

def replace_char_at_index(org_str, index, replacement):
    ''' Replace character at index in string org_str with the
    given replacement character.'''
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str

def encryptDecryptMessage(choice, message, key):
    if choice.upper() == 'E':
        # twoDArray = []
        # encryptedMessage = ''
        #
        # for i in range(int(key)):
        #     twoDArray.append([])
        #
        # for i in range(int(key)):
        #     for j in range(len(message)):
        #         twoDArray[i].insert(j, -1)
        #
        # firstCountBy = determineFirstCountBy(key)
        # countBy = firstCountBy
        #
        # for i in range(int(key)):
        #     if countBy != 0:
        #         for j in range(0, math.floor(len(message) / int(countBy))):
        #             encryptedMessage += message[j*countBy]
        #             #message[j*countBy] = " "
        #             message = replace_char_at_index(message, j*countBy, ' ')
        #             if countBy != firstCountBy and j*countBy + 1 < len(message) and j != 0:
        #                 encryptedMessage += message[j * countBy + 1]
        #                 #message[j*countBy] = " "
        #                 message = replace_char_at_index(message, j * countBy + 1, ' ')
        #         message = message.replace(" ", "")
        #         countBy -= 2
        #     else:
        #         encryptedMessage += message
        encryptedMessage = ''
        firstCountBy = determineFirstCountBy(key)
        countBy = firstCountBy

        for i in range(int(key)):
            if countBy == firstCountBy:
                for j in range(0, len(message)):
                    if j % countBy == 0:
                        encryptedMessage += message[j]
                        message = replace_char_at_index(message, j, ' ')
                message = message.replace(" ", "")
                countBy -= 1
            elif countBy != 1:
                for j in range(0, len(message)):
                    if j % countBy == 0:
                        encryptedMessage += message[j]
                        message = replace_char_at_index(message, j, ' ')
                    if countBy != firstCountBy and j != 1 and j % countBy == countBy - 1:
                        encryptedMessage += message[j]
                        message = replace_char_at_index(message, j, ' ')
                message = message.replace(" ", "")
                countBy -= 2
            else:
                encryptedMessage += message



        # print(twoDArray)
        return encryptedMessage
def determineFirstCountBy(depth):
    return 2*(int(depth) - 1)

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
            if userChoice == 'D':
                message = input("Enter the cypher text to decrypt: ").upper()
                while (not isAlphabetic(message)):
                    print("Invalid response!")
                    message = input("Enter the cypher text to decrypt: ").upper()
            if userChoice == 'H':
                message = input("Enter the message to hash: ").upper()
                while (not isAlphabetic(message)):
                    print("Invalid response!")
                    message = input("Enter the message to hash: ").upper()
            print(encryptDecryptMessage(userChoice, message, key))
        elif userChoice == 'C':
            message = input("Enter the message to be cracked: ").upper()
            while (not isAlphabetic(message)):
                print("Invalid response!")
                message = input("Enter the message to be cracked: ").upper()
            # figure out the key length
                # make staggered 2D array

        else:
            print("Invalid response!")
        userChoice = input(
            "Enter an E to encrypt a message, a D to decrypt a message, a H to hash a message, a C to crack an encrypted message, and Q to quit: ").upper()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
