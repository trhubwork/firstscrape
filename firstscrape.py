from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.onthesnow.com/vermont/jay-peak/ski-resort.html")
bsObj = BeautifulSoup(html.read())
skiCondi = bsObj.findAll("span", {"class" : "current_status open"})
skiOpCl = bsObj.findAll("span", {"class" : "open_close"})

greenSki = bsObj.findAll("span", {"class" : "ovv_t t1"})
blueSki = bsObj.findAll("span", {"class" : "ovv_t t2"})
blackSki = bsObj.findAll("span", {"class" : "ovv_t t3"})
blackdiaSki = bsObj.findAll("span", {"class" : "ovv_t t4"})

for green in greenSki:
    print("Today's Ski Conditions \nGreen Slopes: " + green.get_text())
for blue in blueSki:
    print("Blue Slopes: " + blue.get_text())
for black in blackSki:
    print("Black Slopes: " + black.get_text())
for blackdia in blackdiaSki:
    print("Black Diamonds: " + blackdia.get_text())
for skiO in skiOpCl:
    print(skiO.get_text())
for ski in skiCondi:
    print("Open Days of the week: "+ ski.get_text())



