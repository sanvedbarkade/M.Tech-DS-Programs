#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

data=pd.read_csv("diabetes1.csv")


# In[2]:


data


# In[4]:


data.shape


# In[6]:


data.info()


# In[7]:


data.info


# In[8]:


data.value_counts()


# In[9]:


data.head


# In[11]:


data.values


# In[13]:


data.tail()


# In[14]:


data.head(100)


# In[16]:


data.tail(100)


# In[18]:


data.head().values


# In[20]:


data.Glucose


# In[21]:


pd.__version__


# In[22]:


import pandas


# In[24]:


pd.__version__


# In[26]:


data.Glucose.values


# In[27]:


data.describe()


# In[28]:


print(data)


# In[30]:


data[(data.Glucose>20)&(data.BloodPressure<90)]


# In[31]:


x=data.iloc[1:3,0:3]


# In[32]:


x


# In[33]:


data.iloc[0:500,0:4]


# In[34]:


data.iloc[:,:].tail()


# In[35]:


data.index


# In[36]:


data.axes


# In[37]:


data.dtypes


# In[41]:


print(data[["Glucose","BloodPressure","BMI"]].head(20))


# In[40]:


print(data["Glucose"])
data.Glucose


# In[43]:


import pandas as pd


# In[45]:


a=pd.DataFrame({'A':[1,2,3,4,5],'B':[4,5,6,7,8]},index=['a','b','c','d','e'])
print(a)
print(a.info())


# In[54]:


s=pd.Series([10,20,30,40,50,np.nan ],index=['a','b','c','d','e',np.nan])
print(s)
s.info()


# In[57]:


R=pd.DataFrame({'A':[1,2,3,4,5,np.nan],'B':[4,5,6,7,8,np.nan]},index=['a','b','c','d','e',np.nan])
R


# In[58]:


dates=pd.date_range("20250201",periods=28)
dates


# In[ ]:




