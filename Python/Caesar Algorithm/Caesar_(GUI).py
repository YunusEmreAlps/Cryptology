# Ceasar Algorithm

import tkinter # GUI: Graphical User Interface
alpbh = ('A','B','C','D','E','F','G','H','I','J','K',
         'L','M','N','O','P','Q','R','S','T','U','V',
         'W','X','Y','Z') # <class 'tuple'> -> alphabeth

A = "" # new message

# decode (decipher)
def decode():
    global alpbh
    global A
    
    msg = theEntry1.get()
    msg = msg.upper()
    key = int(theEntry2.get())
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
    
    
    theEntry3 = tkinter.Entry(root,bd=2,font="arial 14")
    theEntry3.insert(0,f"Decoded Text : {A}")
    theEntry3.place(x=50,y=300,width=400,height=30)
    
# encode (cipher)
def encode():
    global alpbh
    global A
    
    msg = theEntry1.get()
    msg = msg.upper()
    key = int(theEntry2.get())
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
    
    theEntry4 = tkinter.Entry(root,bd=2,font="arial 14")
    theEntry4.insert(0,f"Encoded Text : {A}")
    theEntry4.place(x=50,y=350,width=400,height=30)    

# ----------
# window settings
root = tkinter.Tk() # window
root.title("Ceasar Algorithm")
root.configure(background="white")
root.minsize(width=500, height=500)
root.resizable(width=False, height= False)
# ----------
# label and entry
theLabel1 = tkinter.Label(root,font="arial 14",text="MESSAGE : ")
theLabel1.place(x=30,y=100,width=200,height=30)

theEntry1 = tkinter.Entry(root,bd=2,font="arial 14")
theEntry1.place(x=250,y=100,width=200,height=30)

theLabel2 = tkinter.Label(root,font="arial 14",text="KEY : ")
theLabel2.place(x=30,y=150,width=200,height=30)

theEntry2 = tkinter.Entry(root,bd=2,font="arial 14")
theEntry2.place(x=250,y=150,width=200,height=30)

# ----------
# button
theDecode = tkinter.Button(root,font="arial 14",text="DECRYPT",command=decode)
theDecode.place(x=250,y=200,width=200,height=30)
theEncode = tkinter.Button(root,font="arial 14",text="ENCRYPT",command=encode)
theEncode.place(x=250,y=250,width=200,height=30)

root.mainloop() 