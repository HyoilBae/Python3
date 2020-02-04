#!/usr/bin/env python
# coding: utf-8

# In[1]:


#this exercise will use .split(), .strip(), .format(), for loops, and functions to fix and create "poem discription"

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)


# In[3]:


# use .split() to create new list
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)


# In[4]:


# clean up white spaces and add each index into the new list
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())
print(highlighted_poems_stripped)


# In[5]:


# break up all the information for each poem into it's own list
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(':'))
print(highlighted_poems_details)


# In[6]:


#separate out all of the titles, the poets, and the dates into their own lists
titles = []
poets = []
dates = []
#Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the list titles, poets, and dates
for poem in highlighted_poems_details:
    titles.append(poem[0])
    poets.append(poem[1])
    dates.append(poem[2])
print(titles)
print(poets)
print(dates)


# In[7]:


#write a for loop that uses either f-strings or .format() to prints out the following string for each poem: The poem TITLE was published by POET in DATE.
for i in range(0, len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))


# In[ ]:




