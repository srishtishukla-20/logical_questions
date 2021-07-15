str="hello"
print(str[:3])

str="my blog"
a=" "
for i in range(len(str)):
    a+=str[i]
    print(a)
    
str='MyBLog'
a=' '
for i in range(len(str)):
    print(a*str[i])
    #strings can't be multiplied

s='My'
s1='Blog'                        
s2=s[:1]+s1[len(s1)-1:]
print(s2)
print("my"+"blog"* 2)
print("my" *3 + "blog" +"7")

for i in range(2,7,2):
    print(i * '2')
    """ouput:22
             2222
             222222"""

for i in range(3,12, 2):
    print("a".upper())
    #5 times A will come in output

for i in range(3,12,13):
    print("a".upper)
#will throw error

print(s.find('come'))              
print(s.find('o'))
print(s.find('o', 10, 20))
print(s.find('o', 5, 10))
#name error "s"


