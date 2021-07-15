digit=(input("enter num"))
i=0
sum=0
fac=1
while i<len(digit):
    sum=sum+int(digit[i])
    fac=fac*sum
    i+=1
print(fac)
# sum of factorial


