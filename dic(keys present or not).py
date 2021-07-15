
d1= {"key":1,"key2":2,"key3":3}
d2={"key":1,"key2":2}
for k in d1.values():
    if k in d2:
        if d1[k] == d2[k]:
            print ("Key and value not matches in d1 and d2")
        else:
            print("key and value matches in d1 and d2")