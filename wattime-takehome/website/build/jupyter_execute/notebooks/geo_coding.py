#!/usr/bin/env python
# coding: utf-8

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


# ## Shape Data

# In[2]:


gisfilepath = "/Users/jnapolitano/Projects/wattime-takehome/data/country_shapefiles/World_Countries__Generalized_.shp"


countries_df = gpd.read_file(gisfilepath)

countries_df = countries_df.to_crs(epsg=3857)


# In[3]:


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))


# In[4]:


world.rename({"iso_a3" :  'iso3_country'},axis =1,inplace=True)


# In[5]:


world


# ## FAOSTAT DATA

# In[6]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/FAOSTAT_DATA.csv"

faostat_emissions_df = pd.read_csv(filepath)
faostat_emissions_df.drop('Unnamed: 0', axis = 1 , inplace = True)
faostat_emissions_df = faostat_emissions_df[(faostat_emissions_df["country_name"] != 'Total') & (faostat_emissions_df["country_name"] != "mean")]
faostat_emissions_df.dropna(how="any", axis=1, inplace= True)


# In[7]:


faostat_emissions_df


# ### FAOSTAT Country Merge

# In[8]:


faostat_merged_df = world.merge(faostat_emissions_df, on='iso3_country', how='right', sort=True)


# In[9]:


faostat_merged_df
#trace_merged_df.dropna(axis=1, how='any')


# In[10]:


faostat_merged_df = faostat_merged_df[faostat_merged_df['continent'] != 'Antarctica'].copy()


# ### FAOSTAT Merge to File

# In[11]:


gisout = "/Users/jnapolitano/Projects/wattime-takehome/data/FAOSTAT_GEO.geojson"
faostat_merged_df.to_file(gisout, driver="GeoJSON")


# ## TRACE Data

# In[12]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/TRACE_DATA.csv"

trace_emissions_df = pd.read_csv(filepath)
trace_emissions_df.drop('Unnamed: 0', axis = 1 , inplace = True)
trace_emissions_df = trace_emissions_df[(trace_emissions_df["country_name"] != 'Total') & (trace_emissions_df["country_name"] != "mean")]


# In[13]:


trace_emissions_df


# ## TRACE Country Merge

# In[14]:


trace_merged_df = world.merge(trace_emissions_df, on='iso3_country', how='right', sort=True)


# In[15]:


trace_merged_df


# In[16]:


trace_merged_df = trace_merged_df[trace_merged_df['continent'] != 'Antarctica'].copy()


# In[17]:


trace_merged_df
#trace_merged_df.dropna(axis=1, how='any')


# ### Trace Merge to File

# In[18]:


gisout = "/Users/jnapolitano/Projects/wattime-takehome/data/TRACE_DATA_GEO.geojson"
trace_merged_df.to_file(gisout, driver="GeoJSON")


# ## Merge GEO DATA

# In[19]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/MERGED_DATA.csv"

merged_data = pd.read_csv(filepath)

merged_data.drop('Unnamed: 0', axis = 1 , inplace = True)


# In[20]:


merged_countries = world.merge(merged_data, on='iso3_country', how='right', sort=True)


# In[21]:


merged_countries


# ### Merged Countries to File

# In[22]:


gisout = "/Users/jnapolitano/Projects/wattime-takehome/data/MERGE_DATA_GEO.geojson"
merged_countries.to_file(gisout, driver="GeoJSON")


# In[ ]:




