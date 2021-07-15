test_list = [1, 2, 3, 4, 5, 6]
list1=[]
i=0
while i<len(test_list)-1:
    res=[test_list[i],test_list[i+1]]
    list1.append(res)
    i+=1
print(list1)

