#####################  Ceaser Cypher ####################

# def caesar_cipher(text, shift, mode='encrypt'): 
#     if mode == 'decrypt': 
#         shift = -shift  # Reverse the shift for decryption 
 
#     processed_text = "" 
#     for char in text: 
#         if char.isalpha(): 
#             shift_amount = shift % 26 
#             if char.islower(): 
#                 start = ord('a') 
#                 processed_char = chr(start + (ord(char) - start + 
# shift_amount) % 26) 
#             else: 
#                 start = ord('A') 
#                 processed_char = chr(start + (ord(char) - start + 
# shift_amount) % 26) 
#             processed_text += processed_char 
#         else: 
#             processed_text += char 
 
#     return processed_text 
 
# # User input 
# text = input("Enter the text: ") 
# shift = int(input("Enter the shift value: ")) 
# mode = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ") 
 
# # Process 
# result = caesar_cipher(text, shift, mode) 
# print(f"Result: {result}") 


################### MONO-APLHABATIC ########################

# def generate_fixed_mono_alphabetic_key(): 
#     # Define a fixed key mapping for the alphabet 
#     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
#     shuffled_alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'  # Example of a fixed key 
#     return dict(zip(alphabet, shuffled_alphabet)) 
 
# def mono_alphabetic_cipher(text, key, mode='encrypt'): 
#     if mode == 'decrypt': 
#         key = {v: k for k, v in key.items()}  # Invert the key for decryption 
     
#     processed_text = "" 
#     for char in text: 
#         if char.isalpha(): 
#             if char.islower(): 
#                 processed_text += key[char.upper()].lower() 
#             else: 
#                 processed_text += key[char] 
#         else: 
#             processed_text += char 
#     return processed_text 
 
# # Use a fixed key instead of randomizing 
# key = generate_fixed_mono_alphabetic_key() 
# print("Mono-alphabetic Cipher Algorithm") 
# # Ask user whether to encrypt or decrypt 
# operation = input("Do you want to (1) Encrypt or (2) Decrypt? Enter 1 or 2: ") 
 
# if operation == '1': 
#     # User input for encryption 
#     plaintext = input("Enter the text to encrypt: ") 
#     ciphertext = mono_alphabetic_cipher(plaintext, key, mode='encrypt') 
#     print(f"Key: {key}") 
#     print(f"Encrypted Text: {ciphertext}") 
 
# elif operation == '2': 
#     # User input for decryption 
#     ciphertext = input("Enter the text to decrypt: ") 
#     decrypted_text = mono_alphabetic_cipher(ciphertext, key, mode='decrypt') 
#     print(f"Decrypted Text: {decrypted_text}") 
# else: 
#     print("Invalid option selected.")



############   PLAYFAIR CIPHER  ###############

# import numpy as np
# def arrayGenerate(kw):
#     array = np.empty((5, 5), dtype='str')
#     alpha = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

#     used_letters = set()
#     row, col = 0, 0
    
  
#     for letter in kw:
#         if letter not in used_letters:
#             array[row, col] = letter
#             used_letters.add(letter)
#             col += 1
            
#             if col == 5:
#                 col = 0
#                 row += 1
#                 if row == 5: 
#                     break
            
#     for letter in alpha:
#         if letter not in used_letters and letter != 'J':
#             array[row, col] = letter
#             used_letters.add(letter)
#             col += 1
            
#             if col == 5:
#                 col = 0
#                 row += 1
#                 if row == 5:  
#                     break
                
#     return array
    
# def print_matrix(matrix):
#         for row in matrix:
#             print(" ".join(row))
        
# def find_letter(matrix, letter):
#         for row in range(5):
#             for col in range(5):
#                 if matrix[row, col] == letter:
#                     return row, col
#         return None, None
    
# def playfair_encrypt(plain_text, matrix):
#         encrypted_text = ""
#         plain_text = plain_text.upper().replace("J", "I").replace(" ", "")
        
#         for i in range(0, len(plain_text), 2):
#             letter1 = plain_text[i]
#             letter2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'
            
#             row1, col1 = find_letter(matrix, letter1)
#             row2, col2 = find_letter(matrix, letter2)
        
#             if row1 == row2:
#                 encrypted_text += matrix[row1, (col1 + 1) % 5] + matrix[row2, (col2 + 1) % 5]
#             elif col1 == col2:
#                 encrypted_text += matrix[(row1 + 1) % 5, col1] + matrix[(row2 + 1) % 5, col2]
#             else:
#                 encrypted_text += matrix[row1, col2] + matrix[row2, col1]
                
#         return encrypted_text
        
# def main():
#     keyword = input("Enter keyword: ").upper()
#     matrix = arrayGenerate(keyword)
    
#     print("Generated Playfair Matrix:")
#     print_matrix(matrix)
    
#     plain_text = input("Enter plain text : ")
#     encrypted_text = playfair_encrypt(plain_text, matrix)
    
#     print("Encrypted text:", encrypted_text)
    
# main()
        
################# HILL CIPHER ###############

import numpy as np
def adjoint(matrix):
    matrix[0,0],matrix[1,1]=matrix[1,1],matrix[0,0]
    matrix[0,1]*=-1
    matrix[1,0]*=-1
    return matrix
    
pt=input("Please enter the plain text : ")
key=input("Please enter the key : ")

if len(pt)%2 != 0:
    pt+='x'
    
tempKeyMatrix=np.zeros((2,2), dtype=np.str_)
k=0
for i in range(2):
    for j in range(2):
        tempKeyMatrix[i,j]=key[k]
        k+=1
keyMatrix=np.matrix(tempKeyMatrix)

print('Char key matrix\n',tempKeyMatrix)

keyMatrix=np.zeros((2,2),dtype=np.int64)

for i in range(2):
    for j in range(2):
        keyMatrix[i,j]=ord(tempKeyMatrix[i,j])-96
        
print('Integer key matrix\n',keyMatrix)

ptList=[pt[i:i+2] for i in range(0,len(pt),2)]
ctList=[]
print()
print('Cipher')
print(ptList)
for i in ptList:
    # print('For',i)
    t=np.zeros((2,1),dtype=np.int64)
    t[0,0]=ord(i[0])-96
    t[1,0]=ord(i[1])-96
    cipher=np.dot(keyMatrix,t)%26
    # print(cipher)
    ctList+=[chr(cipher[0,0]+96)+chr(cipher[1,0]+96)]
    del t
    
del ptList
print(ctList)
print()

print('Decipher')
mod=(keyMatrix[0,0]*keyMatrix[1,1])-(keyMatrix[1,0]*keyMatrix[0,1])
print('Determinant of key matrix',mod)

mod%=26
print('Modulus By 26 of Determinant of key matrix',mod)
kInverse=1

while (mod*kInverse)%26!=1:
    kInverse+=1
print()
print('kInverse',kInverse)
print('Adjoint of Key Matrix\n', adjoint(keyMatrix.copy()))

kInverseMatrix=((adjoint(keyMatrix.copy())%26)*kInverse)%26
print()
print('kInverseMatrix\n',kInverseMatrix)

print()
print(ctList)
ptList=[]

for i in ctList:
    # print('For',i)
    t=np.zeros((2,1),dtype=np.int64)
    t[0,0]=ord(i[0])-96
    t[1,0]=ord(i[1])-96
    decipher=np.dot(kInverseMatrix,t)%26
    # print(cipher)
    ptList+=[chr(decipher[0,0]+96)+chr(decipher[1,0]+96)]
    del t
    
print(ptList)