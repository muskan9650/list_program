a = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
b=len(a)
row1=0
row2=0
row3=0
col1=0
col2=0
col3=0
diagonal1=0
diagonal2=0
diagonal3=0
i=0
while i<b:
    c=len(a[i])
    j=0
    while j<c:
        if i==0:
            row1 = row1 + a[i][j]
        elif i==1:
            row2 = row2 + a[i][j]
        else:
            row3 = row3 + a[i][j]
        j=j+1
    m=0
    while m<c:
        if m==0:
            col1 = col1 + a[m][i]
        elif m==1:
            col2 = col2 + a[m][i]
        else:
            col3 = col3 + a[m][i]
        m=m+1
    n=0
    while n<c:
        if n==0:
            diagonal1=diagonal1 + a[n][n]
        elif n==1:
            diagonal2=diagonal2 + a[n][n]
        else:
            diagonal3=diagonal3 + a[n][n]
        n=n+1
    i=i+1
if row1==row2==row3==col1==col2==col3==diagonal1==diagonal2==diagonal3:
    print("it is magic square")
else:
    print("it is not magic square")