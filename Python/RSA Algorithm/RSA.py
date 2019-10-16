# RSA Algorithm

p = int(input(" - P : "))
q = int(input(" - Q : "))

# ----------
i = 2
prime_p = False

while True: # prime number control
    if(p%i == 0):
        prime_p = False
        break
    
    if((p-1) == i):
        prime_p = True
        break
    
    i+=1
    
if(p==2):
    prime_p = True 
    
    
# ----------
i = 2
prime_q = False

while True: # prime number control
    if(q%i == 0):
        prime_q = False
        break
    
    if((q-1) == i):
        prime_q = True
        break
    i+=1

if(q==2):
    prime_q = True
    

# ----------
if prime_p==True and prime_q==True:
    
    n=p*q
    tot=(p-1)*(q-1) # totient
    
    # e (public key)
    i=2

    while True:
        if(tot%i == 0):
            prime_e = False
        
        elif(tot%i != 0):
            e=i
            break
        i+=1
        
    # d (private key)
    i=1
    while True:
        if((e*i)%tot == 1):
            break
        i+=1
        
    d=i # private key
    
    # ascii number
    msg = input(" - Message (number): ")
    e_msg = ""
    for i in msg:
        number = 0
        number = ord(i)
        c = (number**e)%n
        e_msg+=chr(c)
        
    # Encrypt
    print(f" - Encrypt : {e_msg}")
    d_msg=""
    # Decrypt
    for i in e_msg:
        number=0
        number=ord(i)
        m = (number**d)%n
        d_msg+=chr(m)
        
    print(f" - Decrypt : {d_msg}")
    
    









