#!/usr/bin/env python
# coding: utf-8

# # Are We Undercounting Global Methane Emissions? (No Code Example)

# According to the United Nations Environment Program "methane is the primary contributor to the formation of ground-level ozone." Over 20 years, "it is 80 times more potent at warming than carbon dioxide." [(UNEP)](https://www.unep.org/news-and-stories/story/methane-emissions-are-driving-climate-change-heres-how-reduce-them).  In fact, one kilogram of CH4 produced is equivalent to 25 kilograms of CO2 [(Econometra)](https://ecometrica.com/assets/GHGs-CO2-CO2e-and-Carbon-What-Do-These-Mean-v2.1.pdf).  
# 
# The agricultural industry is the primary producer of methane emissions globally.  While the cattle industry is a well known culprit, paddy rice cultivation accounts for another 8 per cent of human linked emissions [(UNEP)](https://www.unep.org/news-and-stories/story/.methane-emissions-are-driving-climate-change-heres-how-reduce-them).
# 

# ## How are Rice Paddy Emissions Measured?

# Methane estimates are calcuated by multipling the hecatares of rice paddy in cultivation by a conversion factor.   
# 
# The Food and Agricultural Organization of the United Nations [(FAOSTAT)](https://www.fao.org/faostat/en/) is the most trusted provider of methane emission estimates.  The accuracy of their data however, can be questioned as the organization relies upon official government sources which may be manipulated.
# 
# Climate TRACE [(Climate TRACE)](https://www.climatetrace.org) on the other hand estimates emission levels by calculating the area of cultivated paddies with satellite imaging.   While this method may undercount small fields and cultivation at higher altitudes, the metric does not rely upon possibly manipulated sources. This should result in more accurate predictions.  
# 

# ```{note}
# It is important to note that FAOSTAT and TRACE estimate emissions with different conversion factors. 
# ```
# 

# ## Differences between FAOSTAT and TRACE Estimates.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


# ### Data Review
# 
# We will be reviewing the data provided by FAOSTAT and TRACE.  The dataframe imported was prepared for this post.  You may review the documentation [here](data_exploration_title).

# In[2]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/MERGE_DATA_GEO.geojson"

merge_geo_df = gpd.read_file(filepath)

## Convert to 3857 for easier plotting and spatial math if necessary
merge_geo_df = merge_geo_df.to_crs(epsg=3857)


# ### Methane Emissions Data 2015 - 2019 
# 

# In[3]:


ch4_data = merge_geo_df[['country_name_FAOSTAT', 'continent','CH4_abs_percent_diff_totals', 'CH4_relative_percent_diff_totals', 'CH4_diff_totals','2015', 'tCH4_2015','2016', 'tCH4_2016','2017', 'tCH4_2017','2017', 'tCH4_2017','2018', 'tCH4_2018', '2019', 'tCH4_2019']].copy()
ch4_data


# #### Methane Emissions Insights

# * FAOSTAT underestimated by about 2.8 percent in comparison to TRACE.  
# * FAOSTAT undestimated a total of 3,100,772 tonnes of methane over a 5 year period.  
# 
# Let's review the bar chart below to better understand the data.  
#  

# In[4]:


merge_geo_df.plot(kind = "barh", x = 'country_name_FAOSTAT', y = ['CH4_relative_percent_diff_2015', 'CH4_relative_percent_diff_2016','CH4_relative_percent_diff_2017', 'CH4_relative_percent_diff_2018', 'CH4_relative_percent_diff_2019','CH4_relative_percent_diff_totals'], xlabel = "Country Name", ylabel = "Tonnes CH4", title = "Relative Percent Global CH4 Emissions 2015 - 2019", figsize = (10,10))


# ### Major Differences Between FAOSTAT and TRACE for Certain Countries

# FaoSTAT methods underestimate nearly as often as they overestimate; however, large producer such as Brazil, Bangladesh, China, and India generate large amounts of emissions not considered by FAOSTAT.   
# 
# The following map illustrates these differences well. 

# In[5]:


fig, ax = plt.subplots(1, 1,figsize=(15,15))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
merge_map = merge_geo_df.plot(column='CH4_relative_percent_diff_totals', ax=ax, legend=True, cax=cax, alpha = .5,legend_kwds={'label': "Overall Percent Difference in CH4 Production in Tonnes 2015-2019 FAOSTAT",
                        'orientation': "vertical"})
cx.add_basemap(merge_map, zoom=3)


# ### FAOSTAT Under Estimation in Brazil China, India, and Bangledesh.  

# Brazil's emissions are greatly undercounted over the 5 year period. A factor greater than the difference in emission conversion factors would predict.  Rice Paddies in cultivation may be hidden from satellites by tree cover or altitude.   China, India, and Bangladesh too differ, but at a smaller scale. It is likely that the TRACE data are nearly equivalent to the FAOSTAT data for these contries.  

