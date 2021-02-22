a=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
b=[]
for i in a:
    if i in a:
        if i not in b:
            b.append(i) 
print(b)