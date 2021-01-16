#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# Let's create a Index object

# In[11]:


pd_index = pd.Index(['index1','index2','index3'],name='index')


# In[12]:


print(pd_index)


# Important attributes that can help to understand Index object

# In[16]:


pd_index.values


# In[35]:


pd_index.name


# In[19]:


pd_index.dtype


# How about MultiIndex object, let's generate one.

# In[28]:


arrays = [['col1','col2','col3'],['lev1','lev2','lev3']]
pd_MultiIndex = pd.MultiIndex.from_arrays(arrays,names=['col','lev'])


# In[29]:


print(pd_MultiIndex)


# Again, play with the attributes a bit to get familiar with the composition of this special object.

# In[30]:


pd_MultiIndex.names


# In[31]:


pd_MultiIndex.levels


# In[34]:


pd_MultiIndex.levels[0]


# In[ ]:




