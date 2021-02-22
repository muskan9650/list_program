a = [
    [8, 3, 8],
    [1, 5, 9],
    [6, 7, 2]
] 
b=len(a)
row1,row2,row3,col1,col2,col3,diagonal1,diagonal2=0,0,0,0,0,0,0,0
i=0
while i<b:
    c=len(a[i])
    j=0
    while j<c:
        if i==0:
            row1 = row1 + a[i][j]
            col1 = col1 + a[j][i]
        elif i==1:
            row2 = row2 + a[i][j]
            col2 = col2 + a[j][i]
        else:
            row3 = row3 + a[i][j]
            col3 = col3 + a[j][i]
        j=j+1
    i=i+1
m=0
k=2
while m<c:
    diagonal1 = diagonal1 + a[m][m]
    diagonal2 = diagonal2 + a[m][k]
    m=m+1
    k=k-1
if row1==row2==row3==col1==col2==col3==diagonal1==diagonal2:
    print("it is magic square")
else:
    print("it is not magic square")