# ## The Case for Climate Trace Estimates

# The TRACE and the FAOSTAT methods could both erroneously estimate methane emissions.  Climate Trace's advantage is that hecatares of cultivation are estimated from satellite imaging as opposed to government reports.  The result of which is a falsifiable report supported by empirical evidence. When calculating the CO2 equivalency of CH4 emissions it is safer to use the TRACE data because the data collection methodology is rigorous. 

# ## Estimating CO2 Equivalency

# CH4 can be converted to CO2 equivalent by multiplying the 1 kilogram of CH4 by 25 [(Econometra)](https://ecometrica.com/assets/GHGs-CO2-CO2e-and-Carbon-What-Do-These-Mean-v2.1.pdf).  The dataframe below has been precalculated view the documentation [here](data_exploration_title).

# In[6]:


co2_data = merge_geo_df[['country_name_TRACE', 'continent','CO2_abs_percent_diff_totals', 'CO2_relative_percent_diff_totals', 'CO2_diff_totals','tCO2_2015_FAOSTAT','tCO2_2015_TRACE', 'tCO2_2016_FAOSTAT', 'tCO2_2016_TRACE', 'tCO2_2017_FAOSTAT', 'tCO2_2017_TRACE','tCO2_2018_FAOSTAT','tCO2_2018_TRACE', 'tCO2_2019_FAOSTAT','tCO2_2019_TRACE']].copy()


# ```{note}
# All differences are recorded as FAOSTAT - TRACE.
# ```

# ### Tonnes C02 2015 - 2019 TRACE Estimations

# In[7]:


TRACE_CO2_df = merge_geo_df[['country_name_TRACE','CO2_abs_percent_diff_totals', 'CO2_relative_percent_diff_totals', 'CO2_diff_totals','tCO2_2015_TRACE','tCO2_2016_TRACE','tCO2_2017_TRACE','tCO2_2018_TRACE','tCO2_2019_TRACE']].copy()
TRACE_CO2_df['Means'] = TRACE_CO2_df.select_dtypes(np.number).mean(axis=1)
TRACE_CO2_df['Totals'] = TRACE_CO2_df[['country_name_TRACE','tCO2_2015_TRACE','tCO2_2016_TRACE','tCO2_2017_TRACE','tCO2_2018_TRACE','tCO2_2019_TRACE']].select_dtypes(np.number).sum(axis=1)
TRACE_CO2_df


# ```{note}
# Note a mean of 561,637,600 tonnes CO2equiv produced between annualy 2015 - 2019.
# ```

# #### CO2 Data Insights
# 
# * Total difference in 3,370,404 tonnes of CO2equiv between the FAOSTAT and TRACE data.
# * TRACE reports 2,808,188,000 Tonnes of CO2equiv produced between 2015 to 2019.
# * There is a relative percent difference of -2.8 percent.
# 

# In[8]:


TRACE_CO2_df.plot(kind = "barh", x = 'country_name_TRACE', y = ['tCO2_2015_TRACE','tCO2_2016_TRACE','tCO2_2017_TRACE','tCO2_2018_TRACE','tCO2_2019_TRACE',], xlabel = "Country Name", ylabel = "Tonnes C02", title = "Global Tonnes CO2 Emissions 2015 - 2019", figsize = (10,10))


# #### The Worst Offenders are the Most Dependent on Rice Cultivation

# The worst offenders are China, India, and Bangladesh.  These states struggle with feeding their massive populations.  Including CO2equiv in carbon goals may harm the people of these countries.  

# In[9]:


fig, ax = plt.subplots(1, 1,figsize=(15,15))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
merge_map = merge_geo_df.plot(column='Total_CO2_TRACE', ax=ax, legend=True, cax=cax, alpha = .5,legend_kwds={'label':  "Tonnes CO2 TRACE 2015-2019",
                        'orientation': "vertical"})
cx.add_basemap(merge_map, zoom=3)


# ```{note}
# Values in billions.
# ```

# ## Conclusions
# 
# ### FAOSTAT Likely Undercounts Emissions
# 
# The TRACE data set on average reports about 2.8 percent more methane emissions than the FAOSTAT data set.  This equates to a total methane emmissions estimates difference of 3,100,772 tonnes over a 5 year period.  The CO2equiv over that same period is 77,519,300 tonnes.  Neither value is negligible.  
# 
# ### Countries Should Attempt to Reduce Methane Emssions
# 
# The 20 and 100 year warming potentials for methane emsission are 84 and 28 [(WG1AR5_Chapter08, Pg 73)].  These factors will impact our climate if nothing is done.  Unfortunately, the countries that produce the most methane from rice cultivation are also those most dependent on the grain.  To make the change, realistic solutions must be provided to feed people culturally and geographically dependent on rice cultivation.    
# 

# In[ ]:




