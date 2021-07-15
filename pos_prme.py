st=input("enter string")
dic={}
for x in st:
    if x in dic:
        dic[x]=dic[x]+1
    else:
        dic[x]+=1
for key in dic:
    print(key,":",dic[key])