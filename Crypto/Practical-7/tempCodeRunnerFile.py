import random

# Function to compute gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm to find the modular inverse
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Function to find modular inverse of e mod phi(n)
def mod_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate large random prime numbers
def generate_large_prime(keysize):
    while True:
        num = random.randrange(2**(keysize-1), 2**keysize)
        if is_prime(num):
            return num

# Function to generate public and private keys
def generate_keypair(keysize):
    print("Generating keypair...")
    p = generate_large_prime(keysize)
    q = generate_large_prime(keysize)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    # Compute d such that e * d ≡ 1 (mod phi)
    d = mod_inverse(e, phi)
    
    # Public key is (e, n), private key is (d, n)
    print(f"Generated keys with p={p}, q={q}, n={n}, phi={phi}, e={e}, d={d}")
    return (e, n), (d, n)

# Encryption function
def encrypt(public_key, plaintext):
    e, n = public_key
    # Convert plaintext to integer
    plaintext_int = int.from_bytes(plaintext.encode(), 'big')
    print(f"Encrypting plaintext '{plaintext}' to integer: {plaintext_int}")
    # Encrypt using c = m^e mod n
    ciphertext = pow(plaintext_int, e, n)
    print(f"Encrypted integer (ciphertext): {ciphertext}")
    return ciphertext

# Decryption function
def decrypt(private_key, ciphertext):
    d, n = private_key
    print(f"Decrypting ciphertext: {ciphertext}")
    # Decrypt using m = c^d mod n
    plaintext_int = pow(ciphertext, d, n)
    
    try:
        # Convert the integer back to plaintext
        plaintext = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'big').decode()
        print(f"Decrypted integer back to plaintext: {plaintext}")
        return plaintext
    except UnicodeDecodeError:
        # If decoding fails, return raw bytes for inspection
        return plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'big')

# Example usage
keysize = 256  # You can increase this value for stronger keys (e.g., 1024 or 2048)

# Generate public and private keys
public_key, private_key = generate_keypair(keysize)

# Display the generated keys
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Example plaintext
plaintext = "Hello, RSA!"

# Encrypt the plaintext using the public key
ciphertext = encrypt(public_key, plaintext)
print(f"Encrypted message: {ciphertext}")

# Decrypt the ciphertext using the private key
decrypted_message = decrypt(private_key, ciphertext)
print(f"Decrypted message: {decrypted_message}")
