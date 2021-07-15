a = "refrigerator"
count = 0
for i in a:
    count = count+1
print (count)

b="umbrella"
f=input("enter letter")
for i in b:
    if f in b:
        print("Yes it exists")
        break
    print("no it does not exists")
    break
s="This is a orange juice"
p=s.split()
i=0
while i<len(p):
    if p[i]=="juice":
        print("yes")
        break
    i+=1
str_123="Hello World"

i=0
count=0
while i<len(str_123):
    if str_123=="o":
        count=count+1
        print(count)
    i+=1


a = input("enter your full name")
gender=input("enter m for male and f for female")
marital_status=input("enter single/married")
b= a.split()
c=""
ab=""
i=0
while i<len(b)-1:
    j=0
    while j<=0:
        u=b[i][j]
        if gender=="f":
            if marital_status=="married":
                b="Mrs"
                ab+=b
                c+=u
            elif marital_status=="single":
                b1="Miss"
                ab+=b1
                c+=u
            else:
                pass
        elif gender=="m":
            if marital_status=="married":
                b="Mr"
                ab+=b
                c+=u
            elif marital_status=="single":
                b1="Mister"
                ab+=b1
                c+=u
            else:
                pass
        else:
            pass
        j+=1
    i+=1
k=1
c1=""
while k<=1:
    e=b[k]
    c1+=e
    k+=1
print(ab,".",c,".",c1)