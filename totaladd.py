num=30
n=[10, 11, 12, 13, 14, 17, 18, 19]
b=len(n)
i=0
while i<b:
    j=0
    while j<8:
        if n[i]+n[j]==30:   
            print(n[i],n[j])
            pass
        j=j+1
    i=i+1

