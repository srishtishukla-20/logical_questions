# Given a List, extract all elements whose frequency is greater than K.
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
test_list1=[]
K = 3
i=0
while i<len(test_list):
    if test_list[i]  not in test_list1:
        if test_list[i]>=K:
            test_list1.append(test_list[i])
    i+=1
# print(test_list1)

# Output: [4, 3]
a= [4, 5, 5, 5, 3,3,3,8]
i=0
while i<len(a)-2:
    if a[i] == a[i + 1]:
        if a[i + 1] == a[i + 2]:
            print(a[i])
    i+=1
#output:5,3


