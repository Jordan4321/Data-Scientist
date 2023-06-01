import numpy as np
import pandas as pd

np.random.seed(42)

# %% Wytnij wiersze obiektu df dla których kolumna C jest większa niż 0.8.
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df_C_0_8 = df[(df['C'] >= 0.8)]
df_C_0_8
# %% Wytnij wiersze obiektu df dla których kolumna C jest większa niż 0.3 
#    oraz kolumna D jest mniejsza niż 0.7.
df_C_D = df[(df['C'] >= 0.3) & (df['D'] <= 0.7)]
df_C_D
# %% Dokonaj iteracji po pierwszych pięciu wierszach obiektu df. 
#    Każdy wiersz wydrukuj do konsoli.
iterrows = df.head().iterrows()
for i in iterrows:
  print(i)
# for index, row in df.head().iterrows():
#    print(row)
# %% Ustaw wartość w wierszu o indeksie 3 dla kolumny B jako np.nan. Wykorzystaj df.iloc.
df.iloc[3].at['B'] = np.nan
df
# df.iloc[3, 1] = np.nan
# df.iat[3, 1] = np.nan
# df
# %% Ustaw wartość w wierszu o indeksie 8 dla kolumny D jako np.nan. Wykorzystaj df.loc.
df.loc[8].at['D'] = np.nan
df
df.loc[8, 'D'] = np.nan

# %% Usuń wszystkie wiersze z obiektu df zawierające braki danych i przypisz 
#    do zmiennej df1. Wyświetl zmienną df1.
df1 = df[~df.isnull().any(axis=1)]
df1
# df1 = df.dropna()

# %% Zresetuj indeks, aby wprowadzić kolejność. 
df1 = df1.reset_index()
df1 = df1.drop('index', axis=1)
df1
#df1 = df1.reset_index(drop=True)

# %% Wyznacz liczbę brakujących elementów w obiekcie df dla każdej kolumny.
df.isna().sum()
# df.isnull().sum()

# %% Uzupełnij brakujące wartości wartością 0 i przypisz do zmiennej df.
df = df.fillna(0)
df

# %% Zamień kolejność kolumn w obiekcie df na podaną: D, A, B, C
def swap_columns(df, col1, col2, col3, col4):
    col_list = list(df.columns)
    a, b, c, d = col_list.index(col1), col_list.index(col2), col_list.index(col3), col_list.index(col4)
    col_list[a], col_list[b], col_list[c], col_list[d] = col_list[d], col_list[a], col_list[b], col_list[c] 
    df = df[col_list]
    return df
df = swap_columns(df, 'A', 'B', 'C', 'D')
# df = df[['D','A','B','C']]

# %% Usuń kolumnę  D  z obiektu df.
df = df.drop(['D'], axis=1)
df
# del df['D']