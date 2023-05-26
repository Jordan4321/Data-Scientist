import numpy as np
import pandas as pd

# %% Utwórz obiekt typu Series z podanej listy.
stocks = ['PLW', 'CDR', '11B', 'TEN']
series = pd.Series(stocks)
series

# %% Utwórz obiekt typu Series z podanego słownika i przypisz do zmiennej quotations.
stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(stocks)
quotations

# %% Przekształć obiekt quotations do listy. Przekształć obiekt quotations do tablicy numpy.
quotations = quotations.tolist()
print(quotations)
quotations = np.array(quotations)
quotations

# %% Przekształć obiekt quotations do obiektu DataFrame. Ustaw nazwę kolumny na price.
df = pd.DataFrame(quotations, columns=['Price'])
df

# %% Wykorzystując bibliotekę numpy zbuduj obiekt typu Series:
first = np.arange(101,110, dtype=int)
secound = np.arange(10,100,10,dtype=float)
join = np.concatenate((first,secound))
series = pd.Series(secound,first)
series

# %% Skonwertuj typ obiektu series na int. Skonwertuj typ obiektu series na float.
series = pd.Series(['001', '002', '003', '004'], list('abcd'))
series_int = series.astype(int)
series_float =  series.astype(float)
print(series_int)
print(series_float)

# %% Dodaj dwa elementy do quotations
stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quo = pd.Series({'BBT':25.5, 'F51':19.2})
quotations = pd.Series(data=stocks)
quotations = quotations.append(quo)
quotations

# %%  Obiekt quotations z poprzedniego ćwiczenia przekształć do obiektu typu
#     DataFrame. Zresetuj indeks i nadaj nazwy kolumn 'ticker' oraz 'price'.
quotations = quotations.to_frame().reset_index(names='Ticker')
quotations = quotations.rename(columns={0:'Price'})
print(quotations)

# %% Zbuduj poniższy obiekt DataFrame i przypisz do zmiennej companies:
    
#   company  	price	ticker
# 0	Amazon	    2375	AMZN.US
# 1	Microsoft	178.6	MSFT.US
# 2	Facebook	179.2	FB.US
companies = pd.DataFrame({'company':['Amazon','Microsoft','Facebook'], 
                          'price':[2375,178.6,179.2],
                          'ticker':['AMZN.US','MSFT.US','FB.US']})
companies

# %% Przekształć pierwszą kolumnę obiektu companies w indeks.
# Wytnij wiersz dla spółki Facebook z obiektu companies. 
# Wytnij cenę dla spółki Microsoft
companies_index = companies.set_index('company')
print(companies_index)
companies_facebook = companies.iloc[2]
print(companies_facebook)
price_microsoft = companies.iloc[1:2,1:2]
print(price_microsoft)
