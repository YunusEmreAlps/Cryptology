# Caesar Algorithm 

alpbh = ('A','B','C','D','E','F','G','H','I','J','K',
         'L','M','N','O','P','Q','R','S','T','U','V',
         'W','X','Y','Z') # <class 'tuple'> -> alphabeth

A = "" # new message
chs = 0 # user choise
key = 0 # shift

# ----------
# menu function
def menu():
    global chs
    print("1. Decode")
    print("2. Encode")
    print("3. Quit")
    
    while True: # infinty loop
        chs = int(input("Please enter your choise : "))
        if ((chs == 1)or(chs == 2)or(chs == 3)):
            break

# ----------
# decode (decipher)
def decode():
    global A
    global key
    global alpbh
    msg = input("Please enter your message : ") # <class 'str'>
    msg = msg.upper() # all letter is upper case
    key = int(input("Please enter your key number : ")) # <class 'int'>
    
    # index 0-25
    A = ""
    for i in msg:
        if i in alpbh:
            temp = alpbh.index(i)
            temp = temp-key
            if temp < 0:
                temp = 26+temp
                A += alpbh[temp]
            else:    
                A += alpbh[temp]
        else:
            A += ' '
    print(A)


# ----------
# encode (cipher)
def encode():
    global A
    global key
    global alpbh
    msg = input("Please enter your message : ") # <class 'str'>
    msg = msg.upper() # all letter is upper case
    key = int(input("Please enter your key number : ")) # <class 'int'>
    
    # index 0-25
    A = ""
    for i in msg:
        if i in alpbh:
            temp = alpbh.index(i)
            temp = temp+key
            if temp > 25: 
                temp = temp%26
                A += alpbh[temp]
            else:    
                A += alpbh[temp]
        else:
            A += ' '
    print(A)
    
# main function
while True:
    menu()
    if chs == 1:
            decode()
    elif chs == 2:
        encode()
    elif chs == 3:
        break


