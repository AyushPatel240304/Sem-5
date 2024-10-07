# Hill cipher
import numpy as np
def adjoint(matrix):
    matrix[0,0],matrix[1,1]=matrix[1,1],matrix[0,0]
    matrix[0,1]*= -1
    matrix[1,0]*= -1
    return matrix

pt = input("Enter the message to encrypt : ")
key = input("Enter the key :" )

if len(pt)%2!=0: 
    pt+='x'

    