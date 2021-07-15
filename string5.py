str1 = "Welcome to my Blog"
print(len(str1))

str2 = "###Welcome to my Blog"
print(len(str2))
print(len(str2.lstrip()))

str2 = "###Welcome to my Blog####"
print(len(str2))
print(len(str2.strip()))
print(len(str2.rstrip()))

str1 = "Welcome to my Blog"
print(str1.rstrip('og'))
print(str1.lstrip('We'))
print(str1.strip('Welog'))


s1 = "   "
s2 = "   Amit"
print(s1.isspace())
print(s2.isspace())

str1 = "welcome to My Blog"
print(len(str1))
print(str1.capitalize())

str1 = "Welcome to my Blog"
x = str1.split()
print(x)

f=input("enter sentence or word")
i=0
count=0
while i<len(f):
    count+=1
    print(f[i])
    i+=1
print(count)

a = "Mummy?Papa?Brother?Sister?Uncle" 
print(a.split())
print(a.split('?'))
print(a.split('?',1))
print(a.split('?',3))
print(a.split('?',10))
print(a.split('?',-1))


str1 = "I do you do and we all will do"
x=str1.replace("do","done")
print(x)

str1 = "I went to Auli"
print(str1.replace("Auli", "Leh"))
print(str1)











