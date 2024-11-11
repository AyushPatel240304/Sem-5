import random
import string

# Function to generate a random key for each message
def generate_random_key(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# Function to encrypt message using a random key
def encrypt_message(message, key):
    encrypted_message = ""
    key_index = 0  # Separate index for key to handle spaces in message
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += encrypted_char
            key_index += 1  # Only move to next key character if message character is a letter
        else:
            encrypted_message += char
    return encrypted_message

# Function to decrypt message using the same key
def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    key_index = 0  # Separate index for key to handle spaces in message
    for char in encrypted_message:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_message += decrypted_char
            key_index += 1  # Only move to next key character if message character is a letter
        else:
            decrypted_message += char
    return decrypted_message

# Example usage for 3 messages
messages = ["Hello Bob", "Send Backup", "Meet at Noon"]
# Sending 3 messages
for i, message in enumerate(messages):
    key = generate_random_key(len(message.replace(" ", "")))  # Generate random key ignoring spaces
    encrypted_message = encrypt_message(message, key)  # Encrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)  # Decrypt the message

    print(f"Message {i+1}: {message}")
    print(f"Generated Key: {key}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}\n")
