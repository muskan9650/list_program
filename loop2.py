n=int(input("enter a number"))
a=3
while a>0:
    j=''
    if a>=2:
        n=n//100
        i=n*n
        i=str(n)
        j=j+i
        n=n*10
    else:
        n=n//10
        i=n*n
        i=str(n)
        j=j+i
    a=a-1
    print(j, end=")
        