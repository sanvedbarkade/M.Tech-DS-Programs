#!/usr/bin/env python
# coding: utf-8

# In[29]:


import matplotlib.pyplot as plt
import numpy as np
x=[2,4,5,8]
y=[7,6,5,4]
plt.plot(x,y, color='orange')
plt.show()


# In[30]:


plt.subplots()


# In[31]:


a,b=plt.subplots()
b.plot([2,4,6,8],[3,5,7,8])
plt.show()


# In[32]:


import numpy
a=numpy.arange(50)
a


# In[33]:


b=numpy.random.randint(0, 2, 100)


# In[34]:


b


# In[39]:


c=np.random.randn(1,50,100)


# In[40]:


c


# In[45]:


data = { "a" : np.arange(50),
       'c' : np.random.randint(0, 50 ,50),
       'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout = 'constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

print(data)


# In[ ]:


##########################################################################################''


# In[ ]:


import pandas as pd
import stastmodels.api as sm

ds=pd.read_csv("mul_predictive_analysis - mul_predictive_analysis.csv")


# In[ ]:


ds


# In[ ]:




