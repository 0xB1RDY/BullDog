# BullDog
BullDog is a tool that can encode and decode plaintext. It can only decode the text if the right decryption seed is given.<br />
Security Feature: You can encode the same message and the output will be different, because it all depends on the generated seed.

# How it works
It works because it goes off of a randomized set of numbers that are generated each time it is ran. Here is a simple process the program goes through:
<br />

Encryption Process:<br />
- Takes the given plaintext, and uses the randomized numbers to create a substituion cipher<br />
- Returns the result back to the user<br />

Decryption Process:<br />
- Takes the given cipher, then attempts to decrypt the cipher with the given seed.<br />
- If the seed is incorrect, it will return a junk cipher that doesnt mean anything.<br />
<br />

# How to use it
This is made in Python, so you must have the Python language installed.<br />
To use BullDog simply follow the instructions below:<br />
<br />
Install the needed package(s)
```
pip install -r requirements.txt<br />
```
Finally, run main.py
```
python main.py<br />
```
Based on your Python configuration, it may be Python3 or your latest version in the command.
