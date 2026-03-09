#!/usr/bin/env python
# coding: utf-8

# # Data Preprocessing Template

# ## Import Libraries

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ##  Importing the data set and assign X as input value y as Output value 

# In[9]:


pd.set_option('display.float_format', str)
dataset = pd.read_csv('C:/ConsoleFlare_Classes/PolynomialRegression/Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# ## Print Input Values

# In[10]:


print(X)


# ## Print Output Values

# In[11]:


print(y)


# ## Encoding String Values into Numeric Values using OneHot Encoder

# In[12]:


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encode', OneHotEncoder(), [0])], remainder='passthrough')
X = ct.fit_transform(X)


# ## Printing Updated Input Value with 3 new Columns

# In[13]:



print(X)


# ## Encoding String Values into Numeric Values using LabelEncoder

# In[15]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)


# ## Printing Updated OutPut Value with Numerical Encoding

# In[16]:


print(y)


# ## Splitting the dataset into the Training set and Test set

# In[17]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 2)


# ## Printing The Splitted Values

# In[18]:


print("Trained Input Value")
print(X_train)


# ## Standardization of Values Age and Salary

# In[19]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])


# ## Printing The Standardization Values

# In[20]:


print("Trained Input Value")
print(X_train)


# In[ ]:





# In[ ]:




