import pandas as pd
import numpy
import datetime
import requests
from bs4 import BeautifulSoup
import re


finallist=[]
for i in range(1,60):
    print(f'collecting Data from page{i}')
    weburl = f'https://www.airlinequality.com/airline-reviews/air-india/page/{i}/'
#print(requests.get(weburl))
    webhtml_text=requests.get(weburl).content
#print(webhtml_text)
    soup1= BeautifulSoup(webhtml_text,"lxml")
#print(soup1)
#print(soup1.title)
    boxes=soup1.find_all(name='article',attrs={'itemprop':"review"})
#print(boxes)
    for boxe in boxes:
        dictionaryreview={}
        Title= boxe.find(name='h2',attrs={'class':'text_header'}).get_text().replace('"','')
        Rating=boxe.find(name='span',attrs={'itemprop':'ratingValue'})
        if (Rating == None):
            Rating = 0
        else:
            Rating.get_text()

        Date=boxe.find(name='time',attrs={'itemprop':'datePublished'})['datetime']
        Review = boxe.find(name='div',attrs={'class':'text_content'}).get_text()
        d={}
        Table=boxe.find(name='table',attrs={'class':'review-ratings'})
    #print(Table)
        Table_rows=Table.find_all('tr') #finding table first row
        for Tablerow in Table_rows:
           key= Tablerow.find_all('td')[0].get_text() #finding first row table value
           value= Tablerow.find_all('td')[1]
           if(value['class']==['review-rating-stars','stars']):
               value = len(value.find_all(name='span',attrs={'class':'star fill'}))
           else:
               value=value.get_text()
           d[key]=value
           dictionaryreview['title']=Title
           dictionaryreview['rating']=Rating
           dictionaryreview['date']=Date
           dictionaryreview['review']=Review
           dictionaryreview['details']=d
        finallist.append(dictionaryreview)
data=pd.json_normalize(finallist)
data['title']=data['title'].str.replace(r'[^ -~\t\n\r\f\v]','') #for if we want alphabate only so we can run also regecs querry
data.to_csv('airindiasrapdata.csv',index=False)
#print(data)
#print(data.isnull().sum())
#def F(r):
    #A= afinn()
    #return A.score(r)

df=pd.read_csv(r'airindiasrapdata.csv')
print(df)
#df['sentiment score']=df.['title'].apply(F)                                                                                                                   #details.Airecraft
                                                                                                                    #details.Seat Comfort
                                                                                                                    #details.Cabin Staff Service
                                                                                                                    #details.Food & Beverage
                                                                                                                    #details.Inflight Entertainment
                                                                                                                    #details.Ground Service
                                                                                                                    #details.Wifi & Connectivity








#https://www.airlinequality.com/airline-reviews/air-india/page/2/