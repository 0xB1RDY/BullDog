### IMPORT NEEDED PACKAGE(S) ###
from src.code import *
import random

### MAIN CODE ###
def main():
    while True:
        try:
            selection = int(input("[1] Encode [2] Decode : ")) # Get the user input
            if selection == 1:
                message = input("[*] Enter Message to Encode : ") # Get the message to encode
                decryption_seed = random.randint(111111111111111, 999999999999999) # Generating the randomized decryption seed
                print("[+] Decryption Seed : " + str(decryption_seed)) # Print out the decryption seed
                try:
                    print(str(encode(message, decryption_seed))) # Print out the result
                except Exception as e:
                    print("[-] Failed to encode message, Error: " + (str(e))) # If the encryption process fails

            elif selection == 2:
                encrypted_message = input("[*] Enter Message to Decode : ") # Get the message to decode
                encrypted_seed = int(input("[*] Enter Decryption Seed : ")) # Get the decryption seed
                try:
                    print(decode(encrypted_message, encrypted_seed)) # Print out the result
                except Exception as e:
                    print("[-] Failed to decode message, Error: " + str(e)) # If the decryption process fails
        except Exception as e:
            print("[-] Error validating input, Error: " + str(e))

if __name__ == "__main__":
    main()