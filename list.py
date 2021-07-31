list1=[7,11,5,4,1]
list2=[]
n=0
while n<len(list1):
    if list1[n]%2!=0:
        list2.append(list1[n])
        a=sorted(list2)
    n+=1
c = 0
list3= []
i=0
while i<len(list1):
    if (list1[i]) % 2 != 0 :
        list3.append(c)
    c+=1
    i+=1
print(list3)
x=0
while x<len(list3):
    z = list3[x]
    list1[z] = a[x]
    # print(list1)
    x+=1
print(list1)

#sorting odd elements without changing position of even numbers 
