#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
from numpy.random import random, uniform


# In[4]:


random_numbers = uniform(low=10.0, high=25.0, size=100000)


# In[5]:


connection = sqlite3.connect("orginal.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Pressure (reading float not null)")
query = "INSERT INTO Pressure (reading) VALUES (?);"


# In[6]:


for number in random_numbers:
    cursor.execute(query, [number])


# In[7]:


cursor.close()


# In[8]:


connection.commit()


# In[9]:


connection.close()


# In[ ]:




