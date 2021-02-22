# def split(s, delim):
#     a = []
#     i = 0
#     temp_s = ''
#     while(i<len(s)):
#         if s[i] != delim:
#             temp_s += s[i]
#         else:
#             a.append(temp_s)
#             temp_s = ''
#         i += 1
#     a.append(temp_s)
#     return a 

# print(split("Muskan Tannu Thakur", "_"))




a=[1, 2, 7, 8, 9, 3]
b=[]
i=0
while i<len(a):
    if a[i]>5:
        print(a[i])
        b.append(a[i])
        i=i+1
print(b)