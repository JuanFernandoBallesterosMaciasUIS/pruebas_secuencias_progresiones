n = int(input("digite hasta el numero de elemento que quieres llegar: "))
s = "Serie: "
for i in range (1,n+1):
    if i< n:
        s = s + str(i) + ","
    else:
         s = s + str(i) 
print(s)