#!/usr/bin/env python
# coding: utf-8

# In[14]:


b=[1,2,3,4,5]#memory allocation in python id heap structure
print(b)
print(id(list))


# In[12]:


b[2] = 11
b


# In[13]:


print(id(list))


# In[16]:


b[1:3]=23,25


# In[17]:


b


# In[20]:


b[-1]=28


# In[21]:


b


# In[22]:


num1 = [1,2,3,4,5]
num2 = [5,6,7,8,9]


# In[24]:


num1*2 


# In[25]:


num1 + num2


# In[41]:


print(6 in num1)


# In[42]:


len(num2)


# In[43]:


if 10 in num1:
    print(True)
else:
    print(False)
    


# In[51]:


for i in num1[:-1]:
    print(i)


# In[52]:


for i in num1:
    print(i-1)


# In[56]:


num3 = [1,2,3,4,5]
num3


# In[58]:


num3.append(8)


# In[59]:


num3


# In[63]:


num3.insert(3,10)


# In[64]:


num3


# In[67]:


num3.extend([7,8,9,0])


# In[70]:


num3


# In[71]:


num1


# In[72]:


num1.pop()


# In[73]:


num1


# In[79]:


del num1[2]


# In[80]:


num1


# num3.remove(3)

# In[87]:


num3


# In[88]:


num3.reverse()


# In[89]:


num3


# In[90]:


num3.sort()


# In[91]:


#what are the built in methods in python 


# In[92]:


del num1


# In[93]:


num1


# In[ ]:


###################################################################


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


import matplotlib as plt1
plt1.__version__


# In[9]:


fruit_set = {1,2,8,4,9}


# In[10]:


fruit_set


# In[11]:


fruit_set


# In[ ]:





# In[12]:


fruit_set


# In[15]:





# In[ ]:




