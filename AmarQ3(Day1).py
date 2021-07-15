user=int(input("enter value"))
user1=user
i=1
count=1
while i<user:
    u=user-i
    if u%(2)==0:
        if count<=3:
            print("previous even numbers are:",u)
        count+=1
    i+=1
print("............")
j=1
count1=1
while j<user1:
    if user1%2!=0:
        if count1<=3:
            print("preceding odd numbers are:",user1)
        count1+=1
    user1+=j
#coming odd and previous even
    

