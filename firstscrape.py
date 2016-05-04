from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.onthesnow.com/vermont/jay-peak/ski-resort.html")
bsObj = BeautifulSoup(html.read())
skiCondi = bsObj.findAll("span", {"class" : "current_status open"})
skiOpCl = bsObj.findAll("span", {"class" : "open_close"})

for skiO in skiOpCl:
    print(skiO.get_text())

for ski in skiCondi:
    print(ski.get_text())



