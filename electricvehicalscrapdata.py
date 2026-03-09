import pandas as pd
from bs4 import BeautifulSoup
import warnings
import re
import requests

weburl = f'https://trucks.tractorjunction.com/en/electric'
#print(requests.get(weburl))
webhtml_text = requests.get(weburl).content
#print(webhtml_text)
soup1 = BeautifulSoup(webhtml_text,"lxml")
box = soup1.find(name='div',attrs= {'class':'newTruckBlock-inner sectionShadow m-t-16'})
#print(box)
Name = box.find(name = 'p', attrs = {'class':'newTruckBlock-title boldfont'}).get_text()
print(Name)
#company_name = box.find(name = 'span',attrs={'class': 'sectionShadow'}).get_text()
#print(company_name)
#Price = box.find(name = 'p',attrs = {'class':'newTruckSingle-price boldfont'} ).get_text()
#print(Price)
#Fuel_Type = box.find(name='a',attrs={'class':'linkclr'}).get_text()
#print(Fuel_Type)

#Range = box.find(name= 'p',attrs = {'class':'boldfont'}).get_text()
#print(Range)
Charging_Time = box.find(name= 'div',attrs={'class':'toolsBlock-inner sectionShadow'}).get_text()
print(Charging_Time)