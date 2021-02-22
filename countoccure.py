a = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
b=[]
for i in a:
    if i in a:
        if i not in b:
            b.append(i) 
print(b)
j=0
list=[]
while j<len(b):
    n=0
    count=0
    while n<len(a):
        if a[n] == b[j]:
            count=count+1
        n=n+1
    x = [b[j],count]
    list.append(x)
    j=j+1
print(list)