str1 = "Welcome to my Blog"
print(str1[-1])
print(str1[9])
# g and o will be the output

str14 = "Welcome to My Blog"
for i in str14:
    print(i)

i=0
while i<len(str14):
    print(str14[i])
    i+=1

i=0
count=0
while i<len(str14):
    count+=1
    i+=1
print(count)

str1 = "Welcome to my Blog"
for i in str1:
    print(i)
    print(i, end =' ')
    print(i, end = '#')  

str1 = "Amit"
for i in str1:
    print(i)
    print(i, end =' ')

a="This is Sarjapur Campus"
b="Here rules are different"
c=a+b
print(c)

for i in range(2,5,2):
    print(i * '@')

for i in "Amit":
    print(i in "Amit")

S = "Welcome to my Blog"
print(S[2 : 3])
print(S[2 : 10])
print(S[-2 : ]) 
print(S[-10 : -2 : 2])

str1 = "Anita"
str1[1]  = 'm'
print(str1)
#strings are immutable

str1= "Amit"
str2 = "My Blog"
str3 = "#blog"
str4 = "My 1st Blog"
print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())
print(str4.isalpha())

s=input("enter sentence")
count=0
for i in range(0,len(s)):
    count+=1
print(count)

st="MY NAME IS NAVGURUKUL"
print(st.lower())

a = 123
b = "123"
b.isdigit()
a.isdigit()
print(b)
print(a)

d=input("enter sentence")
i=0
count=0
count1=0
while i<len(d):
    if d[i].islower():
        count+=1
    if d[i].isupper():
        count1+=1
    else:
        pass
    i+=1
print(count,"LOWER")
print(count1,"Upper")
#number of upper and lower

s = "My blog"
print(s.upper())
print(s.lower())
print(s.islower())
print(s.isupper())
print(s.isalpha())
print(s.isdigit())








