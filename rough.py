import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

warnings.filterwarnings('ignore')
n1df = pd.DataFrame()
filesname = os.listdir('SalesData')
for filename in filesname:
    ndf = pd.read_csv(f'SalesData/{filename}')
    n1df = pd.concat([ndf, n1df])
n1df.to_csv('SalesDataflp2.csv', index=False)
# now cleaning process
df = pd.read_csv(r'SalesDataflp2.csv')
df = df.loc[df['Order ID'] != 'Order ID']
df.to_csv('SalesDataflp2.csv',index=False)
df['Quantity Ordered']=df['Quantity Ordered'].astype('float')
df['Price Each']=df['Price Each'].astype('float')
df=df.dropna(how='all')
df.to_csv('SalesDataflp2.csv',index=False)
df['Total']=(df['Quantity Ordered']*df['Price Each']) #for question first
df['Order Date']= pd.to_datetime(df['Order Date'])
df['Month']=df['Order Date'].dt.month
df['Month Name']=df['Order Date'].dt.month_name()
df.to_csv('SalesDataflp2.csv',index=False)
mdf=df.groupby(['Month','Month Name']).agg(total_sale=('Total','sum'))
mdf=mdf.reset_index()
mdf.to_csv('Monthalytotalsales.csv',index=False)
print(mdf)
#for graph
ndf=pd.read_csv(r'Monthalytotalsales.csv')
plt.bar(ndf['Month_Name'],ndf['total_sale'],color='pink')
plt.title('Monthly sales graph')
plt.xticks(rotation=45)
plt.xlabel('month name')
plt.ylabel('total sale in lakh')
plt.grid()
for x,y in  zip(ndf['Month_Name'],ndf['total_sale']):
    plt.text(x, y,y, va='bottom', ha='right', color='black', fontsize=6)
plt.show()

#project work
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')
n1df = pd.DataFrame()
filesname = os.listdir('SalesData')
for filename in filesname:
    ndf = pd.read_csv(f'SalesData/{filename}')
    n1df = pd.concat([ndf, n1df])
n1df.to_csv('SalesDataflp2.csv', index=False)
# now cleaning process
df = pd.read_csv(r'SalesDataflp2.csv')
df = df.loc[df['Order ID'] != 'Order ID']
df.to_csv('SalesDataflp2.csv',index=False)
df['Quantity Ordered']=df['Quantity Ordered'].astype('float')
df['Price Each']=df['Price Each'].astype('float')
df=df.dropna(how='all')
df.to_csv('SalesDataflp2.csv',index=False)
df['Total']=(df['Quantity Ordered']*df['Price Each']) #for question first
df['Order Date']= pd.to_datetime(df['Order Date'])
df['Month']=df['Order Date'].dt.month
df['Month_Name']=df['Order Date'].dt.month_name()
df.to_csv('SalesDataflp2.csv',index=False)
print(df)
mdf=df.groupby(['Month','Month_Name']).agg(total_sale=('Total','sum'))
mdf=mdf.reset_index()
mdf.to_csv('Monthalytotalsales.csv',index=False)
#for graph
ndf=pd.read_csv(r'Monthalytotalsales.csv')
plt.bar(ndf['Month_Name'],ndf['total_sale'],color='pink')
plt.title('Monthly sales graph')
plt.xticks(rotation=45)
plt.xlabel('month name')
plt.ylabel('total sale in lakh')
plt.grid()
for x,y in  zip(ndf['Month_Name'],ndf['total_sale']):
    plt.text(x, y,y, va='bottom', ha='right', color='black', fontsize=6)
plt.show()


