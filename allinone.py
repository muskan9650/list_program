a=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
b=len(a)
even=0
even_num=0
odd_num=0
odd=0
sum=0
i=0
while i<=b:
    if a[i]%2==0:
        even=even+a[i]
        even_num=even_num+1
    else:
        odd=odd+a[i]
        odd_num=odd_num+1
    i=i+1
    sum=even+odd
print("sum of all", sum)
print("sum of even", even)
print("sum of odd", odd)
print("average of all",sum/b)
print("even average=",even/even_num)
print("odd average=",odd/odd_num)
print("even count=",even_num)
print("odd count=",odd_num)
print("all count=",b)