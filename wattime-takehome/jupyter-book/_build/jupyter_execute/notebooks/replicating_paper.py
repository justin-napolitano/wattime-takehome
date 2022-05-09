#!/usr/bin/env python
# coding: utf-8

# # Replicating the University of Malysia Paper.  

# ## Imports

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


# ## University of Malaysia Data

# In[2]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx"

malaysia_emissions_df = pd.read_excel(filepath)


# In[3]:


# Selecting 2020 columns
malaysia_2020 = malaysia_emissions_df[["iso3_country","country_name", "tCH4_2020"]].copy()


# In[4]:


malaysia_2020


# ## FAOSTAT Data 2019

# In[5]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/emissions_csv_fao_emiss_csv_ch4_fao_2015_2019_tonnes.xlsx"

faostat_emissions_df = pd.read_excel(filepath)


# In[6]:


faostat_2019 = faostat_emissions_df[['code', 'country', 'country_fao', 2019]].copy()


# In[7]:


faostat_2019


# In[8]:


faostat_2019.rename(columns={"code": "iso3_country"}, inplace =True)


# ## Merging Data on Iso3 Country Code

# In[9]:


merged2020_df = faostat_2019.merge(malaysia_2020, on='iso3_country', how='left', sort=False)


# In[10]:


merged2020_df


# ### Calculate difference in Tonnes Between the Estimates

# In[11]:


# Calculate Difference in tons
merged2020_df['diff_2020'] = merged2020_df[2019] - merged2020_df['tCH4_2020']




# ### Calculating the Percent Differences Between the Estimates

# In[12]:


merged2020_df['abs_percent_diff_2020'] = (abs((merged2020_df[2019] - merged2020_df['tCH4_2020']))/(merged2020_df[2019] + merged2020_df["tCH4_2020"])/2)*100

merged2020_df['relative_percent_diff_2020'] = (merged2020_df[2019] - merged2020_df['tCH4_2020'])/(merged2020_df[2019])*100



# In[13]:


merged2020_df


# ### Tonnes CH4 FAOSTAT - TRACE Plot

# In[14]:


merged2020_df.plot(kind = "barh", x = 'country_fao', y = ["diff_2020"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize = (10,10))


# ### Percent Difference FAOSTAT - TRACE

# In[15]:


merged2020_df.plot(kind = "barh", x = 'country_fao', y = ["relative_percent_diff_2020"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize=(10,10))


# ## Recreating the Malysia Paper with 2018 Data.  

# ### University of Malaysia Data

# In[16]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx"

malaysia_emissions_df = pd.read_excel(filepath)


# In[17]:


# Selecting 2020 columns
malaysia_2020 = malaysia_emissions_df[["iso3_country","country_name", "tCH4_2020"]].copy()


# In[18]:


malaysia_2020


# ## FAOSTAT Data 2018

# In[19]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/emissions_csv_fao_emiss_csv_ch4_fao_2015_2019_tonnes.xlsx"

faostat_emissions_df = pd.read_excel(filepath)


# In[20]:


faostat_2018 = faostat_emissions_df[['code', 'country', 'country_fao', 2018]].copy()


# In[21]:


faostat_2018


# In[22]:


faostat_2018.rename(columns={"code": "iso3_country"}, inplace =True)


# ### Merging Data on Iso3 Country Code

# In[23]:


merged2020_df = faostat_2018.merge(malaysia_2020, on='iso3_country', how='left', sort=False)


# In[24]:


merged2020_df


# ### Calculate difference in Tonnes Between the Estimates

# In[25]:


# Calculate Difference in tons
merged2020_df['diff_2020'] = merged2020_df[2018] - merged2020_df['tCH4_2020']




# ### Calculating the Percent Differences Between the Estimates

# In[26]:


merged2020_df['abs_percent_diff_2020'] = (abs((merged2020_df[2018] - merged2020_df['tCH4_2020']))/(merged2020_df[2018] + merged2020_df["tCH4_2020"])/2)*100

merged2020_df['relative_percent_diff_2020'] = (merged2020_df[2018] - merged2020_df['tCH4_2020'])/(merged2020_df[2018])*100



# In[27]:


merged2020_df


# ### Tonnes CH4 FAOSTAT - TRACE Plot

# In[28]:


merged2020_df.plot(kind = "barh", x = 'country_fao', y = ["diff_2020"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize = (10,10))


# ### Percent Difference FAOSTAT - TRACE

# In[29]:


merged2020_df.plot(kind = "barh", x = 'country_fao', y = ["relative_percent_diff_2020"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize=(10,10))


# ## Recreating the Malysia Paper same year

# ### University of Malaysia Data

# In[30]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx"

malaysia_emissions_df = pd.read_excel(filepath)


# In[31]:


# Selecting 2020 columns
malaysia_2018 = malaysia_emissions_df[["iso3_country","country_name", "tCH4_2018"]].copy()


# In[32]:


malaysia_2018


# ## FAOSTAT Data 2018

# In[33]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/emissions_csv_fao_emiss_csv_ch4_fao_2015_2019_tonnes.xlsx"

faostat_emissions_df = pd.read_excel(filepath)


# In[34]:


faostat_2018 = faostat_emissions_df[['code', 'country', 'country_fao', 2018]].copy()


# In[35]:


faostat_2018


# In[36]:


faostat_2018.rename(columns={"code": "iso3_country"}, inplace =True)


# ### Merging Data on Iso3 Country Code

# In[37]:


merged2018_df = faostat_2018.merge(malaysia_2018, on='iso3_country', how='left', sort=False)


# In[38]:


merged2018_df


# ### Calculate difference in Tonnes Between the Estimates

# In[39]:


# Calculate Difference in tons
merged2018_df['diff_2018'] = merged2018_df[2018] - merged2018_df['tCH4_2018']




# ### Calculating the Percent Differences Between the Estimates

# In[40]:


merged2018_df['abs_percent_diff_2018'] = (abs((merged2018_df[2018] - merged2018_df['tCH4_2018']))/(merged2018_df[2018] + merged2018_df["tCH4_2018"])/2)*100

merged2018_df['relative_percent_diff_2018'] = (merged2018_df[2018] - merged2018_df['tCH4_2018'])/(merged2018_df[2018])*100



# In[41]:


merged2018_df


# ### Tonnes CH4 FAOSTAT - TRACE Plot

# In[42]:


merged2018_df.plot(kind = "barh", x = 'country_fao', y = ["diff_2018"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize = (10,10))


# ### Percent Difference FAOSTAT - TRACE

# In[43]:


merged2018_df.plot(kind = "barh", x = 'country_fao', y = ["relative_percent_diff_2018"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize=(10,10))


# ## Impressions

# I was not able to replicate the results exactly.  I reviewed the included paper to find that the university misleadingly rounded to three decimal places.  I did not manipulate the raw data.  
# 
# I found that the overall difference in reporting is only about 6 percent between 2019 and 2020.   The methodology is somewhat misleading as well, because when considering the previous 5 years of data demonstrated a consistent 3 percent difference.  When comparing the TRACE data to itself it does seem to show a significant increase between 2019 and 2020 emissions. I'll test this next.
