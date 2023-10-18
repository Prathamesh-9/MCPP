#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[2]:


customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
transactions = pd.read_csv('transactions.csv')


# In[3]:


orders.columns


# In[4]:


transactions.columns


# In[5]:


customers.columns


# In[6]:


merged_data = pd.merge(orders, transactions, on='order_id')
merged_data = pd.merge(merged_data, customers, on='customer_id')


# In[7]:


merged_data.head()


# In[8]:


hvt = merged_data[merged_data['sales']>250]


# In[9]:


hvt.shape


# In[10]:


hvt_new = hvt.groupby(by=['order_id','customer_name'])[['order_id','customer_name']]
hvt_new.head()


# In[11]:


hvt.columns


# In[12]:


hvt['order_purchase_date'].head()


# In[13]:


from datetime import datetime as dt


# In[14]:


hvt['order_month'] = pd.to_datetime(hvt['order_purchase_date'].str.strip()).dt.month
hvt['order_year'] = pd.to_datetime(hvt['order_purchase_date'].str.strip()).dt.year


# In[15]:


hvt


# In[16]:


hvt_new = hvt.groupby(by=['order_month','order_year'])['order_id'].size()


# In[17]:


hvt_new


# In[ ]:




