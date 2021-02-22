a=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# max=max(a)
# print(max)
max=a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
        print(max)