user=int(input("enter year"))
user1=user
i=4
count=1
while i<user:
    u=user-i
    if u%4==0:
        if count<=3:
            print("preceding leap years are:",u)
        count+=1
    i+=1
print("............")
j=4
count1=1
while j<user1:
    u1=user1+j
    if u1%4==0:
        if count1<=3:
            print("coming leap years are:",u1)
            count1+=1
    j+=1
#preceding and coming leap years

    