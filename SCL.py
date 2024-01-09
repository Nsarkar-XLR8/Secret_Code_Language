'''

                      Write a Python program to translate a message into
                	            \"SECRET CODE LANGUAGE\"

'''

# Importing Necessary modules
import random
import string







psudeo = list(string.ascii_lowercase)       # Listing Random Char For Encoding Part
psudeo1 = random.choice(psudeo)     # Choosing Random Char For Encoding Part


# Encoding Part
def encrypt(message):
    if len(message) >= 3:
        message1 = message[0:1]     # Storing First Char
        message2 = message[1:len(message)]      # Storing Second to Last Char
        message3 = message2 + message1      # Then Adding Them

        secret = psudeo1 + message3 + psudeo1   # In Starting & Ending, Appending Random Char
        print("After Encoding:", secret)     # Printing The Encoded Message
        return secret


    else:
        print("After Encoding:", message[::-1])
        return message[::-1]    # Returning The Encoded Message



# Decoding Part
def decrypt(secret):
    if len(secret) < 3:
        print("After Decoding:", secret[::-1])
        return secret[::-1]     # Returning The Decoded Message
    else:
        secret1 = secret[1:len(secret) - 1]     # Storing The (Removing Encrypted Message First & Last Character0
        secret2 = secret1[:len(secret1) - 1]     # Storing The Last Removing Character
        secret3 = secret1[len(secret1) - 1:len(secret1)]
        secret4 = secret3 + secret2     # Appending The Decoded String

        print("After Decoding:", secret4)
        return secret4      # Returing The Decoded Message


def main():
    choice = input("Do you want to encode or decode? Enter 'encode' or 'decode': ").lower()
    if choice == 'encode':
        message = input("Enter the message to encode: ")
        encrypted = encrypt(message)
        return encrypted
    elif choice == 'decode':
        secret = input("Enter the message to decode: ")
        decrypted = decrypt(secret)
        return decrypted
    else:
        print("Invalid choice. Please enter 'encode' or 'decode'.")
        return None

# Run the program
result = main()
if result is not None:
    decrypt(result)
