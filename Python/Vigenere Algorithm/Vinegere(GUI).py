# Vinegere Algorithm (GUI)

import tkinter # GUI : Graphical User Interface

# global variable
alpbh = ('A','B','C','D','E','F','G','H','I','J','K',
         'L','M','N','O','P','Q','R','S','T','U','V',
         'W','X','Y','Z') # <class 'tuple'> -> alphabeth
msgs = [] # <class 'list'>
keys = [] # <class 'list'>

A = "" # new message
j=0

def decode(): # decipher
    global keys
    global msgs
    global A
    global j
    msg = theEntry1.get()
    msg = msg.upper()
    key = theEntry2.get()
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
    theEntry3 = tkinter.Entry(root, font="arial 14", bd=2)
    theEntry3.insert(0,f"Decode Text:{A}")
    theEntry3.place(x=50, y=300, width=370, height=30)


def encode(): # cipher
    global keys
    global msgs
    global A
    global j
    msg = theEntry1.get()
    msg = msg.upper()
    key = theEntry2.get()
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
    print(A)    
    theEntry4 = tkinter.Entry(root, font="arial 14", bd=2)
    theEntry4.insert(0,f"Encode Text:{A}")
    theEntry4.place(x=50, y=350, width=370, height=30)


# Graphical Component
root = tkinter.Tk() # window
root.title("Vinegere Algorithm")
root.configure(background="white")
root.minsize(width=500, height=500)
root.resizable(width=False, height=False)

theLabel1 = tkinter.Label(root, font="arial 14", text="MESSAGE")
theLabel1.place(x=50, y=100, width=150, height=30)

theEntry1 = tkinter.Entry(root, font="arial 14", bd=2)
theEntry1.place(x=220, y=100, width=200, height=30)

theLabel2 = tkinter.Label(root, font="arial 14", text="KEY")
theLabel2.place(x=50, y=150, width=150, height=30)

theEntry2 = tkinter.Entry(root, font="arial 14", bd=2)
theEntry2.place(x=220, y=150, width=200, height=30)

theButton1 = tkinter.Button(root, font="arial 14", text="DECRYPT", command=decode)
theButton1.place(x=220, y=200, width=200, height=30)

theButton2 = tkinter.Button(root, font="arial 14", text="ENCRYPT", command=encode)
theButton2.place(x=220, y=250, width=200, height=30)

root.mainloop()