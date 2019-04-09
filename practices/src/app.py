#!/usr/bin
import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.walmart.com/ip/Mainstays-Folding-Plush-Saucer-Chair-Multiple-Colors/44706680?wmlspartner=wlpa&selectedSellerId=0&wl13=3112&adid=22222222227033477566&wl0=&wl1=g&wl2=c&wl3=69080058152&wl4=pla-135801016832&wl5=9028059&wl6=&wl7=&wl8=&wl9=pla&wl10=8175035&wl11=local&wl12=44706680&wl13=3112&veh=sem&gclid=Cj0KCQjwkIzlBRDzARIsABgXqV-8boxoV8-vTn2n-yMSSXyOiaN3ZOu0KM5m75Ac0leYe-mRXgQTx5AaArrNEALw_wcB")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class":"price-characteristic", "itemprop":"price"})
print(element.text.strip())
#<span class="price-characteristic" itemprop="price" content="29.00">29</span>


