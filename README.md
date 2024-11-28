# RSA
In this project, I implemented RSA encryption and decryption without using the RSA Python module. As a second part of this project, I have implemented a signature function and conducted a verification of my partner's signature.  

## Part 1: RSA Implementation ##  
1) Parameter Selection (p,q,e generator.py)

generatePrimeNumber - is a function that generates a prime number with input parameters start and end, which are the boundaries within which the number should be generated. This function first generates a random number and then checks if this number is prime. If it is not we go back to regenerating the number and checking it again, until the prime number is found.  

As a result we generate p and q prime numbers between 32768, 65536. Then we calculate N = p*q and PhiN = (p-1)(q-1). Next we generate e that should be less than PhiN and e and PhiN should relative prime numbers. Finally we calculate corresponding private key d, which is a multiplicative inverse of e^(-1) and PhiN.  
p = 36791  
q = 62801  
N = 2310511591  
PhiN = 2310412000  
e = 2179905431  
d = 588194471  

2) Encryption (Encryption.py) - message: "No pain, no gain"

Function "Enc" encrypts my message and takes e, N and an array of integers, which represent our message divided in chunks as an input.  
The main program: we have e and N fixed prameters recieved from my partner.  
N=2563018343  
e=65537  
Then, we divide our message into n-byte chunks. Next, I convert ascii codes too hex values with function "ascii_to_hex". Following that, the hex values are converted into the interger values. Finally, the array of integer values can be given as an input to the "Enc" function to encrypt the message.   

![image](https://github.com/user-attachments/assets/3d27595d-dba3-4010-aac3-141fa81c4685)    

As a result we see an array of encrypted message.  

3) Decryption (decryption.py)

In this case function "Enc" is going to decrypt the message from my partner and it takes d, N and an array of integers, which represents encrypted message from my partner as an input.    

Encrypted Text=[235034025, 1562071064, 1544407760, 1379319713, 983092322, 1688256676]  
Above is an array that represents an encrypted message shared by my partner and we are going to decrypt it.  
First we execute "Enc" function and get an array of integers which represent a decrypted message. Then, we convert integer values into hex values. Following that, we convert the hex values into the ascii representations and join them together as the message was divided into chunks initially.  

![image](https://github.com/user-attachments/assets/1aeb6654-c80d-4316-ba13-be8cb0188f7c)  

As a result we recieve a message "nice to meet you".  

## Part 2: Signature/Verification ##  

(verification.py)  
This part of the project is about RSA signature implementation and verification of the partner's signature.  
First we will generate signature for my full name "Sofya Smolyakova". For this we will use the same public and secret keys from Part 1.  
d = 588194471  
N = 2310511591  

For signing we will use the same "Enc" function that we used for encryption and decryption in previous steps. We used the same series of steps with my full name to convert it into the array of intergers. Then we feed secret key d, public key N and array of itergers as an input to the "Enc" function to compute the signature.   

![image](https://github.com/user-attachments/assets/70525f7d-f941-4c68-8d05-2523eaf84676)  

On the picture above you can find the computed signature.   
In next part we verify the signature of my partner. For that I need the public keys e, N and the signed array that you can see below. We are going to verify it with name "Anyanwu Emmanuel".  
N=2563018343  
e=65537  
S =	[2224170182, 703257278, 1814534509, 1298439442, 1255914868, 1218030636]    
To verify the signature we used the same "Enc" function with public keys e, N of my partner and the signed text he shared as an input.  
Then we convert the verified intergers into the letters and compare the result with the original name. If these two are the same it means that verification was successfull.   

![image](https://github.com/user-attachments/assets/4b7ed1fa-c373-4d79-883f-54d0aa3996e9)  

As we can see the verification was successful!















