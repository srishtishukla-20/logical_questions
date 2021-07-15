num=int(input("enter num"))
i = 10**(len(str(num))-1)
ans = ''
while num:
    if (num//i)*i != 0:
        ans += str((num//i)*i) + ' + '
        num = num % i
        i=i//10
        a=(ans[0:len(ans)-3])
    print(a)




