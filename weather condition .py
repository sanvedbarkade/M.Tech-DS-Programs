#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[5]:


d= pd.read_csv("weather_condition.csv")


# In[6]:


d


# 

# In[12]:


hot_encoded_data= pd.get_dummies(d, columns = ['Weather_Condition'])
hot_encoded_data


# In[14]:


x1= pd.get_dummies(d, columns = ["Weather_Condition"])
x1


# In[15]:


y1= pd.get_dummies(d, columns = ["Match Played"])


# In[16]:


y1


# In[17]:


#############################################################################################################


from sklearn.preprocessing import OrdinalEncoder

import numpy as np
e=OrdinalEncoder()


# In[31]:


X = [['male','from US', 'uses safari'],['female','from europe','uses firefox'],['child','from india','uses google']]
X


# In[32]:


e.fit(X)
e.transform(X)


# In[33]:


X1 = [['male'],['female'],[np.nan],['child']]
X1


# In[34]:


e.fit_transform(X1)


# In[ ]:




