import binascii

"""
prime number p: 36791
prime number q: 62801
N: 2310511591
PhiN: 2310412000
e: 2179905431
d: 588194471
check: 1
"""
#we will use the same p,q,N,Phin,e and d as for enryption/decryption parts of RSA
e = 2179905431  # veryfication exponent
d = 588194471   # signing exponent
N = 2310511591  # mod

def Enc (x,y,array):                                #encryption/decryption function which is using square and multiply
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

message = "Sofya Smolyakova"
n = 3                                                           # The size of Chunk
Chank=[message[i:i+n] for i in range(0, len(message), n)]       # Creating array with n-byte chunks
print (Chank)

def ascii_to_hex(ascii_str):                                    # function of coverting ascii to hex value
    hex_str = binascii.hexlify(ascii_str.encode())
    return hex_str

Hex=[]
for i in range (0,len(Chank)):                                  #Converting ascii to hex
    ascii_input=Chank[i]
    hex_output = ascii_to_hex(ascii_input)
    Hex.append(hex_output.decode('utf8'))
print(Hex)

text=[]
for i in range (0,len(Hex)):                                      #Converting hex to integer
    int_value=int(Hex[i],16)
    text.append(int_value)
print(text)

Signature = Enc(d,N,text)                                   #signing message
print (Signature, '= signature')


# another verification
N=2563018343
e=65537
S =	[2224170182, 703257278, 1814534509, 1298439442, 1255914868, 1218030636]
nameOrig = "Anyanwu Emmanuel"

verf2 = Enc(e,N,S)
print (verf2, 'verification')

HexHex=[]
for i in range (0,len(verf2)):
    H=hex(verf2[i])
    HexHex.append(H[2:])
print( 'hex values', HexHex)

plaintxt = []
for i in range (0,len(HexHex)):
    y=bytes.fromhex(HexHex[i])
    plaintxt.append(y.decode("ascii"))
    name1="".join(plaintxt)
print ('name1 = ', name1)

if nameOrig == name1:
    print ("Veryfication is successfull!")
else:
    print ("Something went wrong!")
