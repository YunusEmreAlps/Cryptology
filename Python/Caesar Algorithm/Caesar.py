# Caesar Algorithm

# global variable
A = "" # new message
chs = 0 # user choise variable
key = 0 # key -> (positive number)

# ----------
# menu
def menu():
    global chs 
    print("1. Decode")
    print("2. Encode")
    print("3. Quit")
    
    while True:
        chs = int(input("Please enter your choise ? : ")) # <class 'int'>
        if ((chs == 1)or(chs == 2)or(chs == 3)):
            break;

# ----------
# decode (decipher)
def decode():
    global A
    global key
    msg = input("Please enter your message : ") # <class 'str'>
    msg = msg.upper() # MESSAGE
    while True:
        key = int(input("Please enter your key : "))
        if key > 0:
            break
        
    A = ""
    for i in msg: # decipher
        temp = 0
        if ord(i)>64 and ord(i) < (65+key):
            temp = (ord(i)-(key))
            temp = 64-temp
            temp = 90 - temp
            A += chr(temp)
        elif ord(i) < 65:
            A += " "
        else:
            A += chr(ord(i)-key)
    print("Result :",A) # Result : YUNUS

# ----------
# encode (cipher)
def encode():
    global A
    global key
    msg = input("Please enter your message : ") # <class 'str'>
    msg = msg.upper() # MESSAGE
    while True:
        key = int(input("Please enter your key : "))
        if key > 0:
            break
    A = ""
    for i in msg: # cipher
        temp = 0
        if ord(i) > (90-key):
            temp = (ord(i)+(key))%90
            temp = temp + 64
            A += chr(temp)
        elif ord(i) < 65:
            A += " " 
        else:
            A += chr(ord(i)+key)
    print("Result :",A) # Result : DZSZX


# main function
while True:
    menu()
    if(chs == 1): # decipher
        decode()
    elif(chs == 2): # cipher
        encode()
    elif(chs == 3): # quit
        break
    
    
    
    
    
    
    
    