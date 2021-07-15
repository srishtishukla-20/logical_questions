d=input("enter name")
b=""
i=0
while i<len(d):
    if len(d)>3:
        if i==0:
            b+=d[i]
        if i==1:
            b+=d[i]
            b+=d[-i-1]
            b+=d[-i]
    elif len(d)<=3:
        print(d)
        break
    i+=1
print(b)