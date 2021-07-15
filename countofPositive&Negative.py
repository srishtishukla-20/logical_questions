list1 = [2, -7, 5,8, -64, -14]
i=0
pos=0
neg=0
while i<len(list1):
    if list1[i]>1:
        pos+=1
    elif list1[i]<1:
        neg+=1
    i+=1
print("positive numbers:",pos)
print("negative numbers:",neg)
# Output: pos = 3, neg = 3
