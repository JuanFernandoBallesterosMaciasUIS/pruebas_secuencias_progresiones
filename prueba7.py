n = int(input("digite hasta el numero de elemento que quieres que se genere: "))
s = "Serie= "


for i in range (1,n+1):
    c = i
    i = (5*i)-2
    if c != n:
        s = s + str(i) + ","  
    else:
        s = s + str(i)    
print(s)
