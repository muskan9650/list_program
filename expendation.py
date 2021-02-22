n=int(input("enter a number"))
count=0
while n>0:
    n=n//10
    count+=1
    while n<=count:
        n=n//10
        print(n)
