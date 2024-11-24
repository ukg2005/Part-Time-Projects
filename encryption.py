import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

#Encrypting a  message

plain_text = input("Enter message to encrypt:")
keyed_text = ""

for letter in plain_text:
    index = chars.index(letter)
    keyed_text += keys[index]

print(f"Encryped message:{keyed_text}")

#Decrypting a message

keyed_text = input("Enter message to dencrypt:")
plain_text = ""

for letter in keyed_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"Decrypted message:{plain_text}")