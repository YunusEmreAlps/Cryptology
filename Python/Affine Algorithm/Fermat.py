# Fermat Algorithm

# (a)^p = a mod p
numi = int(input(" - Enter dividend number : ")) # a : dividend
basi = int(input(" - Enter the base number : ")) # base
modi = int(input(" - Enter divisor number : "))  # p : divisor

i=2 # counter
cont=False # control

while True: # infinity loop
    if((numi%i == 0)and(modi%i == 0)): # no coprime
        cont=False
        break
    if((i == max(numi,modi)))and(cont == False): # coprime
        cont=True
        break
    i+=1


i=2 # counter
cont2=False # control

while True: # infinity loop
    if(modi%i == 0): # modi == prime number
        cont2=False
        break
    if(i == (modi-1) and cont == True):
        cont2=True
        break
    i+=1

print(cont)
print(cont2)

if((cont==True)and(cont2==True)):        
    frmt = modi-1
    result = (numi**(basi%frmt))%modi
    print(f"{numi}^{basi} = {result} mod {modi}")


else:
    if cont == False:
         print(" - There is no modular multiplicative inverse for this integer")
