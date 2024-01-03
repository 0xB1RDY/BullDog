### IMPORT NEEDED PACKAGE(S) ###
import random

### VARIABLES ###
characters_in_order = [chr(x) for x in range(32, 127)]

### ENCODE FUNCTION ###
def encode(message: str, r_seed: int, result=""): # Encode function, take the plaintext, take the seed, and create a result
    random.seed(r_seed) # Use the randomized decryption seed
    shuffled_list = [chr(x) for x in range(32, 127)]
    random.shuffle(shuffled_list)
    for i in range(0, len(message)):
        result += shuffled_list[characters_in_order.index(message[i])] # Create the Cipher

    return result
    result = ''

### DECODE FUNCTION ###
def decode(message: str, r_seed: int, result=""):
    random.seed(r_seed) # Take the given seed for decryption use
    shuffled_list = [chr(x) for x in range(32, 127)]
    random.shuffle(shuffled_list)
    for i in range(0, len(message)):
        result += characters_in_order[shuffled_list.index(message[i])] # Decode the given Cipher

    return result
    result = ''