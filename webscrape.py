import requests
from bs4 import BeautifulSoup
import json
url=requests.get("https://webscraper.io/test-sites")
data=BeautifulSoup(url.text,"html.parser")
def scrape_heading(url):
    mainDiv=data.find_all("h2",class_="site-heading")
    dict1={}
    l=[]
    for i in mainDiv:
        title=i.text.strip()
        l.append(title)
    dict1["Heading"]=l
    print(dict1)
    with open ("heading.json","w+") as file:
        json.dump(dict1,file,indent=4)
scrape_heading("https://webscraper.io/test-sites")