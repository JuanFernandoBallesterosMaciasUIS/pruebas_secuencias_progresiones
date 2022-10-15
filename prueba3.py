n = int(input("digite hasta el numero de elemento que quieres que se genere: "))
s = "Serie= "
for i in range (1,n+1):
    i = 2**i
    if i == 2**n:
        s = s + str(i)
    else:
        s = s + str(i) + ","      
print(s)