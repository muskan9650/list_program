a=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
b=len(a)
even=0
even_num=0
odd_num=0
odd=0
i=0
while i<=11:
    if a[i]%2==0:
        even=even+a[i]
        even_num=even_num+1
    else:
        odd=odd+a[i]
        odd_num=odd_num+1
    i=i+1
print("even average=",even/even_num, "and", "odd average=",odd/odd_num)