#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
transactions = pd.read_csv('transactions.csv')


# In[6]:


orders.columns


# In[7]:


transactions.columns


# In[8]:


customers.columns


# In[10]:


merged_data = pd.merge(orders, transactions, on='order_id')
merged_data = pd.merge(merged_data, customers, on='customer_id')


# In[11]:


merged_data.head()


# In[20]:


hvt = merged_data[merged_data['sales']>150]


# In[24]:


hvt_by_oc = hvt.groupby(by=['order_id','customer_name'])


# In[28]:


hvt_by_oc[['order_id','customer_name']].head()


# In[ ]:




