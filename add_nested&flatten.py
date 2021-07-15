l=[1,2,3,[6,8,4]]
l1=[]
sum=0
i=0
while i<len(l):
    if type(l[i])==list:
        a=l[i]
    i+=1
j=0
b=[]
while j<len(l)-1:
    b.append(l[j])
    j+=1
list1=a+b
for i in list1:
    sum+=i
print(sum)





	