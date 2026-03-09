import requests
from bs4 import BeautifulSoup
import pandas as pd
import collections

url='https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
html_txt1 = requests.get(url).content
title1= BeautifulSoup(html_txt1,"lxml")
#for single phone scraping
box=title1.find(name='a', attrs={'class': "_1fQZEK"})
phone_name=box.find(name='div',attrs={'class':'_4rR01T'}).get_text()
price=box.find(name='div',attrs={'class':'_30jeq3 _1_WHN1'}).get_text()
#Rating=box.find(name='div',attrs={'class':''}).get_text()
print(phone_name,price)

