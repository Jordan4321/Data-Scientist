import numpy as np
import pandas as pd

np.random.seed(42)

# %% Połącz te dwa obiekty w jeden obiekt typu DataFrame (jako dwie kolumny) 
#    i przypisz do zmiennej df. Nadaj nazwy kolumn odpowiednio col1 oraz col2
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))
dict_s3 = {'col1':s1, 'col2':s2}
df = pd.DataFrame(dict_s3)
df
# %% Wytnij z obiektu df wiersze, dla których wartość w kolumnie col2 jest 
#    pomiędzy 0.0 a 1.0 (włącznie).
df_col2_0_1 = df.loc[(df['col2'] >= 0) & (df['col2'] <= 1)]
df_col2_0_1
# df[df['col2].between(0.0,1.0)]

# %% Przypisz nową kolumnę o nazwie col3, która przyjmie wartość 1 w momencie 
#    gdy w kolumnie col2 jest wartość nieujemna i przeciwnie -1.
df2 = pd.DataFrame({'col3':df['col2']})
df = pd.concat([df,df2], axis =1)
df['col3'] = df['col3'].where(df['col3'] >= 0, -1).where(df['col3'] < 0, 1).astype(int)
print(df)
# df['col3'] = df['col2'].map(lambda x: 1 if x >= 0 else -1)

# %% Przypisz nową kolumnę o nazwie col4, która przytnie wartości z kolumny 
#    col2 do przedziału  [−1.0,1.0] . Innymi słowy, dla wartości poniżej -1.0 
#     należy wstawić wartość -1.0, dla wartości powyżej 1.0 wartość 1.0.
df4 = pd.DataFrame({'col4':df['col2']})
df = pd.concat([df,df4], axis =1)
df['col4'] = df['col4'].where(df['col4'] >= -1, -1).where(df['col4'] < 1, 1)
print(df)
# df['col4'] = df['col2'].clip(-1.0, 1.0)

# %% Znajdź 5 największych wartości dla kolumny col2.
col_2_max_5 = df.nlargest(5, ['col2'])
col_2_max_5
# %% Znajdź 5 najmniejszych wartości dla kolumny col2.
col_2_min_5 = df.nsmallest(5, ['col2'])
col_2_min_5

# %% Wyznacz skumulowaną sumę dla każdej kolumny.
cumsum = pd.DataFrame.cumsum(df)
cumsum

# %% Wyznacz medianę dla zmiennej col2 (inaczej kwantyl rzędu 0.5).
col_2_median = df['col2'].median()
col_2_median

# %% Wytnij wiersze, dla których zmienna col2 przyjmuje wartości większe od 0.0
col2_higher_0 = df[df['col2'] > 0.0]
col2_higher_0
# df.query()

# %% Wytnij 5 pierwszych wierszy obiektu df i przekształć je do słownika.
rows_5 = df.loc[0:5]
dict_5_rows = rows_5.to_dict('series')
dict_5_rows

# %% Wytnij 5 pierwszych wierszy obiektu df, przekształć je do formatu 
#    Markdown i przypisz do zmiennej df_markdown.
rows_5 = df.loc[0:5]
df_markdown = rows_5.to_markdown()
df_markdown
# %% Wydrukuj do konsoli zawartość zmiennej df_markdown.
print(df_markdown)
