# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()


# %% import data
df = pd.read_csv('data/new_data.csv', index_col=0)
# %% wytnij kolumne categories i zlicz wartosci
df_categories = df['categories']
df_categories = df_categories.value_counts()
# %% wykres słupkowy kolumny categories
df_categories.plot(kind='bar', legend=True, title='Categories')

# %% wykres kołowy kolumny categories
df_categories.plot(kind='pie', legend=True, title='Categories')

# %% wykres kolumny rating
df_rating = df['rating']
df_rating = df_rating.value_counts()
df_rating.sort_index().plot(kind='bar', color='red', alpha=0.7, legend=True, title='Rating')

# %% wytnij top 3 najczęsciej ocenianych z kolumny products
df_top_3_name = df[['name', 'rating']]
df_name = df_top_3_name.groupby('name').count()['rating']
df_name = df_name.nlargest(3)

df_name.plot(kind='bar')

# %% wytnij top 3 najwyżej ocenianych z kolumny products
df_top_3_high = df[['name', 'rating']]
df_mean = df_top_3_high.groupby('name').agg('mean')
top3_high = df_mean.nlargest(3, columns='rating')

# %% wytnij bottom 3 products
df_top_3_lower = df[['name', 'rating']]
df_mean_low = df_top_3_lower.groupby('name').agg('mean')
top3_lower = df_mean_low.nsmallest(3, columns='rating')