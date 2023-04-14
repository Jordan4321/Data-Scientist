# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %% Read
df = pd.read_csv('data/btcusd_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close']
# %% Check info
df.info()
df.describe()

# %% take top-1 and bottom-1 in "Close" column
top_btc = df.nlargest(1, columns='Close')
bot_btc = df.nsmallest(1, columns='Close')
# %% take mean in "Close" column
mean = df['Close'].aggregate('mean')

# %% plot - "Open" and "Close"column from 2020 year
start_close = df[['Open', 'Close']]
start_close = start_close.loc['2020-01-01':] 
start_close.plot(cmap='viridis', alpha=0.5)

# %% 2023_year
april23 = df.loc['2023-01-01':'2023-04-01']
top23 = april23.nlargest(10, columns='Close')
mean23 = april23.mean().rename('mean')
std23 = april23.std().rename('std')
april_stats = april23.aggregate(['mean','std','max','min'])
april23_sort = april23.sort_values('Open', ascending=False) 
# %% chart 2023
april23_sort.plot(title="Chart 2023")