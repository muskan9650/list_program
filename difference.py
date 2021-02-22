list1=[1, 2, 3, 4, 5, 6]
list2=[2, 3, 1, 0, 6, 7]
a=len(list2)
i=0
while i<=a:
    if list1[i] in list2:
        continue
    else:
        print(list1[i])
    i=i+1