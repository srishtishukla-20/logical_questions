a=input("enter word")
print(a[::3])
if len(a)>2:
    if a[:-3]=="ing":

        a+="ly"
        print(a)
    else:
        a+="ing"
    print(a)
else:
    pass


