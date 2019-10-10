# Fermat Algorithm 2

# x^129 = 9 mod 17
# x = ? 

numi = 'x' # a : dividend
quot = int(input(" - Enter the quotient number : ")) # quotient
basi = int(input(" - Enter the base number : ")) # base
modi = int(input(" - Enter divisor number : "))  # p : divisor

i=2 # counter
cont = False
cont2=False # control

while True: # infinity loop
    if(modi%i == 0): # modi == prime number
        cont2=False
        break
    if(i == (modi-1)):
        cont2=True
        break
    i+=1


if((modi > quot)and(cont2==True)):        
    frmt = modi-1
    counter = 1

    
    while True:
        if((counter**(basi%frmt))%modi == quot):
            cont=True
            break
        if counter > modi:
            cont=False
            break
        counter+=1
        
    if (cont == True):
        print(f" - {numi}^{basi} = {quot} mod {modi}")
        print(f" - x is {counter}")
    
    else:
        print(" - Error 404 not found")
    
    

else:
    if cont2 == False:
         print(" - There is no modular multiplicative inverse for this integer")
