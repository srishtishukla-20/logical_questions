# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i=0
# count=1
# list=[]
# while i<count:
#     count+=1
#     j=i
#     while j<count:
#         list.append(l[i])
#         j+=1
#     i+=1
# print(list)
def elements_difference(nums):
    result = [j-i for i, j in zip(nums[:-1], nums[1:])]
    return result

nums1 = [1,2,3,4,5,6,7,8,9,10]
print("\nDfference between elements (n+1th – nth) of the said list :")
print(elements_difference(nums1))






