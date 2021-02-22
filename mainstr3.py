mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr='over'
list1=list(mainStr)
print(list1)
i=0
b=' '
list1=[]
while i<len(list1):
    if list1[i] ==' ':
        list1.append(b)
        b=b+ " "
    else:
        b=b+list[i]
    i=i+1
print(b)