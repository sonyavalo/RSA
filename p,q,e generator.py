
import random
import math
import binascii


def generatePrimeNumber (start,end):
    while True:
        x=random.randint(start,end) #chose random 16 bit prime number
        prime = True
        for i in range(2, x):
            if (x % i) == 0:
                prime = False
                break
        if (prime):
            return x

p = generatePrimeNumber(32768,65536)
print ("prime number p:", p)

q = generatePrimeNumber(32768,65536)
print ("prime number q:", q)

N = p*q # N calculation
print("N:",N)
PhiN = (p-1)*(q-1) # PhiN calculation
print("PhiN:",PhiN)

while True:
    e = random.randrange(1, PhiN) # chose random e less than PhiN and e and PhiN should be relative prime numbers
    GCD = math.gcd(e, PhiN)
    if GCD == 1:
        print ("e:", e)
        break

d=pow(e,-1,PhiN) # corresponding private key d calculation using multiplicative inverse d=e^(-1) mod PhiN
print("d:",d)

check=(e*d)%PhiN
print("check:", check)



"""
prime number p: 36791
prime number q: 62801
N: 2310511591
PhiN: 2310412000
e: 2179905431
d: 588194471
check: 1
"""






