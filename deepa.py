num=9119
list=""
multiple =1
while num>0:
    i=num%10
    num=num//10
    multiple=i*i
    list=list+str(multiple)

  
   
print(list)