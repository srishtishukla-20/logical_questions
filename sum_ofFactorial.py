n=int(input("enter num"))
i=1
fac=1
sum=0
while i<n:
    fac=fac*i
    sum=sum+fac
    i+=1
print(sum)