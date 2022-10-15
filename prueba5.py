n = int(input("digite hasta el numero de elemento que quieres que se genere: "))
s = "Serie= "
e = 1
for i in range (1,n+1):
    c = i
    i = i**2 +1
    if c == n+1:
        s = s + "1/" + str(i)
    else:
        s = s + "1/" + str(i) + ","      
print(s)