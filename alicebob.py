alice= [11, 2, 3]
bob = [3, 2, 1]
i=0
count=1
while i<len(alice):
    if alice[i]>bob[i]:
        print("Alice will get",count,"points")
    elif alice[i]<bob[i]:
        print("Bob will get",count,"points")
    else:
        print("No one will get any points")
    i+=1
    count+=1