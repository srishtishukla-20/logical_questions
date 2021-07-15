n=[1,3,4,[6,8,9]]
i=0
a=[]
sum=0
while i<len(n):
    if type(n[i])==list:
        j=3
        while j<=3:
            sum=sum+n[i][j]
            j+=1
    else:
        sum=sum+n[i]
    i=i+1
a.append(sum)
print(a)
# i=0
# a=[]
# j=0
# while i<len(n):
#     # j=0
#     # while j<len(n):
#     a.append(n[i])
#     a.append([j])
#         # j+=1
#     i+=1          
# print(a)  

marks=[[45, 56, 23, 44],[56, 55,76,87,34],[88,54,24,33,12]]
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+(marks[i][j])
        j=j+1
    i=i+1
print(sum)
