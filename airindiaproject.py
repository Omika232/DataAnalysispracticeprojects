import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime
import re
l = []
for i in range(1,10):
    url = f'https://www.airlinequality.com/airline-reviews/air-india/page/{i}/'
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text,'lxml')
    boxes = soup.find_all(name='article',attrs={'itemprop':'review'})
    for box in boxes:
      dictionary_review = {}
      rating = box.find(name='span',attrs={'itemprop':'ratingValue'}).get_text()
      title = box.find(name='h2',attrs={'class':'text_header'}).get_text().replace('"','')
      date = box.find(name='time',attrs={'itemprop':'datePublished'})['datetime']
      review = box.find(name='div',attrs={'class':'text_content'}).get_text()
      d = {}
      table = box.find(name='table',attrs={'class':'review-ratings'})
      table_rows= table.find_all('tr') # [tr1 , tr2 ,tr3]
      for table_row in table_rows:
         key = table_row.find_all('td')[0].get_text()
         value = table_row.find_all('td')[1]
         if(value['class']==['review-rating-stars', 'stars']):
           value = len(value.find_all(name='span',attrs={'class':'star fill'}))
         else:
           value = value.get_text()
         d[key] = value
         dictionary_review['title'] = title
         dictionary_review['rating'] = rating
         dictionary_review['date'] = date
         dictionary_review['review'] = review
         dictionary_review['detail'] = d
      l.append(dictionary_review)
data = pd.json_normalize(l)
data['title']=data['title'].str.replace(r'[^ -~\t\n\r\f\v]','')
data.to_csv('sample.csv',index=False)
print(data)
#https://www.airlinequality.com/airline-reviews/air-india/page/2/