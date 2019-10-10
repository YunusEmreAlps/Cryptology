# Euclidean Algorithm and inverse mod

# (ax) = c mod b
numi = int(input(" - Enter dividend number : ")) # ax : dividend -> 7
modi = int(input(" - Enter divisor number : "))  # b : divisor -> 26

i=2 # counter
cont=False # control

while True: # infinity loop
    if((numi%i == 0)and(modi%i == 0)): # no coprime
        cont=False
        break
    if((i==modi)and(cont == False)): # coprime
        cont=True
        break
    i+=1

if((modi>numi)and(cont==True)):
    
    # a*x = 1 mod b
    # gcd(a*x,b*y) = 1
    
    icount = 0 # counter (x) 
    count2 = 0 # counter (y)
    
    ni = numi
    mdi = modi
    
    while True:  
        if(ni != 0):
            print(f" - {mdi}={ni}*{int(mdi/ni)}+{mdi%ni} \t- {mdi}-{ni}*{int(mdi/ni)}={mdi%ni}")
            temp1 = mdi
            temp2 = ni
            mdi = temp2
            ni = temp1%temp2
        
        if((numi*icount)%modi == 1):
            break
        icount+=1
    
    while True:
        if((numi*icount)-(modi*count2) == 1):
            break
        count2 +=1
        
    
    print(f"\n - {numi}*{icount} - {modi}*{count2} = 1")
    print(f" - {numi}^-1 = {icount} mod {modi}")
    print(f" - Result : {icount}")

else:
    if cont == False:
         print(" - There is no modular multiplicative inverse for this integer")
    if numi > modi:
        print(f" - Error : {numi} > {modi}")
    
