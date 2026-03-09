import pandas as pd
from afinn import Afinn
import matplotlib.pyplot as plt
from wordcloud import WordCloud
df=pd.read_csv(r"airindiasrapdata.csv")
df=df.dropna(subset='title')
#print(df.isnull().sum())
def f(r):
   a=Afinn()
   r='this is worst service'
   return a.score(r)
df['sentimetscore']=df['title'].apply(f)
#print(df)
ndf=df.groupby('details.Type Of Traveller').agg(avg_snt=('sentimetscore','mean'))
#print(ndf)
text = ' ' .join(df['title'])   #when we need that our series convert into big string then we can use function use .join
#wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
text = text.lower()
wordcloud = WordCloud(width=800, height=400, background_color='white',stopwords=['is','the','good','flight','air' ,'india', 'line','air line','not','was','experiance']).generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axis
plt.title('Word Cloud')
plt.show()