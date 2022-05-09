#!/usr/bin/env python
# coding: utf-8

# # Emissions Estimation Data: A Comparison between FAOSTAT and University of Malysia Estimates

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import contextily as cx
from shapely.geometry import Point, LineString, Polygon
import numpy as np
from scipy.spatial import cKDTree
from geopy.distance import distance
import scipy.stats as stats


# ### Dependencies 
# 
# * Geopandas
# * pandas
# * openpyxl

# ## Plan
# 
# ### Data Imports
# 
# * /Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx
# * /Users/jnapolitano/Projects/wattime-takehome/data/emissions_csv_fao_emiss_csv_ch4_fao_2015_2019_tonnes.xlsx
# 
# ### Import Data Frames
# Since jupyter caches the data to the notebook json I can import the dataframes that I will be using together.
# 
# If I were to build automated scripts to perform the analysis I would only load the data necessary to perform a process. 
# 
# ### Experiment with Plots for each Set
# I don't know exactly which plots I want to include in the final report. 
# 
# I 'll plot a few for each data set 
# 
# ### Calculate differences between the datasets
# * create a differences data frame
# * write to file for use
# * plot
# 
# 

# ## University of Malaysia Emission Estimates

# In[2]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx"

malaysia_emissions_df = pd.read_excel(filepath)


# ### Print Df Head

# In[3]:


malaysia_emissions_df


# ### Calculate Co2 Equivalency

# In[4]:


malaysia_emissions_df['tCO2_2015'] = (malaysia_emissions_df['tCH4_2015'] * 25)
malaysia_emissions_df['tCO2_2016'] = (malaysia_emissions_df['tCH4_2016'] * 25)
malaysia_emissions_df['tCO2_2017'] = (malaysia_emissions_df['tCH4_2017'] * 25)
malaysia_emissions_df['tCO2_2018'] = (malaysia_emissions_df['tCH4_2018'] * 25)
malaysia_emissions_df['tCO2_2019'] = (malaysia_emissions_df['tCH4_2019'] * 25)


# ### Calculate Means 

# In[5]:


malaysia_emissions_df.loc['mean'] = malaysia_emissions_df.loc[(malaysia_emissions_df['country_name'] != "Total")].select_dtypes(np.number).mean()
malaysia_emissions_df.at['mean','country_name'] = 'mean'
malaysia_emissions_df


# # Calculate Means and Totals Across Rows

# In[6]:


mean_series = malaysia_emissions_df[['tCH4_2015','tCH4_2016','tCH4_2017','tCH4_2018','tCH4_2019']].select_dtypes(np.number).mean(axis=1)
total_series = malaysia_emissions_df[['tCH4_2015','tCH4_2016','tCH4_2017','tCH4_2018','tCH4_2019']].select_dtypes(np.number).sum(axis=1)
malaysia_emissions_df["Mean_CH4"] = mean_series
malaysia_emissions_df['Total_CH4'] = total_series 


# In[7]:


## the select np.number is uncecessary, but i'm including anyways as it doesnt really hurt but for a small calculation penalty
mean_series = malaysia_emissions_df[['tCO2_2015','tCO2_2016','tCO2_2017','tCO2_2018','tCO2_2019']].select_dtypes(np.number).mean(axis=1)
total_series = malaysia_emissions_df[['tCO2_2015','tCO2_2016','tCO2_2017','tCO2_2018','tCO2_2019']].select_dtypes(np.number).sum(axis=1)
malaysia_emissions_df["Mean_CO2"] = mean_series
malaysia_emissions_df['Total_CO2'] = total_series 


# In[8]:


malaysia_emissions_df.reset_index(inplace=True, drop = True)


# In[9]:


malaysia_emissions_df


# ### Write Data to File

# In[10]:


outfile = "/Users/jnapolitano/Projects/wattime-takehome/data/TRACE_DATA.csv"

malaysia_emissions_df.to_csv(outfile)


# ### Plots

# #### University of Malaysia Bar Plot

# In[11]:


