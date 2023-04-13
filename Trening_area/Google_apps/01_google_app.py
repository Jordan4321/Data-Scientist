# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


# %%
df = pd.read_csv('googleplaystore.csv')

# %% preprocessing
df.info()
df.columns = [col.replace(' ','_') for col in df.columns]
col = [col for col in df.columns]
# %% usunięcie wiersza z nie poprawnymi danymi 10472

df = df.drop(10472)
df = df.reset_index()

# %% zmiana columny reviews na int
df['Reviews'] = pd.to_numeric(df.Reviews)


# %% pogrupowanie columny categoria oraz wyswietlenie wykresu
col_cat = df.groupby('Category').size().rename('Count')
col_cat.plot(kind='bar', cmap='viridis', alpha=0.9, title='Categories')

# %% pogrupowanie type oraz wyswietlenie wykresu
type_products = df.groupby('Type').size().rename('Type_sum')
type_products.plot(kind='pie', cmap='viridis', fontsize=18)

# %% wytnij typ, gatunek i rating, pogrupuj i przeprowadz agregacje
df_1 = df[['Genres', 'Rating', 'Type']]
df_type_gp = df_1.groupby('Type').count()
df_rating_mean = df_1.groupby(['Genres','Type']).agg({'Rating':['count','mean']})

df_rating_mean.columns = ['_'.join(x) for x in df_rating_mean.columns.ravel()]

# sortowanie po kolumnie rating
df_rating_mean = df_rating_mean.sort_values('Rating_mean', ascending=False)

# wykres ratingów
df_rating_mean = df_rating_mean[df_rating_mean['Rating_count']>100]
df_rating_mean.plot(kind='bar', cmap='viridis', subplots=True)

# %% wyswietl top 5 produktów z powyzszej funkcji
top_5 = df_rating_mean.nlargest(5, columns='Rating_count')['Rating_count']
top_5.plot(kind='pie', cmap='hot')
