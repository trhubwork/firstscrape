from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/Main_Page")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)

