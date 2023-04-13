# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# %% import data
df = pd.read_csv('Consumer_Reviews_Amazon.csv')

# %%
df.describe()

# %% replace "." in columns 
for col in df.columns:
    print(col)
    
col = [str(col).replace('.','_') for col in df.columns]
df.columns = [str(col).replace('.','_') for col in df.columns]

# %% take only "name", "primaryCategories", "reviews_text" 
# and "reviews_rating" columns

df_1 = df[['name', 'primaryCategories', 'reviews_text', 'reviews_rating']]

# %% change columns names
df_1.columns = ['name', 'categories', 'text', 'rating']

df_1.info()
df_1.describe()

# %% export dataframe to csv in folder data
df_1.to_csv('data/new_data.csv')