#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
data = [23,46,34,78,101,92,56]


# In[3]:


data = [23,46,34,78,101,92,56]


# In[6]:


mean = np.mean(data)
median = np.median(data)
skewness = stats.skew(data)
std_dev = np.std(data)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize= (12, 5))

ax1.hist(data, bins=range(20,90,10),edgecolor='black', alpha=0.7, color="skyblue")
ax1.axvline(mean, color='red', linestyle = '-', label=f'mean: {mean:.2f}')
ax1.axvline(median, color='green', linestyle ='-',label=f'median:{median}')
ax1.set_title('Histogram of data')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax1.legend()
ax1.grid(axis='y', alpha=0.4)


# In[8]:


plt.tight_layout()
plt.show()


# In[11]:


print("statistical Summary:")
print(f"Sample Size: {len(data)}")
print(f"mean: {mean:.2f}")
print(f"Median: (median)")
print(f"Standerd Deviation: {std_dev:.2f}")
print(f"Skewness: {skewness:.2f}")


# In[ ]:


plt.subplot(1, 2, 2)
plt.boxplot(data, vert+True, patch_artist=True, box)


# In[ ]:





# In[ ]:




