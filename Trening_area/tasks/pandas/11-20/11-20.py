import pandas as pd
import numpy as np

# %% Zbuduj obiekt DatetimeIndex zawierający daty w formacie 'yyyy-mm-dd' 
# dla wszystkich dni ze stycznia 2020 roku i przypisz do zmiennej date_range.
date_range = pd.date_range(start = '2020-01-01', periods=31)
print(date_range)
# Ze zmiennej date_range zbuduj obiekt typu Series.
date_series = pd.Series(date_range)
print(date_series)

# %% Zbuduj obiekt DatetimeIndex zawierający daty w formacie 'yyyy-mm-dd' 
# dla wszystkich poniedziałków z 2020 roku i przypisz do zmiennej date_range.
date_range = pd.date_range(start='2020-01-01', end='2020-12-01', freq='W-MON')
date_range

# %% Zbuduj obiekt DatetimeIndex zawierający daty w formacie 'yyyy-mm-dd hh:mm:ss'
# dla 1 stycznia 2021 roku z odstępem czasowym 1h i przypisz do zmiennej date_range.

date_range = pd.date_range(start='2021-01-01 00:00:00', end='2021-01-02', freq='H')
date_range

# %% Zbuduj poniższy obiekt DataFrame w którym :
#    Kolumna day zawiera daty od 01 marca 2021 do 31 marca 2021. 
#    Kolumna day_of_year to numer dnia w całym roku.
date_2021 = pd.date_range(start='2021-03-01', end='2021-03-31')
df = pd.DataFrame({
    'day':[date_2021],
    'day_of_year':[date_2021.day_of_year]
    })
df

# %% Zbuduj z tego słownika obiekt DateFrame. Dodatkowo jako indeks dodaj datę 
# od 2020-01-01 i przypisz do zmiennej df.
data_dict = {
    'normal': np.random.normal(loc=0, scale=1, size=1000),
    'uniform': np.random.uniform(low=0, high=1, size=1000),
    'binomial': np.random.binomial(n=1, p=0.2, size=1000)
}
df = pd.DataFrame(data_dict).set_index(pd.date_range(start='2020-01-01', periods=1000))
df

# %% Wyświetl 10 pierwszych wierszy obiektu df z poprzedniego ćwiczenia.
df.head(10)
# %% Wyświetl 8 ostatnich wierszy obiektu df z poprzedniego ćwiczenia.
df.tail(8)

# %% Wyświetl podstawowe informacje o obiekcie df (liczba wierszy, liczba kolumn, typ zmiennych).
df.info()
# %% Wyświetl podstawowe statystyki obiektu df (wartość średnia, odchylenie, min, max, mediana).
df.describe()

# %% Używając meteody pd.DataFrame.plot zbuduj histogramy dla kolejnych trzech zmiennych.
import seaborn as sns
sns.set()
# %% Używając meteody pd.DataFrame.plot zbuduj histogramy dla kolejnych trzech zmiennych.
# normal (20 słupków)
data = {"normal": np.random.normal(loc=0, scale=1, size=20)}
data_frame_normal = pd.DataFrame(data)
data_plot = data_frame_normal.plot()
data_plot
# %% uniform (30 słupków)
data = {"uniform": np.random.uniform(low=0, high=1, size=20)}
data_frame_normal = pd.DataFrame(data)
data_plot = data_frame_normal.plot()
data_plot
# %% binomial
data = {"binomial": np.random.binomial(n=1, p=0.2, size=20)}
data_frame_normal = pd.DataFrame(data)
data_plot = data_frame_normal.plot()
data_plot

# %% Zapisz obiekt df do pliku 'dataframe.csv'
save = df.to_csv('dataframe.csv')

# %% Wczytaj do zmiennej df_new plik dataframe.csv
pd.read_csv('dataframe.csv', index_col=0)