malaysia_emissions_df.plot(kind = "barh", x = 'country_name', xlabel = "Country Name", ylabel = "CH4 Tonnes", figsize = (10,5))


# #### University of Malaysia Density Plot

# In[12]:


malaysia_emissions_df.plot(rot = 0, kind = "density", figsize = (15,5)) 


# I did not exclude totals or mean from the dataframe, but as we can see the second hump in the density graph shows the distribution of totals annualy.  Interestingly the 2020 data is shifted further to the right than other years.  This actually questions the validity of the study promoted by the University of malaysia

# ## FAOSTAT Data 

# In[13]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/emissions_csv_fao_emiss_csv_ch4_fao_2015_2019_tonnes.xlsx"

faostat_emissions_df = pd.read_excel(filepath)


# ### Print FAOSTAT Data

# In[14]:


## I didn't write the index to the csv file in the previous step.  IF time permits go back and fix this error
faostat_emissions_df


# #### Change code to iso3_country

# In[15]:



faostat_emissions_df.rename(columns={"code": "iso3_country"}, inplace =True)
faostat_emissions_df.rename(columns={"country": "country_name"}, inplace =True)
# The column title is not a string.  It is understood as an int or a datetime.  
#faostat_emissions_df['2015']
faostat_emissions_df


# #### Set country_name total to total

# In[16]:


faostat_emissions_df.at[23,'country_name'] = 'Total'


# ### Drop Fao Country Code

# In[17]:


faostat_emissions_df.drop(labels = ['country_fao'], axis=1, inplace=True)
faostat_emissions_df


# ### Calculate Co2 Equivalency

# In[18]:


faostat_emissions_df['tCO2_2015'] = faostat_emissions_df[2015] * 25
faostat_emissions_df['tCO2_2016'] = faostat_emissions_df[2016] * 25
faostat_emissions_df['tCO2_2017'] = faostat_emissions_df[2017] * 25
faostat_emissions_df['tCO2_2018'] = faostat_emissions_df[2018] * 25
faostat_emissions_df['tCO2_2019'] = faostat_emissions_df[2019] * 25


# ### Calculate Means

# In[19]:


faostat_emissions_df.loc['mean'] = faostat_emissions_df.loc[(faostat_emissions_df['country_name'] != "Total")].select_dtypes(np.number).mean()
faostat_emissions_df.at['mean','country_name'] = 'mean'
faostat_emissions_df.reset_index(inplace=True, drop=True)
#faostat_emissions_df.at['mean','country_fao'] = 'mean'


# ### Calculate Means and Totals Across Rows

# In[20]:


mean_series = faostat_emissions_df[[2015,2016,2017,2018,2019]].select_dtypes(np.number).mean(axis=1)
total_series = faostat_emissions_df[[2015,2016,2017,2018,2019]].select_dtypes(np.number).sum(axis=1)
faostat_emissions_df["Mean_CH4"] = mean_series
faostat_emissions_df['Total_CH4'] = total_series 


# In[21]:


## the select np.number is uncecessary, but i'm including anyways as it doesnt really hurt but for a small calculation penalty
mean_series = faostat_emissions_df[['tCO2_2015','tCO2_2016','tCO2_2017','tCO2_2018','tCO2_2019']].select_dtypes(np.number).mean(axis=1)
total_series = faostat_emissions_df[['tCO2_2015','tCO2_2016','tCO2_2017','tCO2_2018','tCO2_2019']].select_dtypes(np.number).sum(axis=1)
faostat_emissions_df["Mean_CO2"] = mean_series
faostat_emissions_df['Total_CO2'] = total_series 


# In[22]:


faostat_emissions_df.reset_index(inplace=True, drop=True)


# In[23]:


faostat_emissions_df


# ### FAOSTAT Data to File

# In[24]:


outfile = "/Users/jnapolitano/Projects/wattime-takehome/data/FAOSTAT_DATA.csv"

faostat_emissions_df.to_csv(outfile)


# ### FaoSTAT PLOTS

# #### FAOSTAT Hectare Estimates Bar Plot

# In[25]:


faostat_emissions_df.plot(kind = "barh", x = 'country_name', y = [2015, 2016, 2017, 2018, 2019], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize = (10,5))


