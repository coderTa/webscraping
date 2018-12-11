import requests as r
from bs4 import BeautifulSoup as bs

query = input("What do you want to look up? ")
query = query.replace(' ', '+')
result = r.get('https://www.google.com/search?q=' + query)
text = bs(result.text)
search_results = text.find_all("div", {"class": "g"})
clean_search_results = []

for i in range(len(search_results)):
    title = search_results[i].find("h3", {"class": "r"})

    if title != None:
        title = title.text
        print(title)

    description = search_results[i].find("span", {"class": "st"})

    if description != None:
        description = description.text
        print(description)
        print("\n")