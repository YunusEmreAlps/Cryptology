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
    nc = 1
    
    while True: # infinity loop
            if(((numi*nc)%modi) == 1): # status positive
                break
            nc += 1
    print(nc)
       
else:
    if cont == False:
        print("There is no modular multiplicative inverse for this integer")
    
    elif (numi > modi):    
        print(f"Error: {numi} > {modi} ")