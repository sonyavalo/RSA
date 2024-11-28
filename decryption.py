
import random
import math
import binascii



def Enc (x,y,array):                    #encryption/decryption function which is using square and multiply
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

CyphertextEnc=[235034025, 1562071064, 1544407760, 1379319713, 983092322, 1688256676]

N = 2310511591
print ('N=',N)
e = 2179905431
print ('e=', e)
d = 588194471
print ('d=', d)

Message = Enc(d,N,CyphertextEnc)            #decryption of cyphertext
print ('decrypted',Message)

HexHex=[]
for i in range (0,len(Message)):
    H=hex(Message[i])
    HexHex.append(H[2:])
print( 'hex values', HexHex)

plaintxt = []
for i in range (0,len(HexHex)):
    y=bytes.fromhex(HexHex[i])
    plaintxt.append(y.decode("ascii"))
    mmm=y.decode("ascii")
    print(mmm)
    Message="".join(plaintxt)

print ('message = ', Message)


