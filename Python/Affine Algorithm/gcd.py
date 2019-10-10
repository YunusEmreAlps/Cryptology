# Euclidean Algorithm find gcd

# (ax) = c mod b
numi = int(input(" - Enter dividend number : ")) # ax : dividend -> 7
modi = int(input(" - Enter divisor number : "))  # b : divisor -> 26

temp = max(numi,modi)
numi = min(numi,modi)
modi = temp

if((numi != 0)and(modi != 0)):

    while True:  
        if(numi != 0):
            print(f" - {modi}={numi}*{int(modi/numi)}+{modi%numi} \t- {modi}-{numi}*{int(modi/numi)}={modi%numi}")
            temp1 = modi
            temp2 = numi
            modi = temp2
            numi = temp1%temp2
        
        if(numi == 0):
            break
        
    print(" - Result : ",modi)
    
else:
        print(f" - Error : Negative number .")

