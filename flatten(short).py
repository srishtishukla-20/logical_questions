a=[1,[2,3],4,[5,6]]
m=[]
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            m.append(a[i][j])
            j+=1
    else:
        m.append(a[i])
    i+=1
print(m)