# ### FAOSTAT Density Plot

# In[26]:


faostat_emissions_df.plot(rot = 90, kind = "density",y = [2015, 2016, 2017, 2018, 2019], figsize = (15,5)) 


# The density plot is fairly consistent.  There is nearly no variation between nations and in total.  The 2020 data may show otherwise as the Malaysian data shows.  

# ## Join Df's by ISO3 Country

# ### Drop totals and means from the original df.
# 
# Because I am joining on iso3 country country code if the totals and means are located at different indexes we may experience merge and calculation errors

# In[27]:


faostat_emissions_df = faostat_emissions_df[(faostat_emissions_df["country_name"] != "Total") & (faostat_emissions_df['country_name'] != 'mean')].copy()


# In[28]:


malaysia_emissions_df = malaysia_emissions_df[(malaysia_emissions_df["country_name"] != "Total") & (malaysia_emissions_df['country_name'] != 'mean')].copy()


# In[29]:


faostat_emissions_df


# In[30]:


malaysia_emissions_df


# In[31]:


merged_df = faostat_emissions_df.merge(malaysia_emissions_df,suffixes=('_FAOSTAT', '_TRACE'), on='iso3_country', how='left', sort=False)


# ### Dropping 2020 and 2021 from the data sets

# I will only compare data compiled from the same year. 

# In[32]:


merged_df.drop([2020, 2021, "tCH4_2020","tCH4_2021"], axis = 1, inplace = True)


# In[33]:


merged_df


# ### Calculate difference in Ch4 Tonnes Between the Estimates

# In[34]:


# Calculate Difference in tons
merged_df['CH4_diff_2015'] = merged_df[2015] - merged_df['tCH4_2015']
merged_df['CH4_diff_2016'] = merged_df[2016] - merged_df['tCH4_2016']
merged_df['CH4_diff_2017'] = merged_df[2017] - merged_df['tCH4_2017']
merged_df['CH4_diff_2018'] = merged_df[2018] - merged_df['tCH4_2018']
merged_df['CH4_diff_2019'] = merged_df[2019] - merged_df['tCH4_2019']
merged_df['CH4_diff_means'] = merged_df['Mean_CH4_FAOSTAT'] - merged_df['Mean_CH4_TRACE']
merged_df['CH4_diff_totals'] = merged_df['Total_CH4_FAOSTAT'] - merged_df['Total_CH4_TRACE']


# In[35]:


merged_df


# ### Calculate difference in C02 Tonnes Between the Estimates

# In[36]:


# Calculate Difference in tons
merged_df['CO2_diff_2015'] = merged_df['tCO2_2015_FAOSTAT'] - merged_df['tCO2_2015_TRACE']
merged_df['CO2_diff_2016'] = merged_df['tCO2_2016_FAOSTAT'] - merged_df['tCO2_2016_TRACE']
merged_df['CO2_diff_2017'] = merged_df['tCO2_2017_FAOSTAT'] - merged_df['tCO2_2017_TRACE']
merged_df['CO2_diff_2018'] = merged_df['tCO2_2018_FAOSTAT'] - merged_df['tCO2_2018_TRACE']
merged_df['CO2_diff_2019'] = merged_df['tCO2_2019_FAOSTAT'] - merged_df['tCO2_2019_TRACE']
merged_df['CO2_diff_means'] = merged_df['Mean_CO2_FAOSTAT'] - merged_df['Mean_CO2_TRACE']
merged_df['CO2_diff_totals'] = merged_df['Total_CO2_FAOSTAT'] - merged_df['Total_CO2_TRACE']


# ### Calculating the CH4 Percent Differences Between the Estimates

# In[37]:


