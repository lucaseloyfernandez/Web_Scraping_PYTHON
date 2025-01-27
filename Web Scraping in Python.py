#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests


# In[5]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[7]:


print(soup)


# In[9]:


soup.find('table', class_ = 'wikitable sortable')


# In[11]:


table = soup.find_all('table')[1]


# In[13]:


print(table)


# In[15]:


world_titles = table.find_all('th')


# In[17]:


world_titles


# In[19]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[21]:


import pandas as pd


# In[23]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[25]:


column_data = table.find_all('tr')


# In[29]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[31]:


df


# In[ ]:


# we download the data into CSV file in the path we want to. Later we analyze the data in excel.


# In[33]:


df.to_csv(r"C:\Users\lucas\Desktop\Programacion 2019\Phyton\Web Scraping in Python\Companies.csv", index = False)


# In[ ]:





# In[3]:





# In[5]:





# In[7]:





# In[14]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




