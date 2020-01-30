#!/usr/bin/env python
# coding: utf-8

# In[9]:


x = 13
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')


# In[46]:


hourrate = 10
overtimerate = 15

def payperhours(hours):
    if hours <= 40:
        return ((hours * hourrate))
    elif hours > 40:
        #return ((hours % 40) * 15) + 400
        return ((hours % 40) * overtimerate) + ((hours - (hours % 40)) * hourrate)

print(payperhours(40))
print(payperhours(45))


# In[52]:


def computepay(hours, rate = 10):
    if hours <= 40:
        return (hours * rate)
    elif hours > 40:
        return ((hours % 40) * 15) + ((hours - (hours % 40)) * rate)

print(computepay(40, 10))
print(computepay(45, 10))


# In[55]:


def computepay(hours, rate = 10):
    if hours <= 40:
        print((hours * rate))
    elif hours > 40:
        print(((hours % 40) * 15) + ((hours - (hours % 40)) * rate))

computepay(45, 10)


# In[68]:


def computepay(hours, rate = 10):
    if hours <= 40:
        print((hours * rate))
    elif hours > 40:
        print(((hours % 40) * 15) + ((hours - (hours % 40)) * rate))

inputhours = input("how many hours did you work?")
computepay(int(inputhours), 10)


# In[ ]:




