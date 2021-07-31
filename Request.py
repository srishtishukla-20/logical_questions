import requests
import json
result=requests.get('https://join.navgurukul.org/api/partners')
a=result.json()
def nav():
    count=1
    l=[]
    dict1={}
    for i in a["data"]:
        s=count,i["name"]
        # print(s)
        l.append(s)
        count+=1
    print(l)
    dict1["PARTNERS"]=l
    # print(dict1)
    with open ("Partners.json","w+") as file:
        json.dump(dict1,file,indent=2)
nav()