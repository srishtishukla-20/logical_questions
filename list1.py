grocery_list = ['flour','cheese','carrots']
i=0
while i<len(grocery_list):
    print(i,":",grocery_list[i])
    i+=1


list= [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
a=""
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        a+=(list[i][j])
        j+=1
    i+=1
print(a)
# The String after join: gfgisbest

List = [6,1,3,5,6,3,1]
a=[]
i=0
while i<len(List):
    if List[i] not in a:
        a.append(List[i])
        j=0
        mul=1
        while j<len(a):
            mul=mul*a[j]
            j+=1
    i+=1
print(mul)
#multiplication excluding duplicates

input_list = [1, 2, 2, 5, 8, 4, 4, 8]
new=[]
i=0
count=0
while i<len(input_list):
    if input_list[i] not in new:
        new.append(input_list[i])
        count+=1
    i+=1
print(count)
print(new)
#Count = 5 #because [1,2,5,8,4] are unique values.




