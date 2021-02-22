list1=["HELLO", "TAKE"]
list2=["DEAR", "SIR"]
list3=[]
i=0
while i<len(list1):
    j=0
    while j<len(list2):
        c=list1[i], list2[j]
        list3.append(c)
        j=j+1
    i=i+1
print(list3)