## Calculate Percent Differnces on this data set )*100
# With raw data i could have accomplished this with a groupby.aggregate(lambda x ), however the pivot tables given are not easy to apply #vectorized functions across time series
merged_df['CH4_abs_percent_diff_2015'] = ((abs(merged_df[2015] - merged_df['tCH4_2015']))/((merged_df[2015] + merged_df['tCH4_2015'])/2))*100
merged_df['CH4_abs_percent_diff_2016'] = ((abs((merged_df[2016] - merged_df['tCH4_2016']))/((merged_df[2016] + merged_df['tCH4_2016'])/2)))*100
merged_df['CH4_abs_percent_diff_2017'] = ((abs(merged_df[2017] - merged_df['tCH4_2017']))/((merged_df[2017] + merged_df['tCH4_2017'])/2))*100
merged_df['CH4_abs_percent_diff_2018'] = (abs((merged_df[2018] - merged_df['tCH4_2018']))/((merged_df[2018] + merged_df['tCH4_2018'])/2))*100
merged_df['CH4_abs_percent_diff_2019'] = (abs((merged_df[2019] - merged_df['tCH4_2019']))/((merged_df[2019] + merged_df['tCH4_2019'])/2))*100
merged_df['CH4_abs_percent_diff_means'] = (abs((merged_df['Mean_CH4_FAOSTAT'] - merged_df['Mean_CH4_TRACE']))/((merged_df['Mean_CH4_FAOSTAT'] + merged_df['Mean_CH4_TRACE'])/2))* 100
merged_df['CH4_abs_percent_diff_totals'] = (abs((merged_df['Total_CH4_FAOSTAT'] - merged_df['Total_CH4_TRACE']))/((merged_df['Total_CH4_TRACE'] + merged_df['Total_CH4_FAOSTAT'])/2))*100


merged_df['CH4_relative_percent_diff_2015'] = ((merged_df[2015] - merged_df['tCH4_2015'])/(merged_df[2015]))*100
merged_df['CH4_relative_percent_diff_2016'] = ((merged_df[2016] - merged_df['tCH4_2016'])/(merged_df[2016]))*100
merged_df['CH4_relative_percent_diff_2017'] = ((merged_df[2017] - merged_df['tCH4_2017'])/(merged_df[2017]))*100
merged_df['CH4_relative_percent_diff_2018'] = ((merged_df[2018] - merged_df['tCH4_2018'])/(merged_df[2018]))*100
merged_df['CH4_relative_percent_diff_2019'] = ((merged_df[2019] - merged_df['tCH4_2019'])/(merged_df[2019]))*100
merged_df['CH4_relative_percent_diff_means'] = ((merged_df['Mean_CH4_FAOSTAT'] - merged_df['Mean_CH4_TRACE'])/(merged_df["Mean_CH4_FAOSTAT"]))*100
merged_df['CH4_relative_percent_diff_totals'] = ((merged_df['Total_CH4_FAOSTAT'] - merged_df['Total_CH4_TRACE'])/(merged_df["Total_CH4_FAOSTAT"]))*100


# ### Calculate CO2 Differences 

# In[38]:


## Calculate Percent Differnces on this data set )*100
# With raw data i could have accomplished this with a groupby.aggregate(lambda x ), however the pivot tables given are not easy to apply #vectorized functions across time series
merged_df['CO2_abs_percent_diff_2015'] = (abs((merged_df['tCO2_2015_FAOSTAT'] - merged_df['tCO2_2015_TRACE']))/((merged_df['tCO2_2015_TRACE'] + merged_df['tCO2_2015_FAOSTAT'])/2))*100
merged_df['CO2_abs_percent_diff_2016'] = ((abs(merged_df['tCO2_2016_FAOSTAT'] - merged_df['tCO2_2016_TRACE']))/((merged_df['tCO2_2016_TRACE'] + merged_df['tCO2_2016_FAOSTAT'])/2))*100
merged_df['CO2_abs_percent_diff_2017'] = ((abs(merged_df['tCO2_2017_FAOSTAT'] - merged_df['tCO2_2017_TRACE']))/((merged_df['tCO2_2017_TRACE'] + merged_df['tCO2_2017_FAOSTAT'])/2))*100
merged_df['CO2_abs_percent_diff_2018'] = ((abs(merged_df['tCO2_2018_FAOSTAT'] - merged_df['tCO2_2018_TRACE']))/((merged_df['tCO2_2018_TRACE'] + merged_df['tCO2_2018_FAOSTAT'])/2))*100
merged_df['CO2_abs_percent_diff_2019'] = ((abs(merged_df['tCO2_2019_FAOSTAT'] - merged_df['tCO2_2019_TRACE']))/((merged_df['tCO2_2019_TRACE'] + merged_df['tCO2_2019_FAOSTAT'])/2))*100
merged_df['CO2_abs_percent_diff_means'] = ((abs(merged_df['Mean_CO2_FAOSTAT'] - merged_df['Mean_CO2_TRACE']))/((merged_df['Mean_CO2_FAOSTAT'] + merged_df['Mean_CO2_TRACE'])/2))* 100
merged_df['CO2_abs_percent_diff_totals'] = ((abs(merged_df['Total_CO2_FAOSTAT'] - merged_df['Total_CO2_TRACE']))/((merged_df['Total_CO2_TRACE'] + merged_df['Total_CO2_FAOSTAT'])/2))*100


