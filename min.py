a=[50, 40, 23, 70, 56, 12, 5, 10, 7]
min=a[0]
for i in range(len(a)):
    if a[i]<min:
        min=a[i]
print(min)