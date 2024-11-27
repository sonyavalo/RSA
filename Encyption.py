
import random
import math
import binascii


def Enc (x,y,array):                                               #encryption/decryption function which is using square and multiply
    Encryption = []
    for i in range (0,len(array)):
        exp=bin(x)
        value=array[i]
        for j in range (3,len(exp)):
            value=(value*value)%y
            if(exp[j:j+1]=='1'):
                value=(value*array[i])%y
        Encryption.append(value)
    return Encryption

N=2563018343
e=65537

Text = 'No pain, no gain'                                         # the message that we want to encrypt or decrypt
n = 3                                                             # The size of Chunk
Chank=[Text[i:i+n] for i in range(0, len(Text), n)]               # Creating array with n-byte chunks
print (Chank)

def ascii_to_hex(ascii_str):                                      # function of coverting ascii to hex value
    hex_str = binascii.hexlify(ascii_str.encode())
    return hex_str

Hex=[]
for i in range (0,len(Chank)):                                    #Converting ascii to hex
    ascii_input=Chank[i]
    hex_output = ascii_to_hex(ascii_input)
    Hex.append(hex_output.decode('utf8'))
print(Hex)

Cyphertext=[]
for i in range (0,len(Hex)):                                      #Converting hex to integer
    int_value=int(Hex[i],16)
    Cyphertext.append(int_value)
print(Cyphertext)

CyphertextEnc = Enc(e,N,Cyphertext)                                 #encrypting message
print (CyphertextEnc, 'encrypted')
