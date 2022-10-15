n = int(input("digite hasta el numero de elemento que quieres llegar: "))
s = "Serie= "

for i in range(1,n+1):
    i = i * i
    if i == n+1:
        s = s + str(i)
    else:
        s = s + str(i) + ","
print(s)