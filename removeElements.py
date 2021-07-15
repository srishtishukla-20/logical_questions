# a=[1,1, 2 ,3 ,4, 5 ,1, 2]
# l=[]
# i=0
# while i<len(a):
#     if a[i]>1:
#         if a[i] not in l:
#             l.append(a[i])
#     i+=1
# l.append(2)
# print(l)
# Output :
# 2 3 4 5 2
T=[5, 6, [], 3, [], [], 9]
s=[]
i=0
while i<len(T):
    if type(T[i])!=list:
        s.append(T[i])
    i+=1
print(s)
# List after empty list removal: [5, 6, 3, 9]

