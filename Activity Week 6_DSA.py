#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_excel(r"C:\Users\Tejes\Downloads\Dataset_w6.xlsx")
data.head(10)


# In[6]:


data.columns


# # 1) Find out how many countries are there in the Dataset
# 

# In[8]:


print('No of countries in the given Dataset is: ',data['country'].count())


# # 2) Visualize The Given Dataset

# In[9]:


data2=data.sort_values(by='GDP per capita (current US$)',ascending=False).head(10)
fig,ax1= plt.subplots(figsize=(8,8))
x=data2['country']
y1=data2['GDP per capita (current US$)']
y2=data2['Agricultural production index ']
y3=data2['International trade: Imports (million US$)']
ax1.plot(x,y1, color='green')
plt.xticks(rotation=90)
ax2=ax1.twinx()
ax2.plot(x,y2,color='blue')
ax3=ax1.twinx()
plt.xticks(rotation=90)
ax3.plot(x,y3,color='red')
plt.xticks(rotation=90)
ax3.spines['right'].set_position(('outward',60))
ax1.set_ylabel('G D P',color='green')
ax2.set_ylabel('A P I',color='blue')
ax3.set_ylabel('INTERNATIONAL TRADE', color='red')
ax1.set_xlabel('COUNTRIES')
ax1.tick_params(axis='y',colors='green')
ax2.tick_params(axis='y',colors='blue')
ax3.tick_params(axis='y',colors='red')
ax2.spines['right'].set_color('blue')
ax3.spines['right'].set_color('red')
ax3.spines['left'].set_color('green')
plt.show()


# # 3) Find out how many countries with respect to the region are available in the        dataset
# 

# In[10]:


data['Region'].value_counts()


# # 4 a) On average which region has the highest -  GDP Per Capita

# In[11]:


highest_gdp=data.groupby('Region')['GDP per capita (current US$)'].mean()
print('The region with highest GDP is: ',highest_gdp.nlargest(1))


# # 4 b) On average which region has the highest -  International trade: Imports (million US$)

# In[12]:


highest_import=data.groupby('Region')['International trade: Imports (million US$)'].mean()
print('The region with highest import trade is: ',highest_import.nlargest(1))


# # 5) Find out which region has more consistent with respect to GDP per capita (current US$)

# In[15]:


least_gdp_variation=data.groupby('Region')['GDP per capita (current US$)'].std().round(3)
least_gdp_variation.sort_values(ascending=True)


# In[16]:


print('The region which is the most consistent with GDP is: ',least_gdp_variation.nsmallest(1))


# In[ ]:




