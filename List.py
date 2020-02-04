#!/usr/bin/env python
# coding: utf-8

# In[4]:


west_coast = ['WA', 'OR', 'CA', 'AR']
print(west_coast)


# In[5]:


for state in west_coast:
    print(state)


# In[6]:


print(west_coast[1])


# In[10]:


print("The length of the list \'west_coast\' is : ", len(west_coast))


# In[15]:


print(range(4))
print(len(range(4)))
print(type(range(4)))

for i in range(4):
    print(i)


# In[16]:


opposite_corner = ['Florida', 'Georgia', 'South Carolina']


# In[19]:


corners = west_coast + opposite_corner
print(corners)


# In[30]:


corners.append('North Carolina')
print(corners)


# In[28]:


corners.remove('North Carolina')


# In[31]:


print(corners)


# In[34]:


corners.insert(4, 'Alabama')


# In[35]:


print(corners)


# In[42]:


p = ['true', 'false']
q = ['true', 'false']
r = ['true', 'false']


# In[41]:


comb = []
for x in p:
    for y in q:
        for z in r:
            print(x, y, z)


# In[46]:


random.random()


# In[48]:


import random


# In[49]:


randlist = []
for i in range(20):
    randlist.append(random.randint(0, 100))
print(randlist)


# In[52]:


randlist.sort()


# In[53]:


print(randlist)


# In[63]:


def how_many_a_in_b(a , b):
    count = 0
    for i in b:
        if i == a:
            count += 1
    return count
    print(i)

a = 'a'
b = ['b', 'a', 'n', 'a','n', 'a' ]
how_many_a_in_b(a, b)


# In[66]:


a = 'a'
b = 'asdfadsfafasdfsadfasdagsdfads'
splitB = b.split('a')


# In[67]:


print(splitB)


# In[ ]:




