#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Testing the University of Malaysia Paper

# ## Claims
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

# ## Data Import

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


# In[2]:


filepath = "/Users/jnapolitano/Projects/wattime-takehome/data/ch4_2015-2021.xlsx"

hypothesis_testing_df = pd.read_excel(filepath)


# ### Drop total row from the data

# In[3]:


hypothesis_testing_df = hypothesis_testing_df.loc[(hypothesis_testing_df['country_name'] != "Total")].copy() #copying to avoid modifying slices in memory.  Old df should also drop from memory in production environment.


# In[4]:


hypothesis_testing_df


# ### Test for Normality: Shapiro-Wilk

# #### 2019

# In[5]:


## Selecting Malaysia 2019 Data 
data_2019 = hypothesis_testing_df['tCH4_2019']
data_2019


# In[6]:


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

# In[7]:


## Selecting the Malaysia Data 2020
data_2020 = hypothesis_testing_df['tCH4_2020']


# In[8]:


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

# In[9]:


# Example of the Mann-Whitney U Test

stat, p = stats.mannwhitneyu(data_2019, data_2020)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# ### Kruskal Wallis test

# In[10]:


stat, p = stats.kruskal(data_2019, data_2020)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


# ### Friedman Test
# 
# Just for the sake of it I will compare data across all distributions

# In[11]:


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
