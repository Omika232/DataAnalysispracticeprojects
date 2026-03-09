import pandas as pd
df = pd.read_csv(r'C:\Users\HP\Documents\Electric_Vehicle_Population_Data.csv')
#print(df)
#print(df.info)
#print(df.describe())
#print(df.shape)
#print(df.head(5))
#print(df.tail(10))
#print(df.isnull().sum())
df= df.drop(columns='Legislative District')
print(df.shape)

#total ev in this dataset
print('total_vehicle is : ' , df.shape[0])
#total_Vehicle_eachType  = df.groupby('Electric Vehicle Type').count()
total_Vehicle_eachType= df["Electric Vehicle Type"].value_counts()
print(total_Vehicle_eachType)
#Which manufacturers have the highest number of electric vehicles?
df1 = df['Make'].value_counts()
df1=df1.sort_values(ascending=False).head(5)
print(f'Most famous company that have most car : {df1}')
#What are the most common models of electric vehicles?
df2= df['Model'].value_counts().head(5)
print(f'most common model is : {df2}')
#Top regions or states with the highest number of electric vehicles
df3= df['State'].value_counts().sort_values(ascending=False).head(5)
print(f'Top 5 Most Populer city which have More Electric vehicals is :{df3}')
#Range of electric vehicles by manufacturer
df4= df['Electric Range'].mean()
print(f'Avrage Range of Ev : {df4}')
#Average range  of electric vehicles according model
df5=df.groupby('Model')['Electric Range'].mean()
print(df5)

