import pandas as pd
df=pd.read_csv(r'Reactions.csv')
#df.info()
#df.describe()
#df.shape
#df.columns
# df.head()
print(df.isnull().sum())#user id and type coloumns have null values in this data
df=df.drop(columns='User ID')
df=df.dropna(subset=['Type'])
print(df.isnull().sum())
df=df.rename(columns={'Type':'ReactionType'})
print(df)
df2=pd.read_csv(r'Content.csv')
df2.isnull().sum()#199 url coloumn are null
df2=df2.drop(columns=['URL','User ID'])
df2=df2.rename(columns={'Type':'ContentType'})
print(df2)


df3=pd.read_csv(r'ReactionTypes.csv')
df3=df3.rename(columns={'Type':'ReactionType'})
print(df3.isnull().sum())
df3=df3.sort_values(by='Score',ascending=False)
print(df3)

df4=df.merge(df2,on='Content ID',how='inner')
df4['Category'] = df4['Category'].str.replace('"', '').str.replace("'", '')
print(df4)
df4.to_csv('accenturedata1.csv',index=False)

df5=pd.read_csv(r'accenturedata1.csv')
print(df5.shape)
dff=df5.merge(df3,on='ReactionType',how='left')
dff.to_csv('accenturefinaldataset.csv',index=False)
print(dff)
dff=dff.groupby('Category')['Score'].max().sort_values(ascending=False)
#dff=dff.sort_values(by='Category', ascending=True)

top5CT= dff.head(5)
top5CT.to_csv('tops5catogary.csv',index=False)
print(top5CT)


