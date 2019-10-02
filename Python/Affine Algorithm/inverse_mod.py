# inverse mod

numi = int(input("Please enter your number : ")) 
modi = int(input("Please enter your divisor : ")) 

i=2
cont = False

while True: # coprime control
    if ((numi%i == 0)and(modi%i == 0)): # no coprime
        cont = False
        break
    elif i > modi: # coprime 
        cont = True
        break
    i+=1

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
    print("Result :",res)
else:
    if cont == False:
        print("There is no modular multiplicative inverse for this integer")
    
    elif (numi > modi):    
        print(f"Error: {numi} > {modi} ")