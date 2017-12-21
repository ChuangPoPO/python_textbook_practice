
# coding: utf-8

# In[1]:


import random


# In[10]:


def recipt():
    res = ''
    for i in range(0,8):
        res += str(random.randint(0,9))
    return res
        


# In[11]:


# print(recipt())