merged_df['CO2_relative_percent_diff_2015'] = ((merged_df['tCO2_2015_FAOSTAT']  - merged_df['tCO2_2015_TRACE'])/(merged_df['tCO2_2015_FAOSTAT']))*100
merged_df['CO2_relative_percent_diff_2016'] = ((merged_df['tCO2_2016_FAOSTAT']  - merged_df['tCO2_2016_TRACE'])/(merged_df['tCO2_2016_FAOSTAT']))*100
merged_df['CO2_relative_percent_diff_2017'] = ((merged_df['tCO2_2017_FAOSTAT']  - merged_df['tCO2_2017_TRACE'])/(merged_df['tCO2_2017_FAOSTAT']))*100
merged_df['CO2_relative_percent_diff_2018'] = ((merged_df['tCO2_2018_FAOSTAT']  - merged_df['tCO2_2018_TRACE'])/(merged_df['tCO2_2018_FAOSTAT']))*100
merged_df['CO2_relative_percent_diff_2019'] = ((merged_df['tCO2_2019_FAOSTAT']  - merged_df['tCO2_2019_TRACE'])/(merged_df['tCO2_2019_FAOSTAT']))*100
merged_df['CO2_relative_percent_diff_means'] = ((merged_df["Mean_CO2_FAOSTAT"] - merged_df['Mean_CO2_TRACE'])/(merged_df["Mean_CO2_FAOSTAT"]))*100
merged_df['CO2_relative_percent_diff_totals'] = ((merged_df['Total_CO2_FAOSTAT'] - merged_df['Total_CO2_TRACE'])/(merged_df["Total_CO2_FAOSTAT"]))*100


# In[39]:


merged_df


# ### Recalculate Means

# In[40]:


merged_df.loc['mean'] = merged_df.select_dtypes(np.number).mean()


# In[41]:


merged_df.at['mean','country_name_FAOSTAT'] = 'mean'
merged_df.at['mean','country_name_TRACE'] = 'mean'


# In[42]:


merged_df


# ### Recalculate Totals

# In[43]:


merged_df.loc['total'] = merged_df[merged_df['country_name_FAOSTAT'] != 'mean'].select_dtypes(np.number).sum()


# In[44]:


merged_df.at['total','country_name_FAOSTAT'] = 'total'
merged_df.at['total','country_name_TRACE'] = 'total'


# In[45]:


merged_df.reset_index(inplace=True, drop = True)


# In[46]:


merged_df


# ### Merged Data to File

# In[47]:


outfile = "/Users/jnapolitano/Projects/wattime-takehome/data/MERGED_DATA.csv"

merged_df.to_csv(outfile)


# ### CO2 Difference Plots

# In[48]:


