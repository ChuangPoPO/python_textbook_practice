
# coding: utf-8

# In[1]:


import random    


# In[6]:


def lotto(n, m):
    nums = [i for i in range(1, n+1)] 
    return random.sample(nums, m)
    


# In[9]:


# n = int(input('n:'))
# m = int(input('m:'))
# print(lotto(n,m))

