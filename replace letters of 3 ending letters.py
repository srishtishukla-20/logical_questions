s=input("enter word")
if len(s)> 2:
    if s[-1]=="e":
        x=s.replace("e","ing")
        print(x)
    if s[-3:] == 'ing':
        s+="ly"
        print(s)
    elif s[-2:]!="ly":
        s+="ly"
        print(s)
    else:
      s += 'ing'
      print(s)
else:
    print(s)
