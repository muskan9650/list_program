a=input("enter a name")
z=len(a)
i=0
j=-1
while i<z:
    if (a[i]==a[j]):
        i=i+1
        j=j-1
print("it is palindrome")