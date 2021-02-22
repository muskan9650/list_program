i, j, k, s, m, n, d, l, p = 1, 1, 3, 5, 7, 9, 1, 3, 4
while i<=5:
    while j<=i:
        print(j, end=" ")
        j+=1
    while k<=1+i:
        print(k, end=" ")
        k+=1
    while s<i+3:
        print(s,end=" ")
        s=s+1
    while m<i+4:
        print(m, end=" ")
        m=m+1
    while n<i+5:
        print(n, end=" ")
        n=n+1
    while d<i:
        print(2*d, end=" ")
        d+=1
    while l<i+1:
        print(l, end=" ")
        l+=1
    print( )
    i+=1