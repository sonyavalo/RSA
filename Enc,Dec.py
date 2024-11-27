
import random
import math
import binascii
"""

flag = True
while flag == True:
    p = random.randint(32768, 65536)                                #chose random 16 bit prime number
    q = random.randint(32768, 65536)                                #chose random 16 bit prime number
    if p > 1 and q > 1:
        for i in range(2, p):
            if (p % i) == 0:
                #print (p,"is not a prime number")
                break
        else:
            for i in range(2, q):
                if (q % i) == 0:
                    # print (q,"is not a prime number")
                    break
            else:
                print("prime number p:", p)
                print("prime number q:", q)
                flag = False

N = p*q # N calculation
print("N:",N)
PhiN = (p-1)*(q-1)                                               # PhiN calculation
print("PhiN:",PhiN)
flag=True
while flag == True:
    e = random.randrange(1, PhiN)                                # chose random e less than PhiN and e and PhiN should be relative prime numbers
    GCD = math.gcd(e, PhiN)
    if GCD == 1:
        print ("we chose e:", e)
        flag=False

d=pow(e,-1,PhiN)                                                  # corresponding private key d calculation using multiplicative inverse d=e^(-1) mod PhiN
print("d:",d)

check=(e*d)%PhiN                                                  # checking if gcd (e,d)=1
print("check:", check)
"""
p = 36791
q = 62801
N = 2310511591
PhiN = 2310412000
e = 2179905431
d = 588194471



def ascii_to_hex(ascii_str):                                      # function of coverting ascii to hex value
    hex_str = binascii.hexlify(ascii_str.encode())
    return hex_str

Text = 'No pain, no gain'                                         # the message that we want to encrypt or decrypt
n = 3                                                             # The size of Chunk
Chank=[Text[i:i+n] for i in range(0, len(Text), n)]               # Creating array with n-byte chunks
print (Chank)

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

CyphertextEnc = Enc(e,N,Cyphertext)                                 #encrypting message
print (CyphertextEnc, 'encrypted')

Message = Enc(d,N,CyphertextEnc)                                    #decryting message
print (Message, 'decrypted')

HexHex=[]
for i in range (0,len(Message)):                                    #converting integer to hex
    H=hex(Message[i])
    HexHex.append(H[2:])
print(HexHex)

plainText = []
for i in range (0,len(HexHex)):                                     #converting hex to ascii
    y=bytes.fromhex(HexHex[i])
    plainText.append(y.decode("ascii"))
    Message="".join(plainText)

print ('message = ', Message)

