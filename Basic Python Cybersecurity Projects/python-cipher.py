import string

# Function to encrypt a message using Caesar cipher
# (Encrypt the message)
def caesar_cipher(message, key):

    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    encrypted_message = message.lower().translate(cipher)

    return encrypted_message


# Function to decrypt a message using Caesar cipher
# (Decrypt the message)
def caesar_decipher(encrypted_message, key):

    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    message = encrypted_message.translate(cipher)
    return message


# Usage of the functions
message = "Hello, World!"
key = 3

encrypted_message = caesar_cipher(message, key)
print("Encrypted Message:", encrypted_message)

decrypted_message = caesar_decipher(encrypted_message, -key)
print("Decrypted Message:", decrypted_message)