
a=[[4,3],[3,9]]
# op:[[9,-3],[-3,4]]
i=0
list1=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j] not in list1:
            list1.append(a[i][j])
            list1.insert(2,3)
        j+=1
    i+=1
print(list1)
k=0
l=[]
while k<len(list1):
    if list1[k]==4:
        l.append(9)
    elif list1[k]==9:
        l.append(4)
    elif list1[k]==3:
        l.append(-3)
    k+=1
print(l)
list2=[]
list3=[]
p=0
h=2
while p<=2:
    if l[p] not in list2:
        list2.append(l[p])
    p+=1
while h<=3:
    if l[h] not in list3:
        list3.append(l[h])
    h+=1
print(list2)
print(list3)
Main=[]
main1=[]
u=0
while u<len(list2):
    if list2[u] not in Main:
        Main.append(list2[u])
        Main.append(list3[u])
        main1.append(Main)
        print(main1)
    u+=1


