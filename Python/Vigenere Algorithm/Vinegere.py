# Vigenere Algorithm

# global variable
alpbh = ('A','B','C','D','E','F','G','H','I','J','K',
         'L','M','N','O','P','Q','R','S','T','U','V',
         'W','X','Y','Z') # <class 'tuple'> -> alphabeth
msgs = [] # <class 'list'>
keys = [] # <class 'list'>

A = "" # new message
chs = 0 # user choise
j = 0

# ----------
# menu
def menu():
    global chs
    print("1. Decode")
    print("2. Encode")
    print("3. Quit")
    
    while True:
        chs = int(input("Please enter your choise : "))
        if ((chs == 1)or(chs == 2)or(chs == 3)):
            break
        
# ----------
# encode (cipher)
def encode():
    global keys
    global msgs
    global A
    global j
    msg = input("Please enter your message : ") # <class 'str'>
    msg = msg.upper()
    key = input("Please enter your key message : ") # <class 'str'>
    key = key.upper()
    temp=0
    msgs=[]  
    for i in msg:
        if i != " ":
            temp = alpbh.index(i)
            msgs.append(temp)
    
    temp=0
    keys=[]
    for i in key:
        if i != " ":
            temp = alpbh.index(i)
            keys.append(temp)
        
    A=""
    j=0
    for i in msgs:
        temp = 0
        if((i+keys[j])>25):
            temp = (i+keys[j])%26
            A += alpbh[temp] 
        
        else:
            A += alpbh[(i+keys[j])]
            
        j += 1
        if(j == len(key)):
            j=0
        
    print("Result :",A)

# ----------
# decode (decipher)    
def decode():
    global keys
    global msgs
    global A
    global j
    msg = input("Please enter your message : ") # <class 'str'>
    msg = msg.upper()
    key = input("Please enter your key message : ") # <class 'str'>
    key = key.upper()        
    temp =0 
    msgs=[]  
    for i in msg:
        if i != " ": 
            temp = alpbh.index(i)
            msgs.append(temp)
    
    temp=0
    keys=[]
    for i in key:
        if i != " ":
            temp = alpbh.index(i)
            keys.append(temp)
        
    A=""
    j=0
    for i in msgs:
        temp = 0
        if ((i-keys[j]) < 0):
            temp =26+(i-keys[j])
            A += alpbh[temp]
        else:
            A += alpbh[i-(keys[j])]

        j += 1
        if(j == len(key)):
            j = 0
        
    print(A)

# main
while True:
    menu()
    if chs == 1: # decipher
        decode()
    elif chs == 2: # cipher 
        encode()
    elif chs == 3: # quit
        break