# Function for Vigenère Cipher Encryption
def vigenere_encrypt(plain_text, key):
    key = key.upper()
    encrypted_text = []
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            encrypted_char = chr((ord(plain_text[i].upper()) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(plain_text[i])
    return ''.join(encrypted_text)

# Function for Vigenère Cipher Decryption
def vigenere_decrypt(encrypted_text, key):
    key = key.upper()
    decrypted_text = []
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            decrypted_char = chr((ord(encrypted_text[i]) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(encrypted_text[i])
    return ''.join(decrypted_text)

# Example usage with a specific key for Vigenère Cipher
vigenere_key = "SECRET"
message = "Palladium Mall"

encrypted_vigenere_message = vigenere_encrypt(message, vigenere_key)
decrypted_vigenere_message = vigenere_decrypt(encrypted_vigenere_message, vigenere_key)

print("Original Message:", message)
print("Vigenere Encrypted Message:", encrypted_vigenere_message)
print("Vigenere Decrypted Message:", decrypted_vigenere_message)
