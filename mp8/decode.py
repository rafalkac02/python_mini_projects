# Print all headings from bbc.com in "news" and "sport" sections

import requests
from bs4 import BeautifulSoup

url = 'http://www.bbc.com'
r = requests.get(url)
text = BeautifulSoup(requests.get(url).text, features='lxml')

for heading in (text.find_all(rev="news|headline") + text.find_all(rev="sport|headline")):
    if heading.a:
        print(heading.a.text.replace("\n").strip())
    else:
        print(heading.contents[0].strip())