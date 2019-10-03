# Substitution Algorithm

alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U','V','W','X','Y','Z')
            # <class 'tuple'>

nalphabeth = ('X','N','Y','A','H','P','O','G','Z','Q','W','B','T',
              'S','F','L','R','C','V','M','U','E','K','J','D','I')
            # <class tuple>
            
N = '' # new message            

# ----------

pro = 0 # process number

# ----------
# menu
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
# encrypt
def encrypt():
    global N
    global alphabet
    global nalphabeth
    print("----------")
    msg = input("Please enter your message : ")
    msg = msg.upper()
    
    N = ''
    for i in msg:
        if i != ' ':
            temp = int(alphabet.index(i))
            N += nalphabeth[temp]
    
    print("Result : ",N)
    
# ----------
# decrypt
def decrypt():
    global N
    global alphabet
    global nalphabeth
    print("----------")
    msg = input("Please enter your message : ")
    msg = msg.upper()
    
    N = ''
    for i in msg:
        if i != ' ':
            temp = int(nalphabeth.index(i))
            N += alphabet[temp]
    
    print("Result : ",N) 

        
     
# ----------
# main function
while True:
    menu()
    if pro==1: # cipher
        encrypt()
    elif pro==2: # decipher
        decrypt()
    elif pro==3: # quit
        break