# RSA Algorithm (GUI)

import tkinter # GUI : Graphical User Interface

# global variables
prime_p = False
prime_q = False
prime_e = False
e_msg=""

 # prime number control
def prime():
    global prime_q
    global prime_p
    p = int(theEntry1.get())
    q = int(theEntry2.get())
    
    i = 2
    prime_p = False

    if p>10: 
        while True: # prime number control
            if(p%i == 0):
                prime_p = False
                break
        
            if((p-1) == i and p!=2):
                prime_p = True
                break
        
            i+=1
        
# ----------
    i = 2
    prime_q = False
    if q>10:
        while True: # prime number control
            if(q%i == 0):
                prime_q = False
                break
        
            if((q-1) == i):
                prime_q = True
                break
        
            i+=1 
        
        
# encode
def encode():
    global prime_q
    global prime_p
    global prime_e
    prime()
    
    if(prime_q == True and prime_p == True):
        p = int(theEntry1.get())
        q = int(theEntry2.get())
        msg = theEntry3.get()
        
        n=p*q
        tot=(p-1)*(q-1)
        
        i=2    
        while True:
            if(tot%i == 0):
                prime_e = False
        
            elif(tot%i != 0):
                e=i
                break
            i+=1
    
        e_msg = ""
        for i in msg:
            number = 0
            number = ord(i)
            c = (number**e)%n
            e_msg+=chr(c)
            
            
        theLabel4 = tkinter.Label(root, font="arial 14", bg="white", text=" Encrypt: ")
        theLabel4.place(x=100, y=350, width=110, height=30)
        theEntry4 = tkinter.Entry(root, bd=2, font="arial 14")
        theEntry4.insert(0,f"{e_msg}")
        theEntry4.place(x=230, y=350, width=200, height=30) 
        
# decode
def decode():
    global prime_q
    global prime_p
    global prime_e
    global e_msg
    prime()
    if(prime_q == True and prime_p == True):
        p = int(theEntry1.get())
        q = int(theEntry2.get())
        msg = theEntry3.get()
        
        n=p*q
        tot=(p-1)*(q-1)
        
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
        d_msg=""
    
        # ascii number
        e_msg = ""
    
        for i in msg:
            number = 0
            number = ord(i)
            c = (number**e)%n
            e_msg+=chr(c)
    
        # Decrypt
        for i in e_msg:
            number=0
            number=ord(i)
            m = (number**d)%n
            d_msg+=chr(m)
    
        theLabel5 = tkinter.Label(root, font="arial 14", bg="white", text=" Decrypt: ")
        theLabel5.place(x=100, y=400, width=110, height=30)
        theEntry5 = tkinter.Entry(root, bd=2, font="arial 14")    
        theEntry5.insert(0,f"{d_msg}")
        theEntry5.place(x=230, y=400, width=200, height=30)
        

    
# window
root = tkinter.Tk()
root.title(" RSA Algorithm")
root.configure(background="white")
root.minsize(width=500, height=500)
root.resizable(width=False, height=False)

# Label
theLabel1 = tkinter.Label(root, font="arial 14", bg="white", text=" P:")
theLabel1.place(x=100, y=100, width=110, height=30)
theLabel2 = tkinter.Label(root, font="arial 14", bg="white", text=" Q:")
theLabel2.place(x=100, y=150, width=110, height=30)
theLabel3 = tkinter.Label(root, font="arial 14", bg="white", text=" MESSAGE:")
theLabel3.place(x=100, y=200, width=110, height=30)

# Entry
theEntry1 = tkinter.Entry(root, bd=2, font="arial 14")
theEntry1.place(x=230, y=100, width=200, height=30)
theEntry2 = tkinter.Entry(root, bd=2, font="arial 14")
theEntry2.place(x=230, y=150, width=200, height=30)
theEntry3 = tkinter.Entry(root, bd=2, font="arial 14")
theEntry3.place(x=230, y=200, width=200, height=30)

# Button
theButton1= tkinter.Button(root, font="arial 14", text="Encrypt", command=encode)
theButton1.place(x=230, y=250, width=200, height=30)
theButton2= tkinter.Button(root, font="arial 14", text="Decrypt", command=decode)
theButton2.place(x=230, y=300, width=200, height=30)

root.mainloop()