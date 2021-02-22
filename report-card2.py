marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
] 
n=len(marks)
j=len(marks[0])+len(marks[1])+len(marks[2])
print(j)
i=0
sum = 0
while i<n:
    j=0
    b=len(marks[i])
    while j<b:
        sum = sum + marks[i][j]
        j=j+1
    i=i+1
print(sum/j)