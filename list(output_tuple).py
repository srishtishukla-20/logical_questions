a=[1,2,3]
a1=[]
a2=[]
i=0
while i<len(a)-1:
    a1.append(a[i])
    # print(a1)
    i+=1
a2.append(a[-1])
# print(a2)
a3=[]
j=0
while j<len(a):
    m1=a1[j],a1[j+1]
    m2=a1[j],a2[j]
    m3=a1[j+1],a2[j]
    a3.append(m1)
    a3.append(m2)
    a3.append(m3)
    break
print(a3)
# a=[(1,2),(1,3),(2,3)]
















































# a=[-1,10,11,9,-1,5,3,8]
# s=1
# i=0
# m=[]
# while i<len(a):
#     if a[i]<a[s]:
#         a[s]=a[i]
#         m.append(a[s])
#     s+=1
#     i+=1
# print(m)



