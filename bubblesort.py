a=[7,6,8,2,1,4]
i=0
j=1
while i<len(a):
    if a[i]>a[j]:
        print(a[i],a[j]," ", end="")
    else:
        print(a[j],a[i], " ", end="")
    i=i+2
    j=j+2