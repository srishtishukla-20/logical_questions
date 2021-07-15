a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
i=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i])+1:
        sum=sum+a[j][i]
        
        j+=1
    i+=1
    avg=sum/len(a[j])
    print(avg)


# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]
