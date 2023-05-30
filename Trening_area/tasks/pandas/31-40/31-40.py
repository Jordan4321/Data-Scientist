import numpy as np
import pandas as pd
import seaborn as sns

sns.set()

# %% Wczytaj plik csv do obiektu DataFrame o nazwie df_raw z domyślnymi 
# parametrami funkcji pd.read_csv() i wyświetl 5 pierwszych wierszy.
df_raw = pd.read_csv('Telco-customer-Churn.csv')
df_raw.loc[0:5,:]

# %% Skopiuj obiekt df_raw do zmiennej df.
df = df_raw
# %% Wyświetl podstawowe informacje na temat obiektu df.
df.info()
# %% Wyznacz liczbę brakujących elementów (np.nan) w obiekcie df dla każdej zmiennej.
df.isna().sum()
# df.isnull().sum()
# %% Zwróć uwagę na kolumnę TotalCharges. Typ tej kolumny to object.
df['TotalCharges'].value_counts()
df['TotalCharges'].value_counts()[:3].index
# %% Spróbuj zamienić brakujące wartości kolumny TotalCharges na jej medianę.
totalchargers_median = df['TotalCharges'][df['TotalCharges'] != ' '].median()
df.loc[df['TotalCharges'] == ' ', 'TotalCharges'] = totalchargers_median
df['TotalCharges'] = df['TotalCharges'].astype(float)
df.info()
# Sprawdź, czy typ został poprawnie zmieniony.
df.TotalCharges.dtype

# %% Kolumny z poniższej listy categorical przekształć do typu category.
categorical = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 
               'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
               'StreamingTV', 'Contract', 'StreamingMovies', 'PaperlessBilling', 'PaymentMethod', 'Churn']

for col in categorical:
  df[col] = pd.Categorical(df[col])
# %% Kolumny z poniższej listy numerical przekształć do typu float.
numerical = ['tenure', 'MonthlyCharges']

for col in numerical:
  df[col] = df[col].astype(float)
# %% Ustaw kolumnę customerID jako indeks obiektu df
df = df.set_index('customerID')
df.info()

# %% Użyj meteody describe() do wyświetlenia podstawowych statystyk obiektu df.
df.describe()
# Zauważ, że są to tylko zmienne numeryczne. Wyświetl podstawowe statystyki 
# zmiennych kategorycznych przekazując odpowiedni parametr include metody describe().
df.describe(include='category')

# %% Znajdź rozkład wartości zmiennej Churn
df['Churn'].value_counts()
# %% Zbuduj wykres kołowy rozkładu wartości zmiennej Churn.
x = df['Churn'].value_counts().plot.pie()
# %% Zbuduj wykres pairplot() z biblioteki seaborn. Przekaż zmienne:
# tenure, MonthlyCharges, TotalCharges oraz parametr: hue='Churn'.
df2 = df.loc[:, ['tenure','MonthlyCharges','TotalCharges']]
plot_sea = sns.pairplot(df, vars=df2, hue='Churn')

# %% Dokonaj mapowania kolumny Churn odpowiednio ('Yes'->1,'No'->0)
# Wyświetl 5 pierwszych wierszy obiektu df.
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
churn_map = df.head(5)
churn_map

# %% Wyznacz macierz korelacji dla obiektu df.
df.corr()

# %% Pogrupuj dane po zmiennej PaymentMethod i policz średnią wartość 
#    dla zmiennej TotalCharges.
pay_m = df.groupby('PaymentMethod')
print(pay_m['TotalCharges'].mean())

# %% Pobierz próbkę 10-ciu wierszy z obiektu df i zapisz do pliku sample_10.csv.
sample_10 = df.sample(n=10)
sample_10.to_csv('sample_10.csv')