merged_df.plot(kind = "barh", x = 'country_name_FAOSTAT', y = ["CO2_diff_2015", "CO2_diff_2016",	"CO2_diff_2017", "CO2_diff_2018", "CO2_diff_2019"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize = (10,10))


# ### Percent Difference Plot

# In[49]:


merged_df.plot(kind = "barh", x = 'country_name_FAOSTAT', y = ["CO2_relative_percent_diff_2015", "CO2_relative_percent_diff_2016",	"CO2_relative_percent_diff_2017", "CO2_relative_percent_diff_2018", "CO2_relative_percent_diff_2019"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize=(10,10))


# ### Impressions

# #### Initial 
# 
# The percent difference and the tonnege difference do not support each other.  I need to recalculate the totals section to ensure that we are doing things correctly.  
# 
# I need to confirm the values, but I'm initially impressed by the fact that the faostat data reports higher values than the malaysia data on average.  According to the included paper this shold not be the case.  
# 
# The quote included below states the problems with the malysia methodology.  
# 
# "The difference between harvested rice cultivation area from statistical data and remote-sensing estimates can be due to two factors: (i) MODIS data which have moderate spatial resolution lead to mixed pixels, where rice fields and non-rice fields are combined. This can overestimate area, especially in lowland regions and have a low ability to detect small rice field patches in upland regions (Frolking et al 1999, Seto et al 2000); and (ii) political and policy factors (Yan et al., 2019) such as determination of the amount of subsidies for fertilizers and evaluation of achievement of government programs in the agricultural sector.
# Other factors that contribute to discrepancy in CH4 emission are from different emission and scale factors that are related to water regime and organic amendment. These values give high uncertainty since the availability of these data are limited and quite variable."

# #### Verified
# 
# I calculated differences totals and means per dataframe to ensure accuracy prior to the join.  I also dropped precalcuated values when joining to ensure that the aggregation algorithms to not modify the results. 
# 
# The data is now consistent and supports the findings of the University of Malaysia Paper  

# ## Recreating the Malysia Paper.  

# ### University of Malaysia Data

# In[50]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx"

malaysia_emissions_df = pd.read_excel(filepath)


# In[51]:


# Selecting 2020 columns
malaysia_2020 = malaysia_emissions_df[["iso3_country","country_name", "tCH4_2020"]].copy()


# In[52]:


malaysia_2020


# ## FAOSTAT Data 2019

# In[53]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/emissions_csv_fao_emiss_csv_ch4_fao_2015_2019_tonnes.xlsx"

faostat_emissions_df = pd.read_excel(filepath)


# In[54]:


faostat_2019 = faostat_emissions_df[['code', 'country', 'country_fao', 2019]].copy()


# In[55]:


faostat_2019


# In[56]:


faostat_2019.rename(columns={"code": "iso3_country"}, inplace =True)


# ## Merging Data on Iso3 Country Code

# In[57]:


merged2020_df = faostat_2019.merge(malaysia_2020, on='iso3_country', how='left', sort=False)


# In[58]:


merged2020_df


# ### Calculate difference in Tonnes Between the Estimates

# In[59]:


# Calculate Difference in tons
merged2020_df['diff_2020'] = merged2020_df[2019] - merged2020_df['tCH4_2020']



# ### Calculating the Percent Differences Between the Estimates

# In[60]:


merged2020_df['abs_percent_diff_2020'] = (abs((merged2020_df[2019] - merged2020_df['tCH4_2020']))/(merged2020_df[2019] + merged2020_df["tCH4_2020"])/2)*100

merged2020_df['relative_percent_diff_2020'] = (merged2020_df[2019] - merged2020_df['tCH4_2020'])/(merged2020_df[2019])*100


# In[61]:


merged2020_df


# ### Tonnes CH4 FAOSTAT - TRACE Plot

# In[62]:


merged2020_df.plot(kind = "barh", x = 'country_fao', y = ["diff_2020"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize = (10,10))


# ### Percent Difference FAOSTAT - TRACE

# In[63]:


merged2020_df.plot(kind = "barh", x = 'country_fao', y = ["relative_percent_diff_2020"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize=(10,10))


# ## Recreating the Malysia Paper with 2018 Data.  

# ### University of Malaysia Data

# In[64]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx"

malaysia_emissions_df = pd.read_excel(filepath)


# In[65]:


# Selecting 2020 columns
malaysia_2020 = malaysia_emissions_df[["iso3_country","country_name", "tCH4_2020"]].copy()


# In[66]:


malaysia_2020


# ## FAOSTAT Data 2018

# In[67]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/emissions_csv_fao_emiss_csv_ch4_fao_2015_2019_tonnes.xlsx"

faostat_emissions_df = pd.read_excel(filepath)


# In[68]:


faostat_2018 = faostat_emissions_df[['code', 'country', 'country_fao', 2018]].copy()


# In[69]:


faostat_2018


# In[70]:


faostat_2018.rename(columns={"code": "iso3_country"}, inplace =True)


# ## Merging Data on Iso3 Country Code

# In[71]:


merged2020_df = faostat_2018.merge(malaysia_2020, on='iso3_country', how='left', sort=False)


# In[72]:


merged2020_df


# ### Calculate difference in Tonnes Between the Estimates

# In[73]:


# Calculate Difference in tons
merged2020_df['diff_2020'] = merged2020_df[2018] - merged2020_df['tCH4_2020']



# ### Calculating the Percent Differences Between the Estimates

# In[74]:


merged2020_df['abs_percent_diff_2020'] = (abs((merged2020_df[2018] - merged2020_df['tCH4_2020']))/(merged2020_df[2018] + merged2020_df["tCH4_2020"])/2)*100

merged2020_df['relative_percent_diff_2020'] = (merged2020_df[2018] - merged2020_df['tCH4_2020'])/(merged2020_df[2018])*100


# In[75]:


merged2020_df


# ### Tonnes CH4 FAOSTAT - TRACE Plot

# In[76]:


merged2020_df.plot(kind = "barh", x = 'country_fao', y = ["diff_2020"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize = (10,10))


# ### Percent Difference FAOSTAT - TRACE

# In[77]:


merged2020_df.plot(kind = "barh", x = 'country_fao', y = ["relative_percent_diff_2020"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize=(10,10))


# ## Recreating the Malysia Paper same year

# ### University of Malaysia Data

# In[78]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx"

malaysia_emissions_df = pd.read_excel(filepath)


# In[79]:


# Selecting 2020 columns
malaysia_2018 = malaysia_emissions_df[["iso3_country","country_name", "tCH4_2018"]].copy()


# In[80]:


malaysia_2018


# ## FAOSTAT Data 2018

# In[81]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/emissions_csv_fao_emiss_csv_ch4_fao_2015_2019_tonnes.xlsx"

faostat_emissions_df = pd.read_excel(filepath)


# In[82]:


faostat_2018 = faostat_emissions_df[['code', 'country', 'country_fao', 2018]].copy()


# In[83]:


faostat_2018


# In[84]:


faostat_2018.rename(columns={"code": "iso3_country"}, inplace =True)


# ## Merging Data on Iso3 Country Code

# In[85]:


merged2018_df = faostat_2018.merge(malaysia_2018, on='iso3_country', how='left', sort=False)


# In[86]:


merged2018_df


# ### Calculate difference in Tonnes Between the Estimates

# In[87]:


# Calculate Difference in tons
merged2018_df['diff_2018'] = merged2018_df[2018] - merged2018_df['tCH4_2018']



# ### Calculating the Percent Differences Between the Estimates

# In[88]:


merged2018_df['abs_percent_diff_2018'] = (abs((merged2018_df[2018] - merged2018_df['tCH4_2018']))/(merged2018_df[2018] + merged2018_df["tCH4_2018"])/2)*100

merged2018_df['relative_percent_diff_2018'] = (merged2018_df[2018] - merged2018_df['tCH4_2018'])/(merged2018_df[2018])*100


# In[89]:


merged2018_df


# ### Tonnes CH4 FAOSTAT - TRACE Plot

# In[90]:


merged2018_df.plot(kind = "barh", x = 'country_fao', y = ["diff_2018"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize = (10,10))


# ### Percent Difference FAOSTAT - TRACE

# In[91]:


merged2018_df.plot(kind = "barh", x = 'country_fao', y = ["relative_percent_diff_2018"], xlabel = "Country Name", ylabel = "Tonnes CH4", figsize=(10,10))


# ### Impressions

# I was not able to replicate the results exactly.  I reviewed the included paper to find that the university misleadingly rounded to three decimal places.  I did not manipulate the raw data.  
# 
# I found that the overall difference in reporting is only about 6 percent between 2019 and 2020.   The methodology is somewhat misleading as well, because when considering the previous 5 years of data demonstrated a consistent 3 percent difference.  When comparing the TRACE data to itself it does seem to show a significant increase between 2019 and 2020 emissions. I'll test this next  

# ## Hypothesis Testing the Malaysian Data

# ### Claims
# 
# * That the distributions do not differ between 2020 and 2019
# * That the means do no differ between 2020 and 2019

# ## What will be testing.  
# 
# * That the Data are independent and evenly distributed: Test for normality
#     * Shapiro-Wilk Test
# * That the means between 2019 and 2020 do not differ: Parametric Statistical Hypothesis Tests
#     * T Test because we have less than 25 observations
# * If nonparametirc: That the distributions between 2019 and 2020 do not differ
#     Mann-Whitney U Test
# 
# 

# ### Data Import
# I am importing data again to ensure that our data is valid.  I will move this section to another notebook when the work is completed.  This file must be very large at this point.

# In[92]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx"

hypothesis_testing_df = pd.read_excel(filepath)


# ### Drop total row from the data

# In[93]:


hypothesis_testing_df = hypothesis_testing_df.loc[(hypothesis_testing_df['country_name'] != "Total")].copy() #copying to avoid modifying slices in memory.  Old df should also drop from memory in production environment.


# In[94]:


hypothesis_testing_df


# ### Test for Normality: Shapiro-Wilk

# #### 2019

# In[95]:


## Selecting Malaysia 2019 Data 
data_2019 = hypothesis_testing_df['tCH4_2019']
data_2019


# In[96]:


results = stats.shapiro(data_2019)
print('stat=%.3f, p=%.3f' % (results.statistic, results.pvalue))
if results.pvalue > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')


# ##### Results
# 
# The distribution is not gausian so a non-paremtric test must be completed.  It is not necessary to perform this test on the 2020 data, but I will do so anyways for practice.

# #### 2020

# In[97]:


## Selecting the Malaysia Data 2020
data_2020 = hypothesis_testing_df['tCH4_2020']


# In[98]:


results = stats.shapiro(data_2020)
print('stat=%.3f, p=%.3f' % (results.statistic, results.pvalue))
if results.pvalue > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')


# ##### Results
# 
# The 2020 data is not gausian which verifies that we will need to perform a non parmetric test

# ### Independence of Samples.  
# We have to assume that the samples are independent of each other as we know they are dependent on hecatares.  
# Though the correlations are rather high this is due to the smiliarity of hectares per year.  Thus the amount of ch4 is similiar
# 

# ### Distribution Similiarity

# #### Mann-Whitney U Test

# In[99]:


# Example of the Mann-Whitney U Test

stat, p = stats.mannwhitneyu(data_2019, data_2020)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# ### Kruskal Wallis test

# In[100]:



stat, p = stats.kruskal(data_2019, data_2020)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# ### Friedman Test
# 
# Just for the sake of it I will compare data across all distributions

# In[101]:


# Example of the Friedman Test
#data_2014 = hypothesis_testing_df['tCH4_2014']
data_2015 = hypothesis_testing_df['tCH4_2015']
data_2016 = hypothesis_testing_df['tCH4_2016']
data_2017 = hypothesis_testing_df['tCH4_2017']
data_2018 = hypothesis_testing_df['tCH4_2018']

stat, p = stats.friedmanchisquare(data_2015, data_2016, data_2017, data_2018, data_2019, data_2020)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# #### Results.  
# 
# Some distributions differ from one another.  Which those are have yet to be discovered.  For the sake of this analysis I will not attempt to identify them.  
# 
# The statment that the distributions of the 2019 and 2020 data do not differ cannot differ.  That said we also cannot claim that the means are statistically equivalent as the data is not parametric.  
# 
# 
