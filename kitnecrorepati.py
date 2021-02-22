a= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
b=len(a)
i=0
crorepati=0
lakhpati=0
diwale=0
while i<b:
    if a[i]>10000000:
        crorepati=crorepati+1
    elif a[i]>100000 and a[i]<10000000:
        lakhpati=lakhpati+1
    else:
        diwale=diwale+1
    i=i+1
print("diwale=", diwale, "lakhpati=", lakhpati, "crorepati=", crorepati)