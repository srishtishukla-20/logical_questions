
s="mamatha"
new_str=""
for i in range (len(s)):
    if s[i]=="m":
        new_str+=s[i].upper()
    else:
        new_str+=s[i].lower()
print(new_str)



