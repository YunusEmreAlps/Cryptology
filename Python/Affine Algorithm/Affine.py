# Affine Algorithm

alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U','V','W','X','Y','Z')
            # <class 'tuple'>
            
keys = [] 
# ----------
N = '' # new message

A,B = 0,0
res = 0 
pro = 0 # process number

def menu():
    global pro
    print("----------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")
    print("----------")
    while True: # infinity loop
        pro = int(input("Please enter your process number : "))
        if pro>0 and pro<4:
            break
# ----------   
# key control
def keycont():
        global A
        global B
        # gcd(A,26) = 1
        while True: # infinity loop
            A = int(input("Please enter your A number : "))    
            if (A%2 != 0 and A != 13) and (A > 0 and A < 26):
                break
        # 0 <= B <= 25
        while True: # infinity loop
            B = int(input("Please enter your B number : "))    
            if A > 0 and A < 26:
                break

# ----------
def inverse(): # inverse mod
    global A
    global res
    k=2
    modi=26
    numi = A
    cont = False
    
    # ----------
    while True: # coprime control
        if ((numi%k == 0)and(modi%k == 0)): # no coprime
            cont = False
            break
        elif k > modi: # coprime 
            cont = True
            break
        k+=1
    
    # ----------
    if ((modi > numi)and (cont == True)):
        lpc = int(modi/numi) # loop counter
        nc,mdc = 1,0
        a = 1
    
        while True: # infinity loop
            if(((modi*mdc)-(numi*nc)) == 1): # status positive
                break
            if(nc > lpc): 
                mdc += 1
                lpc += int(modi/numi)
            nc += 1

        if(modi - nc) < 0 :
            while True:
                res = modi*a - nc
                if res > 0:
                    break
                else:
                    a +=1

        else:
            res = modi - nc
    # ----------
    else:
        if cont == False:
            print("There is no modular multiplicative inverse for this integer")
    
        elif (numi > modi):    
            print(f"Error: {numi} > {modi} ")
    

# ----------
# cipher
def encrypt():
    global A
    global B
    global N
    global keys
    print("----------")
    keycont()
    msg = input("Please enter your msg : ")
    msg = msg.upper() # MESSAGE
    
    keys  = []
    for i in msg:
        if i != ' ':
            keys.append(alphabet.index(i))    
    N = ''
    for i in range(0,len(keys)):
        temp = (A*keys[i]+B)%26
        N += alphabet[temp]
    
    print("Result:",N)
    
# ----------
# decipher
def decrypt():
   global res
   global A
   global B
   global N
   global keys
   print("----------")
   
   keycont()
   inverse()
   print(res)
   
   msg = input("Please enter your msg : ")
   msg = msg.upper() # MESSAGE
    
   keys  = []
   for i in msg:
       if i != ' ':
           keys.append(alphabet.index(i))    
   N = ''
   for i in range(0,len(keys)):
       temp = (res*(keys[i]-B))%26
       N += alphabet[temp]
    
   print("Result:",N)
   
# main part
while True: 
    menu()
    if pro == 1: # cipher
        encrypt()
    elif pro == 2: # decipher
        decrypt()
    elif pro == 3: # quit
        break