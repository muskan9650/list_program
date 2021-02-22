list=[[78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]]
n=len(list)
i=0
sum = 0
while i<n:
    j=0
    b=len(list[i])
    while j<b:
        sum = sum + list[i][j]
        j=j+1
    i=i+1
print(sum)