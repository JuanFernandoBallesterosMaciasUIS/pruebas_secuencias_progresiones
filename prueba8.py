n = int(input("digite hasta el numero de elemento que quieres que se genere: "))
s = "Serie= "

for i in range (1,n+1):
    c = i
    
    e = i
    i = i ** (i - 1)
    e = (2 * e) + 1
    if c == n:
        s = s + str(i) + "/" + str(e)
    else:
        s = s + str(i) + "/" + str(e) + ","      
print(s)