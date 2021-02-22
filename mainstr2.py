# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# subStr = 'over' 
# replace = 'on'
# var = mainStr.split()
# print(var)
# i = 0
# b =  " "
# while i < len(var):
#     if var[i] == subStr :
#         b = b + "on" + " "
#     else :
#         b = b + var[i]  + " "
#     i = i + 1
# # print(b)


# k="i saw a CD play-er and a modern in ccd"
# b=" "
# list1=[]
# for i in k:
#     if i==" ":
#         list1.append(b)
#         b=" "
#     else:
#         b+=i
# print(list1)




k="i saw a cd player and a modern in ccd"
for i in range(len(k)):
    count=0
    # j=i+1
    # for j in range(i+1, len(k)):
    if k[i]>="a" and k[i]<="z":
        if k[i+1]==k[i]:
            count+=1
            print( k[i], count)
