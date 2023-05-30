import pandas as pd
import numpy as np

# %% Wykorzystując funkcję fetch_financial_data() pobierz notowania dla spółki 
#    Google (Alphabet) i przypisz do zmiennej google. Wyświetl obiekt google.
def fetch_financial_data(company='GOOGL.US'):
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')
print(fetch_financial_data())
google_alphabet = fetch_financial_data()

# %% Wyświetl podstawowe informacje na temat obiektu google.
print(google_alphabet.info())
# %% Wyświetl podstawowe statystyki o obiekcie google.
print(google_alphabet.describe())
# %% Ustaw odpowiednie opcje biblioteki pandas, tak aby wyświetlać 
#    dane z dokładnością do dwóch miejsc po przecinku.
pd.set_option('display.float_format', lambda x: '%.2f' % x)
print(google_alphabet.describe())
# %% Zbuduj wykres ceny zamknięcia (Close) dla obiektu google.
google_alphabet['Close'].plot()

# %% Zamień indeks Date na kolumnę. Przypisz trwale zmiany do zniennej google.
data = google_alphabet.reset_index()
data

# %% Przypisz dwie nowe kolumny do obiektu google dodając kolumnę z aktualnym 
#    numerem miesiąca o nazwie 'Month', 'Day' oraz z rokiem o nazwie 'Year'.
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year
data['Day'] = data['Date'].dt.day
data

# %% Policz średnią cenę zamknięcia (Close) dla poszczególnego roku.
year_mean = data.groupby('Year')['Close'].mean()
print(year_mean)
# %% Otrzymane wartości przedstaw na wykresie wykorzystując metodę plot().
year_mean.plot(kind='bar')

# %% Policz średnią cenę zamknięcia (Close) dla miesiąca.
month_mean = data.groupby('Month')['Close'].mean()
month_mean
# %% Otrzymane wartości przedstaw na wykresie wykorzystując metodę plot().
month_mean.plot(kind='bar')

# %% Pogrupuj dane z obiektu google na poziomie roku i miesiąca.
#    Następnie policz wartość średnią.
year_month_mean = data.groupby(['Year','Month'])['Close'].mean()
year_month_mean

# %% Znajdź indeks dla którego kolumna Close przyjmuje wartość największą.
max_arg = data['Close'].argmax()
max_arg
# data['Close'].idxmax()
# %% Wytnij wiersz dla tego indeksu z obiektu google jako obiekt DataFrame. Odczytaj datę.
max_close = data.loc[data['Close'].argmax()]
max_close

# %% Z obiektu google wytnij kolumny Date, Open, Close, Volume. 
#    Nie zmieniaj pierwotnego obiektu google!
new_data = data.loc[:,["Date","Open","Close","Volume"]]
new_data

# %% Ustaw z powrotem indeks dla kolumny Date. Wyświetl obiekt google.
data = data.set_index("Date")
data

# %% Usuń na stałe kolumny Year i Month z obiektu google. Wyświetl obiekt google
data = data.drop(['Year',"Month",'Day'], axis=1)
data

# %% Przypisz polskie nazwy kolumn do obiektu google
data = data.rename(columns={"Open": "Otwarcie", "High": "Najwyzszy",
                            "Low":"Najnizszy",'Close':'Zamkniecie',
                            'Volume':'Wolumen'})
data


