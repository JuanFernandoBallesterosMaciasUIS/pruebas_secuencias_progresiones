n = int(input("digite hasta el numero de elemento que quieres que se genere: "))
s = "Serie= "
for i in range (1,n+1):
    i = 0 + i
    if i == n+1:
        s = s + "1/" + str(i)
    else:
        s = s + "1/" + str(i) + ","      
print(s)