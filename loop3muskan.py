n="MUSKAN"
m=list(n)
# print(m)
for i in range(0, len(m)):
    j=0
    while j<=i:
        print(m[i],end=" ")
        m[i]=m[i].lower()
        j=j+1
    print("_", end=" ")
    m[i]=m[i].upper()
    i+=1