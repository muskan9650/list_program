a=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
b=len(a)
even=0
odd=0
i=0
while i<=11:
    if a[i]%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i+1
print("even number=", even, "and", "odd number=", odd)