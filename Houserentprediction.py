import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import math

df = pd.read_csv(r'C:\Users\HP\Documents\House_Rent_Dataset.csv')
print(df)
df= df.drop(['Posted On', 'Point of Contact','Floor','Area Type',
'Area Locality','City','Furnishing Status','Tenant Preferred'],axis=1)
print(df)
sns.heatmap(df.corr(),annot= True)
plt.show()

X = df.drop('Rent',axis=1)
Y = df['Rent']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=1)
Model = LinearRegression()
Model.fit(X_train,Y_train)
predict = Model.predict(X_test)
print("possible error is ")
error = mean_squared_error(predict,Y_test)
print(error)
print("Accurecy is")
print(math.sqrt(error))
print('**Possible Rent In Future**')
print(Model.predict(([[4,1100,6]])))



